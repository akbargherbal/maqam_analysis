# Maqam review — batch-001 (2 songs)

Read `skills/maqam-analysis/SKILL.md` before deciding. Hard rules:
- 12-TET ABC cannot prove quarter tones. Quarter-tone maqamat (Rast, Bayati, Saba, Sikah, Huzam, Iraq, Awj Ara, Suznek, Jiharkah, Bastanikar) are status `possible`, never `consistent`.
- If the analyzer says `name_allowed=false`, a scale is not identified, parse <95%, or pitch classes are too few: use `maqam_status="withheld"`.
- Confidence can be lowered, never raised above the tool's evidence.
- A tonic/dominant split must name the other tonic in `tonic_alternatives`.
- Never import outside knowledge of the song. Evidence is the ABC only.

Fill the sibling template, then run:
```bash
python3 scripts/review.py record --batch work/review/batch-001.json \
  --labels work/review/batch-001.labels.json
```

## 1. `elissa-1998-baddy-doub-01-baddy-doub` — Elissa — Elissa - 1998 Baddy Doub — "بدي دوب"
- file: `01. Baddy Doub.mp3` | duration 236.8s | declared key Em | tempo 101.0 | voice Vocal
- parse: 100% of bars
- pitch classes: F# 32%, G 25%, E 20%, D 9%, C 7%, B 6%
- tonic: E (low, margin 0.019) | cues: most-used note -> F#; phrase endings -> F#; tool key & chords* -> E (key) / D (commonest chord root); other voice -> B
- scale: Nahawand [natural minor / Aeolian] (fit 0.98, shape confidence medium, name_allowed=True) | tied: Bayati, Nahawand | 12-TET shadow of: Bayati
- candidate ghammaz: B (700c, 46% of phrase endings)
- flags: same notes also fit other tonics: B (0.98), D (0.98)  -> relative-mode ambiguity
- sections:
  - Section: verse: F# low / Kurd low (fit 0.714)  [!] same notes also fit other tonics: E (0.98), B (0.98), C (0.98)  -> relative-mode ambiguity
  - Section: pre-chorus: E low / Nahawand medium (fit 1.0)  [!] tonic/dominant split: E and B (a 4th/5th apart) score almost equally; the true tonic could be either
  - Section: chorus: E low / Nahawand low (fit 0.94)  [!] same notes also fit other tonics: F# (0.93), G (0.94), D (0.94)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): F# low / Kurd low (fit 0.844)
- full report: `work/elissa-1998-baddy-doub-01-baddy-doub/report.md`
## 2. `elissa-1998-baddy-doub-02-da-lolak` — Elissa — Elissa - 1998 Baddy Doub — "ده لولاك"
- file: `02. Da Lolak.mp3` | duration 292.911s | declared key Fm | tempo 115.0 | voice Vocal
- parse: 100% of bars
- pitch classes: Eb 23%, F 22%, G 22%, C 16%, C# 11%, Bb 5%
- tonic: C (low, margin 0.115) | cues: most-used note -> Eb; phrase endings -> C; tool key & chords* -> F (key) / C (commonest chord root); other voice -> F
- scale: Kurd [Phrygian] (fit 0.967, shape confidence medium, name_allowed=True) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- candidate ghammaz: G (700c, 25% of phrase endings)
- flags: tonic/dominant split: C and F (a 4th/5th apart) score almost equally; the true tonic could be either | same notes also fit other tonics: F (0.97), Eb (0.97)  -> relative-mode ambiguity
- sections:
  - Section: chorus: C low / Kurd low (fit 0.946)  [!] same notes also fit other tonics: F (0.95), Eb (0.95)  -> relative-mode ambiguity
  - Section: verse: G low / Nahawand low (fit 0.785)  [!] same notes also fit other tonics: F (0.97), C (0.97), Eb (0.97)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): C low / Kurd medium (fit 0.967)
- full report: `work/elissa-1998-baddy-doub-02-da-lolak/report.md`
