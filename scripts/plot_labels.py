#!/usr/bin/env python3
"""Build interactive Plotly views of the maqam labels and their evidence.

    python3 scripts/plot_labels.py

Outputs (self-contained, offline-capable):
    exports/plots/index.html
    exports/plots/01_overview.html
    exports/plots/02_artists_albums.html
    exports/plots/03_evidence.html
    exports/plots/04_tonic_maqam.html
    exports/plots/05_confidence.html
    exports/plots/06_duplicates.html
    exports/plots/label_data.csv

Every view is descriptive. The labels are weak labels from 12-TET ABC input;
there is no ground truth, and the plots are not an accuracy report.
"""
from __future__ import annotations

import json
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import load_config, load_manifest, path, read_json  # noqa: E402

OUT = path("exports/plots")
STATUS_ORDER = ["consistent", "possible", "withheld"]
STATUS_COLORS = {"consistent": "#2E86AB", "possible": "#F18F01", "withheld": "#8D99AE"}
CONF_ORDER = ["low", "medium", "high"]
CONF_COLORS = {"low": "#D1495B", "medium": "#EDAE49", "high": "#2A9D8F"}
MAQAM_COLORS = {
    "Kurd": "#4C78A8",
    "Nahawand": "#F58518",
    "Withheld": "#9E9E9E",
    "Ajam": "#54A24B",
    "Rast": "#B279A2",
    "Hijaz": "#E45756",
    "Nahawand (raised 7th)": "#72B7B2",
}
TONIC_ORDER = ["C", "C#", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B"]


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def load_rows() -> pd.DataFrame:
    cfg = load_config()
    manifest = {r["song_id"]: r for r in load_manifest(cfg)}
    labels = []
    for p in sorted(path("labels").glob("*.json")):
        if p.name.startswith("_"):
            continue
        obj = read_json(p)
        if isinstance(obj, dict) and obj.get("song_id"):
            labels.append(obj)
    if not labels:
        raise SystemExit("no labels found; run the labeling batches first")

    rows = []
    for label in labels:
        sid = label["song_id"]
        lab = label.get("label") or {}
        ev = label.get("evidence") or {}
        primary = ev.get("primary") or {}
        src = label.get("source") or {}
        rev = label.get("review") or {}
        m = manifest.get(sid, {})
        sections = ev.get("sections") or []
        section_tonics = {s.get("tonic") for s in sections if s.get("tonic")}
        flags = primary.get("flags") or []
        rows.append(
            {
                "song_id": sid,
                "artist": label.get("artist") or m.get("artist", ""),
                "album": label.get("album") or m.get("album", ""),
                "title": label.get("lyric_title") or label.get("file") or m.get("file", ""),
                "file": label.get("file") or m.get("file", ""),
                "maqam": lab.get("maqam") or "Withheld",
                "maqam_status": lab.get("maqam_status") or "withheld",
                "tonic": lab.get("tonic") or "",
                "tonic_confidence": lab.get("tonic_confidence") or "low",
                "overall_confidence": lab.get("overall_confidence") or "low",
                "scale_family": lab.get("scale_family") or "",
                "alternatives": "; ".join(lab.get("alternatives") or []),
                "tonic_alternatives": "; ".join(lab.get("tonic_alternatives") or []),
                "ghammaz": lab.get("ghammaz_candidate") or "",
                "fit": float(primary.get("fit") or 0.0),
                "tonic_margin": float(primary.get("tonic_margin") or 0.0),
                "analyzer_shape": primary.get("scale_shape") or "",
                "analyzer_tonic": primary.get("tonic") or "",
                "tied_shapes": "; ".join(primary.get("tied_shapes") or []),
                "shadow_of": "; ".join(primary.get("shadow_of") or []),
                "name_allowed": bool(primary.get("name_allowed")),
                "n_flags": len(flags),
                "flags": " | ".join(flags),
                "n_sections": len(sections),
                "section_tonics": len(section_tonics),
                "duration_s": float(src.get("duration_s") or m.get("duration_s") or 0.0),
                "notes_vocal": m.get("notes_vocal") or 0,
                "notes_ins": m.get("notes_ins") or 0,
                "batch_id": rev.get("batch_id") or lab.get("batch_id") or "",
                "reviewed_at": rev.get("reviewed_at") or "",
                "revision": (label.get("provenance") or {}).get("revision") or 1,
                "withheld_reason": lab.get("withheld_reason") or "",
                "rationale": lab.get("rationale") or "",
                "duplicate_of": m.get("duplicate_of") or "",
            }
        )
    df = pd.DataFrame(rows)
    df["maqam"] = pd.Categorical(df["maqam"], categories=ordered_maqams(df), ordered=True)
    df["maqam_status"] = pd.Categorical(df["maqam_status"], categories=STATUS_ORDER, ordered=True)
    df["overall_confidence"] = pd.Categorical(
        df["overall_confidence"], categories=CONF_ORDER, ordered=True
    )
    df["tonic_confidence"] = pd.Categorical(
        df["tonic_confidence"], categories=CONF_ORDER, ordered=True
    )
    return df


def ordered_maqams(df: pd.DataFrame) -> list[str]:
    counts = Counter(df["maqam"].astype(str))
    return [m for m, _ in counts.most_common() if m != "Withheld"] + (
        ["Withheld"] if counts.get("Withheld") else []
    )


def flag_category(flag: str) -> str:
    text = flag.lower()
    if "same notes also fit other tonics" in text:
        return "Relative-mode ambiguity"
    if "tonic/dominant split" in text:
        return "Tonic / dominant split"
    if "no single scale" in text:
        return "No single scale"
    if "only 4 pitch classes" in text or "pitch classes in use" in text:
        return "Too few pitch classes"
    return flag.split(":")[0][:48]


def style(fig: go.Figure, title: str, height: int = 560) -> go.Figure:
    fig.update_layout(
        template="plotly_white",
        title={"text": title, "x": 0.02, "xanchor": "left", "font": {"size": 20}},
        font={"family": "Inter, Arial, sans-serif", "size": 12, "color": "#22313F"},
        height=height,
        margin={"l": 60, "r": 30, "t": 80, "b": 60},
        legend={"orientation": "h", "yanchor": "bottom", "y": 1.02, "x": 0, "xanchor": "left"},
        hoverlabel={"font_size": 12},
    )
    return fig


def save(fig: go.Figure, name: str) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    fig.write_html(OUT / name, include_plotlyjs="directory", full_html=True)


# ------------------------------------------------------------------ 01 overview
def plot_overview(df: pd.DataFrame) -> None:
    maqams = ordered_maqams(df)
    fig = make_subplots(
        rows=2,
        cols=3,
        specs=[[{"type": "xy"}, {"type": "domain"}, {"type": "xy"}],
               [{"type": "xy"}, {"type": "xy"}, {"type": "xy"}]],
        subplot_titles=(
            "Maqam label",
            "Label status",
            "Overall confidence by status",
            "Tonic confidence",
            "Evidence flags",
            "Scale fit (1.0 = perfect)",
        ),
        vertical_spacing=0.18,
        horizontal_spacing=0.10,
    )

    # Maqam stacked by status.
    for status in STATUS_ORDER:
        sub = df[df["maqam_status"] == status]
        counts = sub.groupby("maqam", observed=False).size().reindex(maqams, fill_value=0)
        fig.add_trace(
            go.Bar(
                y=maqams,
                x=counts.values,
                orientation="h",
                name=status,
                marker_color=STATUS_COLORS[status],
                hovertemplate="%{y}<br>" + status + ": %{x}<extra></extra>",
            ),
            row=1,
            col=1,
        )

    # Status donut.
    status_counts = df["maqam_status"].value_counts().reindex(STATUS_ORDER, fill_value=0)
    fig.add_trace(
        go.Pie(
            labels=status_counts.index,
            values=status_counts.values,
            hole=0.55,
            marker_colors=[STATUS_COLORS[s] for s in status_counts.index],
            textinfo="label+value",
            hovertemplate="%{label}: %{value} (%{percent})<extra></extra>",
        ),
        row=1,
        col=2,
    )

    # Overall confidence stacked by status.
    for status in STATUS_ORDER:
        sub = df[df["maqam_status"] == status]
        counts = sub["overall_confidence"].value_counts().reindex(CONF_ORDER, fill_value=0)
        fig.add_trace(
            go.Bar(
                x=CONF_ORDER,
                y=counts.values,
                name=status,
                marker_color=STATUS_COLORS[status],
                showlegend=False,
                hovertemplate="%{x}: %{y}<extra></extra>",
            ),
            row=1,
            col=3,
        )

    # Tonic confidence.
    tc = df["tonic_confidence"].value_counts().reindex(CONF_ORDER, fill_value=0)
    fig.add_trace(
        go.Bar(
            x=CONF_ORDER,
            y=tc.values,
            marker_color=[CONF_COLORS[c] for c in CONF_ORDER],
            showlegend=False,
            text=tc.values,
            textposition="outside",
            hovertemplate="%{x}: %{y}<extra></extra>",
        ),
        row=2,
        col=1,
    )

    # Flags.
    flags = Counter(flag_category(f) for raw in df["flags"] for f in raw.split(" | ") if f)
    flag_names = [k for k, _ in flags.most_common(5)][::-1]
    fig.add_trace(
        go.Bar(
            y=flag_names,
            x=[flags[k] for k in flag_names],
            orientation="h",
            marker_color="#7A5195",
            showlegend=False,
            text=[flags[k] for k in flag_names],
            textposition="outside",
            hovertemplate="%{y}: %{x} songs<extra></extra>",
        ),
        row=2,
        col=2,
    )

    # Fit histogram.
    fig.add_trace(
        go.Histogram(
            x=df["fit"],
            nbinsx=20,
            marker_color="#2E86AB",
            showlegend=False,
            hovertemplate="fit %{x:.2f}: %{y} songs<extra></extra>",
        ),
        row=2,
        col=3,
    )
    fig.update_yaxes(autorange="reversed", row=1, col=1)
    fig.update_xaxes(title_text="songs", row=1, col=1)
    fig.update_yaxes(title_text="songs", row=1, col=3)
    fig.update_yaxes(title_text="songs", row=2, col=1)
    fig.update_xaxes(title_text="songs", row=2, col=2)
    fig.update_xaxes(title_text="fit", row=2, col=3)
    fig.update_layout(barmode="stack")
    style(fig, f"Maqam labels overview — {len(df)} labeled songs", height=720)
    save(fig, "01_overview.html")


# ----------------------------------------------------------- 02 artists/albums
def plot_artists_albums(df: pd.DataFrame) -> None:
    maqams = ordered_maqams(df)
    top = maqams[:8]
    work = df.copy()
    work["maqam_plot"] = work["maqam"].astype(str).where(work["maqam"].astype(str).isin(top), "Other")

    # Normalized maqam share per artist.
    share = (
        pd.crosstab(work["artist"], work["maqam_plot"], normalize="index")
        .reindex(columns=top + (["Other"] if "Other" in work["maqam_plot"].unique() else []), fill_value=0)
        * 100
    )
    fig = make_subplots(
        rows=1,
        cols=2,
        specs=[[{"type": "xy"}, {"type": "xy"}]],
        subplot_titles=("Maqam share by artist (%)", "Scale fit by artist"),
        column_widths=[0.55, 0.45],
    )
    for artist in share.index:
        fig.add_trace(
            go.Bar(
                x=share.columns,
                y=share.loc[artist].values,
                name=artist,
                hovertemplate="%{x}<br>" + artist + ": %{y:.1f}%<extra></extra>",
            ),
            row=1,
            col=1,
        )
    for artist in df["artist"].unique():
        sub = df[df["artist"] == artist]
        fig.add_trace(
            go.Box(
                y=sub["fit"],
                name=artist,
                boxpoints="all",
                jitter=0.35,
                pointpos=0,
                marker={"size": 4, "opacity": 0.55},
                showlegend=False,
                hovertemplate=artist + "<br>fit %{y:.3f}<extra></extra>",
            ),
            row=1,
            col=2,
        )
    fig.update_yaxes(title_text="% of labels", row=1, col=1)
    fig.update_yaxes(title_text="fit", row=1, col=2)
    fig.update_layout(barmode="group")
    style(fig, "Artist comparison", height=520)
    save(fig, "02_artists.html")

    # Sunburst artist -> album -> maqam.
    fig = px.sunburst(
        work,
        path=["artist", "album", "maqam_plot"],
        color="maqam_plot",
        color_discrete_map={**MAQAM_COLORS, "Other": "#BAB0AC"},
        hover_data={"fit": ":.3f", "overall_confidence": True},
    )
    fig.update_traces(textinfo="label+percent parent")
    style(fig, "Artist → album → maqam", height=760)
    fig.update_layout(legend={"orientation": "h", "y": -0.05})
    save(fig, "02_albums_sunburst.html")

    # Album x maqam heatmap.
    order = work.groupby("album", observed=True).size().sort_values(ascending=True).index
    matrix = (
        pd.crosstab(work["album"], work["maqam_plot"])
        .reindex(index=order, columns=top + (["Other"] if "Other" in work["maqam_plot"].unique() else []), fill_value=0)
    )
    fig = go.Figure(
        go.Heatmap(
            z=matrix.values,
            x=list(matrix.columns),
            y=list(matrix.index),
            colorscale="Blues",
            text=matrix.values,
            texttemplate="%{text}",
            hovertemplate="%{y}<br>%{x}: %{z} songs<extra></extra>",
            colorbar={"title": "songs"},
        )
    )
    style(fig, "Album × maqam count", height=760)
    fig.update_xaxes(title_text="maqam")
    fig.update_yaxes(title_text="album")
    save(fig, "02_albums_heatmap.html")


# ------------------------------------------------------------------ 03 evidence
def plot_evidence(df: pd.DataFrame) -> None:
    hover = ["artist", "tonic", "maqam_status", "overall_confidence", "tonic_margin", "fit", "flags"]
    fig = px.scatter(
        df,
        x="tonic_margin",
        y="fit",
        color="maqam",
        symbol="maqam_status",
        size="n_flags",
        size_max=18,
        hover_name="title",
        hover_data=hover,
        color_discrete_map=MAQAM_COLORS,
        labels={"tonic_margin": "tonic margin (cue agreement)", "fit": "scale fit"},
    )
    fig.add_hline(y=0.90, line_dash="dash", line_color="#D1495B",
                  annotation_text="fit 0.90: no single scale below this")
    fig.add_vline(x=0.08, line_dash="dot", line_color="#8D99AE",
                  annotation_text="margin 0.08")
    style(fig, "Evidence: fit vs tonic margin (size = number of flags)", height=650)
    save(fig, "03_fit_margin.html")

    # Margin distribution by status.
    fig = px.histogram(
        df,
        x="tonic_margin",
        color="maqam_status",
        nbins=24,
        barmode="overlay",
        opacity=0.72,
        color_discrete_map=STATUS_COLORS,
        labels={"tonic_margin": "tonic margin", "count": "songs"},
    )
    style(fig, "Tonic margin distribution", height=460)
    save(fig, "03_margin_histogram.html")

    # Section tonic drift.
    drift = (
        df.assign(has_drift=df["section_tonics"] > 1)
        .groupby(["artist", "has_drift"], observed=True)
        .size()
        .unstack(fill_value=0)
        .rename(columns={False: "one tonic", True: "sections disagree"})
    )
    fig = go.Figure()
    for col, color in (("one tonic", "#8D99AE"), ("sections disagree", "#D1495B")):
        if col in drift:
            fig.add_trace(
                go.Bar(
                    x=drift.index,
                    y=drift[col],
                    name=col,
                    marker_color=color,
                    text=drift[col],
                    textposition="outside",
                    hovertemplate="%{x}<br>" + col + ": %{y}<extra></extra>",
                )
            )
    fig.update_layout(barmode="group")
    style(fig, "Songs whose sections disagree on the top tonic", height=460)
    fig.update_yaxes(title_text="songs")
    save(fig, "03_section_drift.html")

    # Fit by maqam.
    named = df[df["maqam"] != "Withheld"]
    order = named.groupby("maqam", observed=True)["fit"].median().sort_values().index
    fig = px.box(
        named,
        x="maqam",
        y="fit",
        color="maqam",
        points="all",
        category_orders={"maqam": list(order)},
        color_discrete_map=MAQAM_COLORS,
        labels={"fit": "scale fit"},
    )
    fig.update_layout(showlegend=False)
    style(fig, "Scale fit by named maqam (withheld excluded)", height=520)
    save(fig, "03_fit_by_maqam.html")


# --------------------------------------------------------------- 04 tonic/maqam
def plot_tonic_maqam(df: pd.DataFrame) -> None:
    maqams = ordered_maqams(df)
    matrix = (
        pd.crosstab(df["tonic"], df["maqam"])
        .reindex(index=[t for t in TONIC_ORDER if t in set(df["tonic"])], columns=maqams, fill_value=0)
    )
    fig = go.Figure(
        go.Heatmap(
            z=matrix.values,
            x=list(matrix.columns),
            y=list(matrix.index),
            colorscale="Viridis",
            text=matrix.values,
            texttemplate="%{text}",
            hovertemplate="tonic %{y}<br>%{x}: %{z} songs<extra></extra>",
            colorbar={"title": "songs"},
        )
    )
    style(fig, "Tonic × maqam", height=560)
    fig.update_xaxes(title_text="maqam")
    fig.update_yaxes(title_text="tonic")
    save(fig, "04_tonic_maqam_heatmap.html")

    fig = px.histogram(
        df,
        x="tonic",
        color="artist",
        category_orders={"tonic": TONIC_ORDER},
        barmode="group",
        labels={"tonic": "tonic (qarar)", "count": "songs"},
    )
    style(fig, "Tonic distribution", height=460)
    save(fig, "04_tonic_distribution.html")

    # Pitch-class circle order; simple polar bar of tonic counts.
    tonic_counts = df["tonic"].value_counts().reindex(
        [t for t in TONIC_ORDER if t in set(df["tonic"])], fill_value=0
    )
    fig = go.Figure(
        go.Barpolar(
            r=tonic_counts.values,
            theta=tonic_counts.index,
            marker_color=tonic_counts.values,
            marker_colorscale="Viridis",
            text=tonic_counts.values,
            hovertemplate="%{theta}: %{r} songs<extra></extra>",
        )
    )
    style(fig, "Tonic distribution (polar)", height=560)
    fig.update_layout(polar={"angularaxis": {"direction": "clockwise"}})
    save(fig, "04_tonic_polar.html")


# ------------------------------------------------------------------ 05 confidence
def plot_confidence(df: pd.DataFrame) -> None:
    # Parallel categories: label -> status -> tonic conf -> overall conf.
    subset = df.copy()
    subset["maqam"] = subset["maqam"].astype(str)
    fig = px.parallel_categories(
        subset,
        dimensions=["maqam", "maqam_status", "tonic_confidence", "overall_confidence"],
        color="fit",
        color_continuous_scale="Viridis",
        labels={
            "maqam": "label",
            "maqam_status": "status",
            "tonic_confidence": "tonic conf.",
            "overall_confidence": "overall conf.",
            "fit": "fit",
        },
    )
    style(fig, "Confidence flow: label → status → tonic confidence → overall confidence", height=620)
    save(fig, "05_confidence_flow.html")

    # Heatmap tonic vs overall confidence.
    matrix = pd.crosstab(
        df["tonic_confidence"], df["overall_confidence"]
    ).reindex(index=CONF_ORDER, columns=CONF_ORDER, fill_value=0)
    fig = go.Figure(
        go.Heatmap(
            z=matrix.values,
            x=list(matrix.columns),
            y=list(matrix.index),
            colorscale="Blues",
            text=matrix.values,
            texttemplate="%{text}",
            hovertemplate="tonic %{y}<br>overall %{x}: %{z}<extra></extra>",
            colorbar={"title": "songs"},
        )
    )
    style(fig, "Tonic confidence vs overall confidence", height=460)
    fig.update_xaxes(title_text="overall confidence")
    fig.update_yaxes(title_text="tonic confidence")
    save(fig, "05_confidence_heatmap.html")

    # Status by overall confidence.
    fig = px.histogram(
        df,
        x="overall_confidence",
        color="maqam_status",
        category_orders={"overall_confidence": CONF_ORDER, "maqam_status": STATUS_ORDER},
        color_discrete_map=STATUS_COLORS,
        barmode="group",
        labels={"overall_confidence": "overall confidence", "count": "songs"},
    )
    style(fig, "Overall confidence by label status", height=460)
    save(fig, "05_status_confidence.html")


# ------------------------------------------------------------------ 06 duplicates
def plot_duplicates(df: pd.DataFrame) -> None:
    groups = defaultdict(list)
    for _, row in df.iterrows():
        key = (row["title"] or row["file"]).strip()
        if key:
            groups[key].append(row)
    dup = [(title, members) for title, members in groups.items() if len(members) > 1]
    dup.sort(key=lambda x: (-len(x[1]), x[0]))
    rows = []
    for title, members in dup:
        labels = [m["maqam"] for m in members]
        rows.append(
            {
                "title": title,
                "n": len(members),
                "labels": ", ".join(str(x) for x in labels),
                "agree": len(set(labels)) == 1,
                "songs": "<br>".join(f"{m['artist']} — {m['album']}" for m in members),
            }
        )
    agree = sum(r["agree"] for r in rows)
    fig = make_subplots(
        rows=1,
        cols=2,
        specs=[[{"type": "domain"}, {"type": "table"}]],
        column_widths=[0.28, 0.72],
        subplot_titles=("Duplicate-title agreement", "Groups"),
    )
    fig.add_trace(
        go.Pie(
            labels=["agree", "disagree"],
            values=[agree, len(rows) - agree],
            hole=0.55,
            marker_colors=["#2A9D8F", "#D1495B"],
            textinfo="label+value",
        ),
        row=1,
        col=1,
    )
    fig.add_trace(
        go.Table(
            header={
                "values": ["title", "n", "labels", "agree"],
                "fill_color": "#22313F",
                "font_color": "white",
                "align": "left",
            },
            cells={
                "values": [
                    [r["title"] for r in rows],
                    [r["n"] for r in rows],
                    [r["labels"] for r in rows],
                    ["yes" if r["agree"] else "NO" for r in rows],
                ],
                "fill_color": [["#F4F7F9", "#FFFFFF"] * len(rows)],
                "align": "left",
                "height": 26,
            },
        ),
        row=1,
        col=2,
    )
    style(fig, "Duplicate-title consistency (a descriptive check, not ground truth)", height=720)
    save(fig, "06_duplicates.html")


# ---------------------------------------------------------------------- index
def write_index(df: pd.DataFrame) -> None:
    maqam_counts = df["maqam"].value_counts()
    status_counts = df["maqam_status"].value_counts()
    conf_counts = df["overall_confidence"].value_counts()
    flag_counts = Counter(flag_category(f) for raw in df["flags"] for f in raw.split(" | ") if f)
    top_flags = "".join(
        f"<li>{k}: <b>{v}</b></li>" for k, v in flag_counts.most_common(4)
    )
    top_maqams = "".join(
        f"<li>{m}: <b>{int(c)}</b></li>" for m, c in maqam_counts.head(7).items()
    )
    links = [
        ("01_overview.html", "Overview", "Label distribution, status, confidence, flags, fit"),
        ("02_artists.html", "Artists", "Maqam share and fit by artist"),
        ("02_albums_sunburst.html", "Albums sunburst", "Artist → album → maqam"),
        ("02_albums_heatmap.html", "Albums heatmap", "Album × maqam counts"),
        ("03_fit_margin.html", "Fit vs tonic margin", "The central evidence scatter"),
        ("03_margin_histogram.html", "Tonic margin", "How often the cues agree"),
        ("03_section_drift.html", "Section drift", "Songs whose sections disagree"),
        ("03_fit_by_maqam.html", "Fit by maqam", "Named labels only"),
        ("04_tonic_maqam_heatmap.html", "Tonic × maqam", "Where each maqam sits"),
        ("04_tonic_distribution.html", "Tonic distribution", "By artist"),
        ("04_tonic_polar.html", "Tonic polar", "Circular view"),
        ("05_confidence_flow.html", "Confidence flow", "Label → status → confidences"),
        ("05_confidence_heatmap.html", "Confidence heatmap", "Tonic vs overall"),
        ("05_status_confidence.html", "Status × confidence", "Distribution"),
        ("06_duplicates.html", "Duplicates", "Duplicate-title agreement"),
    ]
    cards = "".join(
        f'<a class="card" href="{href}"><h3>{title}</h3><p>{desc}</p></a>'
        for href, title, desc in links
    )
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Maqam labels — interactive analysis</title>
<style>
  :root {{ --ink:#22313F; --muted:#667; --line:#E3E8EE; --bg:#F7F9FB; --accent:#2E86AB; }}
  * {{ box-sizing:border-box; }}
  body {{ margin:0; font-family:Inter, Arial, sans-serif; color:var(--ink); background:var(--bg); }}
  header {{ padding:42px 7vw 20px; background:white; border-bottom:1px solid var(--line); }}
  h1 {{ margin:0 0 8px; font-size:30px; letter-spacing:-0.02em; }}
  .sub {{ color:var(--muted); max-width:900px; line-height:1.55; }}
  main {{ padding:26px 7vw 60px; }}
  .grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(230px,1fr)); gap:14px; margin:18px 0 30px; }}
  .stat {{ background:white; border:1px solid var(--line); border-radius:14px; padding:18px 20px; }}
  .stat .n {{ font-size:30px; font-weight:700; color:var(--accent); }}
  .stat .l {{ color:var(--muted); font-size:13px; text-transform:uppercase; letter-spacing:.06em; }}
  .two {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(280px,1fr)); gap:18px; }}
  .panel {{ background:white; border:1px solid var(--line); border-radius:14px; padding:18px 22px; }}
  .panel h2 {{ font-size:16px; margin:0 0 10px; }}
  .panel ul {{ margin:0; padding-left:18px; line-height:1.8; }}
  .cards {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(240px,1fr)); gap:14px; margin-top:18px; }}
  .card {{ display:block; background:white; border:1px solid var(--line); border-radius:14px; padding:16px 18px; text-decoration:none; color:inherit; transition:.15s; }}
  .card:hover {{ border-color:var(--accent); transform:translateY(-1px); box-shadow:0 8px 24px rgba(34,49,63,.07); }}
  .card h3 {{ margin:0 0 6px; font-size:15px; }}
  .card p {{ margin:0; color:var(--muted); font-size:13px; line-height:1.5; }}
  .caveat {{ margin-top:26px; padding:16px 20px; border-left:4px solid #F18F01; background:#FFF8EC; border-radius:8px; color:#5a4a2a; line-height:1.55; }}
  footer {{ color:var(--muted); font-size:12px; margin-top:28px; }}
</style>
</head>
<body>
<header>
  <h1>Maqam labels — interactive analysis</h1>
  <p class="sub">163 labeled songs from Elissa and Fadl Shaker, derived from SheetSage2 ABC transcriptions.
  These are <b>weak labels</b> with no ground truth. Quarter-tone maqamat are marked <i>possible</i>, never stated as fact.
  The plots describe label distribution and evidence, not accuracy.</p>
</header>
<main>
  <div class="grid">
    <div class="stat"><div class="n">{len(df)}</div><div class="l">labeled songs</div></div>
    <div class="stat"><div class="n">{int(status_counts.get("withheld", 0))}</div><div class="l">withheld</div></div>
    <div class="stat"><div class="n">{int(conf_counts.get("low", 0))}</div><div class="l">low overall confidence</div></div>
    <div class="stat"><div class="n">{int(conf_counts.get("medium", 0))}</div><div class="l">medium overall confidence</div></div>
    <div class="stat"><div class="n">{len(flag_counts)}</div><div class="l">distinct evidence flags</div></div>
  </div>
  <div class="two">
    <div class="panel"><h2>Top labels</h2><ul>{top_maqams}</ul></div>
    <div class="panel"><h2>Evidence flags</h2><ul>{top_flags}</ul></div>
  </div>
  <h2 style="margin:34px 0 4px;font-size:20px">Views</h2>
  <div class="cards">{cards}</div>
  <div class="caveat"><b>Reading this correctly:</b> a label is a hypothesis about a 12-TET transcription, not a claim about the recording.
  Nahawand can be a rounded Bayati; Kurd can be a rounded Bayati; Ajam can be a rounded Rast. The 25 withheld labels are cases where the
  analyzer declined a scale or the evidence was contradictory. The 4 corpus tracks with no ABC are not in these plots.</div>
  <footer>Generated {utc_now()} · run maqam-167-v1 · pipeline exports/plots</footer>
</main>
</body>
</html>
"""
    (OUT / "index.html").write_text(html, encoding="utf-8")


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    df = load_rows()
    df.to_csv(OUT / "label_data.csv", index=False, encoding="utf-8")
    plot_overview(df)
    plot_artists_albums(df)
    plot_evidence(df)
    plot_tonic_maqam(df)
    plot_confidence(df)
    plot_duplicates(df)
    write_index(df)
    print(f"wrote {len(df)} labels -> {OUT}")
    for p in sorted(OUT.glob("*.html")):
        print(f"  {p}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
