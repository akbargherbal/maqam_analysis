# Maqam label analysis — maqam-167-v1

Generated from the completed run: **163 labels** for 163 usable ABCs, plus 4
corpus tracks with no ABC. The source is SheetSage2 12-TET ABC; there is **no
ground truth**. These are weak labels, not maqam verdicts.

Interactive dashboard: [`plots/index.html`](plots/index.html)

---

## 1. Headline findings

### The corpus is dominated by two 12-TET shadows

| Label | Songs | Share |
|---|---:|---:|
| Kurd | 66 | 40.5% |
| Nahawand | 61 | 37.4% |
| Withheld | 25 | 15.3% |
| Ajam | 4 | 2.5% |
| Rast | 4 | 2.5% |
| Hijaz | 2 | 1.2% |
| Nahawand (raised 7th) | 1 | 0.6% |

Kurd + Nahawand account for **127/163 labels (77.9%)**. That is not evidence
that four out of five songs "are" Kurd or Nahawand. Both are the exact 12-TET
shadows of **Bayati**, and Nahawand is also the relative-minor reading of many
other pitch-class sets. The analyzer cannot see the 150-cent second that would
separate them.

### Confidence is low by construction

| Overall confidence | Songs |
|---|---:|
| low | 134 (82.2%) |
| medium | 29 (17.8%) |
| high | 0 |

Why: the ABC is 12-TET, so shape confidence is capped at *medium*; 162/163
songs carry a **relative-mode ambiguity** flag (99.4%); 124/163 have *low*
tonic confidence. A **high** overall label would require evidence the file
cannot contain.

### One in six songs is withheld

25/163 (15.3%) are `withheld`:

- 19 because the analyzer said `name_allowed=false` (no single scale, too few
  pitch classes, or a quarter-tone-tonic case);
- 6 because the agent judged the tonic/scale evidence contradictory even though
  a partial scale was available.

Named labels have a mean fit of **0.982** (median 0.997); withheld labels have a
mean fit of **0.880**. The withheld set is genuinely the weaker evidence.

### The mode ambiguity is not a corner case

| Flag | Songs | Share |
|---|---:|---:|
| Same notes fit other tonics (relative modes) | 162 | 99.4% |
| Tonic / dominant split | 48 | 29.4% |
| No single scale explains the material | 17 | 10.4% |
| Only 4 pitch classes in use | 2 | 1.2% |

**93/163 songs (57.1%)** have at least two sections whose top tonic differs:
54/88 Elissa songs and 39/75 Fadl Shaker songs. Verse/chorus drift, modulation,
or weak sections all produce this. The whole-piece label is a summary, not a
stable tonal centre.

---

## 2. Artist comparison

| | Elissa | Fadl Shaker |
|---|---:|---:|
| Labels | 88 | 75 |
| Kurd | 39 | 27 |
| Nahawand | 32 | 29 |
| Withheld | 14 | 11 |
| Ajam | 2 | 2 |
| Rast | 0 | 4 |
| Hijaz | 0 | 2 |
| Nahawand (raised 7th) | 1 | 0 |
| Low / medium confidence | 74 / 14 | 60 / 15 |

- Elissa is **Kurd-leaning** (39 vs 32 Nahawand).
- Fadl Shaker is **balanced** (Nahawand 29 vs Kurd 27), and supplies **all four
  Rast** and **both Hijaz** labels.
- The tonic distributions differ: Elissa is led by E (18), D (11), A (10), F
  (10); Fadl is strongly G-centred (24), then A (14), C (7), D (7).
- Both artists have almost the same withholding rate (15.9% vs 14.7%), so the
  difference is not an artifact of one artist being harder.

See [`plots/02_artists.html`](plots/02_artists.html),
[`plots/02_albums_sunburst.html`](plots/02_albums_sunburst.html) and
[`plots/02_albums_heatmap.html`](plots/02_albums_heatmap.html).

---

## 3. Tonic and maqam structure

The most common tonics are **G (32), A (24), E (22), D (18), C (16)**, then
F (11), F# (10), B (9), Ab (7), Bb (7), C# (5), Eb (2).

- G is the single strongest centre, almost entirely from Fadl Shaker.
- Elissa spreads across E, D, A, F.
- The tonic × maqam heatmap shows that Kurd and Nahawand are not tied to one
  tonic; they occur across the circle, which is what a mode/shadow reading
  predicts.

See [`plots/04_tonic_maqam_heatmap.html`](plots/04_tonic_maqam_heatmap.html),
[`plots/04_tonic_distribution.html`](plots/04_tonic_distribution.html) and
[`plots/04_tonic_polar.html`](plots/04_tonic_polar.html).

---

## 4. Did the agent follow the evidence?

- **135/138 named labels (97.8%)** use the analyzer's displayed shape.
- **138/138 named labels** are within the analyzer's tied shapes (including the
  quarter-tone shadows).
- Only 6 labels are `possible`; the rest of the named labels are `consistent`.
- The agent withheld 6 songs beyond the analyzer's 19 `name_allowed=false`
  cases, all for contradictory tonic evidence.
- No label raises confidence above the analyzer's cap; `high` is unused.

This is the intended behaviour: the agent is a reviewer of the evidence, not a
second opinion from outside knowledge. See
[`plots/05_confidence_flow.html`](plots/05_confidence_flow.html) and
[`plots/03_fit_margin.html`](plots/03_fit_margin.html).

---

## 5. Duplicate-title consistency

The corpus contains **16 duplicate-title groups**, and **7 disagree** on the
label. Examples:

- كرمالك — Kurd vs Nahawand
- متى حبيبي متى — Kurd vs Nahawand
- بياع القلوب — Kurd, Nahawand, Kurd
- يا حبيبي تعال — Nahawand, Kurd, Nahawand
- طاير يا هوى — Rast vs Kurd
- اخدني معاك — Kurd, Kurd, Withheld, Kurd
- معقول — Nahawand vs Rast

These are the same shadow pairs the whole dataset struggles with, not random
noise. They are the best cheap audit set: a human can compare two recordings of
the same song and see whether the difference is real or an artifact of the ABC.
See [`plots/06_duplicates.html`](plots/06_duplicates.html).

---

## 6. What this dataset can and cannot support

**Can support**

- a distribution of "consistent with" / "possible" readings;
- tonic + scale-family hypotheses with explicit confidence;
- research on mode ambiguity, tonic/dominant splits and section drift;
- retrieval/filtering by maqam hypothesis with a confidence field;
- a seed set for human review or audio-based verification.

**Cannot support**

- claims that a song *is* maqam X;
- accuracy metrics — there is no ground truth;
- separating Nahawand from Bayati, Kurd from Bayati, or Ajam from Rast;
- seyir/jins-level analysis;
- treating the 25 withheld songs as failures — withholding is the correct
  output when the file cannot decide.

---

## 7. Recommended next steps

1. **Human spot-check the 7 duplicate disagreements.** They are the highest-value
   audit because the same title appears twice.
2. **Review the 25 withheld labels.** 19 are analyzer-declined; 6 are
   agent-declined. A quick read of the withheld reasons will show whether the
   threshold is too strict.
3. **Run the blind QC pass** (`review.py packet --qc --limit 20` → `qc.py compare`).
   This measures agreement, not accuracy, but it is the only reliability signal
   available without ground truth.
4. **If vocal stems ever become available**, run `analyze_f0.py` on the
   Nahawand/Kurd/Ajam/Rast subset. That is the only route that can measure the
   quarter-tone degrees and break the shadow ambiguity.
5. **Retry the 4 `no_abc` tracks** only with a GPU + SheetSage2; they are
   currently excluded from all plots and exports.

---

## 8. Files

| File | Contents |
|---|---|
| `plots/index.html` | interactive dashboard |
| `plots/01_overview.html` | label, status, confidence, flags, fit |
| `plots/02_artists.html` | maqam share and fit by artist |
| `plots/02_albums_sunburst.html` | artist → album → maqam |
| `plots/02_albums_heatmap.html` | album × maqam counts |
| `plots/03_fit_margin.html` | fit vs tonic margin scatter |
| `plots/03_margin_histogram.html` | tonic margin distribution |
| `plots/03_section_drift.html` | sections disagreeing on tonic |
| `plots/03_fit_by_maqam.html` | fit by named maqam |
| `plots/04_tonic_maqam_heatmap.html` | tonic × maqam |
| `plots/04_tonic_distribution.html` | tonic by artist |
| `plots/04_tonic_polar.html` | polar tonic view |
| `plots/05_confidence_flow.html` | label → status → confidences |
| `plots/05_confidence_heatmap.html` | tonic vs overall confidence |
| `plots/05_status_confidence.html` | status × confidence |
| `plots/06_duplicates.html` | duplicate-title consistency |
| `plots/label_data.csv` | tidy per-song data used by the plots |
| `maqam_labels.csv` | full export (167 rows) |
| `maqam_labels.jsonl` | full label objects |
| `summary.json` / `SUMMARY.md` | export summary and caveats |
