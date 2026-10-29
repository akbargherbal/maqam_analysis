# Maqam review — batch-002 (8 songs)

Read `skills/maqam-analysis/SKILL.md` before deciding. Hard rules:
- 12-TET ABC cannot prove quarter tones. Quarter-tone maqamat (Rast, Bayati, Saba, Sikah, Huzam, Iraq, Awj Ara, Suznek, Jiharkah, Bastanikar) are status `possible`, never `consistent`.
- If the analyzer says `name_allowed=false`, a scale is not identified, parse <95%, or pitch classes are too few: use `maqam_status="withheld"`.
- Confidence can be lowered, never raised above the tool's evidence.
- A tonic/dominant split must name the other tonic in `tonic_alternatives`.
- Never import outside knowledge of the song. Evidence is the ABC only.

Fill the sibling template, then run:
```bash
python3 scripts/review.py record --batch work/review/batch-002.json \
  --labels work/review/batch-002.labels.json
```

## 1. `elissa-1998-baddy-doub-10-helm-alahlam-mix` — Elissa — Elissa - 1998 Baddy Doub — "حلم الاحلام"
- file: `10. Helm Alahlam Mix.mp3` | duration 257.463s | declared key Dm | tempo 94.0 | voice Vocal
- parse: 100% of bars
- pitch classes: E 24%, D 21%, F 19%, C 17%, Bb 7%, A 7%
- tonic: D (low, margin 0.31) | cues: most-used note -> E; phrase endings -> D; tool key & chords* -> D (key) / C (commonest chord root); other voice -> A
- scale: Nahawand [natural minor / Aeolian] (fit 1.0, shape confidence medium, name_allowed=True) | tied: Bayati, Nahawand | 12-TET shadow of: Bayati
- candidate ghammaz: A (700c, 21% of phrase endings)
- flags: same notes also fit other tonics: A (1.00), C (1.00)  -> relative-mode ambiguity
- sections:
  - Section: verse: D medium / Nahawand medium (fit 1.0)  [!] same notes also fit other tonics: A (1.00), C (1.00)  -> relative-mode ambiguity
  - Section: chorus: D low / Nahawand medium (fit 0.98)  [!] same notes also fit other tonics: C (0.98), A (0.98), E (0.97)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): D low / Nahawand medium (fit 1.0)
- full report: `work/elissa-1998-baddy-doub-10-helm-alahlam-mix/report.md`
## 2. `elissa-2000-wakherta-maak-01-betghib-betrouh` — Elissa — Elissa - 2000 Wakherta Maak — "بتغيب بتروح"
- file: `01.Betghib Betrouh.mp3` | duration 261.776s | declared key Fm | tempo 104.0 | voice Vocal
- parse: 100% of bars
- pitch classes: F 23%, G 18%, Eb 14%, Ab 13%, C# 12%, C 10%
- tonic: F (low, margin 0.018) | cues: most-used note -> F; phrase endings -> C; tool key & chords* -> F (key) / C (commonest chord root); other voice -> C
- scale: Nahawand [natural minor / Aeolian] (fit 0.982, shape confidence medium, name_allowed=True) | tied: Bayati, Nahawand | 12-TET shadow of: Bayati
- candidate ghammaz: C (700c, 29% of phrase endings)
- flags: tonic/dominant split: F and C (a 4th/5th apart) score almost equally; the true tonic could be either | same notes also fit other tonics: C (0.98), C# (0.98), Eb (0.98)  -> relative-mode ambiguity
- sections:
  - Section: verse: C low / Kurd medium (fit 0.98)  [!] same notes also fit other tonics: F (0.98), C# (0.98)  -> relative-mode ambiguity
  - Section: pre-chorus: Bb medium / Kurd low (fit 0.924)  [!] same notes also fit other tonics: Ab (0.92), Eb (0.92)  -> relative-mode ambiguity
  - Section: chorus: F low / Nahawand medium (fit 1.0)  [!] tonic/dominant split: F and C (a 4th/5th apart) score almost equally; the true tonic could be either
- melody-only cross-check (chords removed): F low / Nahawand medium (fit 0.982)
- full report: `work/elissa-2000-wakherta-maak-01-betghib-betrouh/report.md`
## 3. `elissa-2000-wakherta-maak-02-daa-el-e-nwann` — Elissa — Elissa - 2000 Wakherta Maak — "ضاع العنوان"
- file: `02.Daa El E'nwann.mp3` | duration 277.92s | declared key Fm | tempo 96.0 | voice Vocal
- parse: 100% of bars
- pitch classes: G 21%, F 21%, C# 17%, Eb 17%, C 15%, Ab 6%
- tonic: F (high, margin 0.237) | cues: most-used note -> G; phrase endings -> F; tool key & chords* -> F (key) / C (commonest chord root); other voice -> F
- scale: Nahawand [natural minor / Aeolian] (fit 0.998, shape confidence medium, name_allowed=True) | tied: Bayati, Nahawand | 12-TET shadow of: Bayati
- candidate ghammaz: C (700c, 40% of phrase endings)
- flags: same notes also fit other tonics: C (1.00), C# (1.00)  -> relative-mode ambiguity
- sections:
  - Section: verse: C low / Kurd medium (fit 0.96)  [!] same notes also fit other tonics: Eb (0.96), C# (0.96)  -> relative-mode ambiguity
  - Section: chorus: F high / Nahawand medium (fit 0.997)  [!] same notes also fit other tonics: C# (1.00), C (1.00)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): F high / Nahawand medium (fit 0.998)
- full report: `work/elissa-2000-wakherta-maak-02-daa-el-e-nwann/report.md`
## 4. `elissa-2000-wakherta-maak-03-w-akherta-maak` — Elissa — Elissa - 2000 Wakherta Maak — "واخرتها معاك"
- file: `03.W'akherta Maak.mp3` | duration 337.087s | declared key Am | tempo 136.0 | voice Vocal
- parse: 100% of bars
- pitch classes: D 24%, E 19%, F 15%, C 13%, A 12%, G 9%
- tonic: A (low, margin 0.072) | cues: most-used note -> D; phrase endings -> A; tool key & chords* -> A (key) / A (commonest chord root); other voice -> A
- scale: Nahawand [natural minor / Aeolian] (fit 0.85, shape confidence low, name_allowed=False) | tied: Bayati, Nahawand | 12-TET shadow of: Bayati
- candidate ghammaz: D (500c, 33% of phrase endings)
- flags: tonic/dominant split: A and D (a 4th/5th apart) score almost equally; the true tonic could be either | same notes also fit other tonics: D (0.85), E (0.85), F (0.85)  -> relative-mode ambiguity | no single scale explains this material (best fit 0.85); expect modulation, chromatic writing or quarter tones; do not name one maqam
- sections:
  - Section: verse: D low / (no standard maqam) low (fit 0.912)  [!] same notes also fit other tonics: A (0.91), C (0.91), E (0.91)  -> relative-mode ambiguity
  - Section: chorus: A low / Nahawand low (fit 0.839)  [!] same notes also fit other tonics: E (0.84), D (0.84), G (0.84)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): A medium / Nahawand low (fit 0.85)
- full report: `work/elissa-2000-wakherta-maak-03-w-akherta-maak/report.md`
## 5. `elissa-2000-wakherta-maak-04-haram` — Elissa — Elissa - 2000 Wakherta Maak — "حرام"
- file: `04.Haram.mp3` | duration 248.846s | declared key C#m | tempo 116.0 | voice Vocal
- parse: 100% of bars
- pitch classes: A 24%, Eb 16%, E 15%, Ab 15%, F# 11%, B 10%
- tonic: A (low, margin 0.068) | cues: most-used note -> A; phrase endings -> A; tool key & chords* -> C# (key) / C# (commonest chord root); other voice -> Ab
- scale: (no standard maqam) [Lydian] (fit 0.982, shape confidence medium, name_allowed=True) | tied: (no standard maqam)
- candidate ghammaz: Eb (600c, 20% of phrase endings)
- flags: same notes also fit other tonics: Ab (0.98), C# (0.98)  -> relative-mode ambiguity
- sections:
  - Section: verse: A medium / (no standard maqam) low (fit 0.93)  [!] same notes also fit other tonics: Ab (0.93), C# (0.93)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): A low / (no standard maqam) medium (fit 0.982)
- full report: `work/elissa-2000-wakherta-maak-04-haram/report.md`
## 6. `elissa-2000-wakherta-maak-05-minn-albi-tmanayt` — Elissa — Elissa - 2000 Wakherta Maak — "من قلبي غنيت"
- file: `05.Minn Albi Tmanayt.mp3` | duration 178.759s | declared key D#m | tempo 127.0 | voice Vocal
- parse: 100% of bars
- pitch classes: Bb 24%, F# 19%, F 18%, B 13%, Eb 10%, Ab 9%
- tonic: Eb (low, margin 0.097) | cues: most-used note -> Bb; phrase endings -> Eb; tool key & chords* -> Eb (key) / Eb (commonest chord root); other voice -> Bb
- scale: Nahawand [natural minor / Aeolian] (fit 0.969, shape confidence medium, name_allowed=True) | tied: Bayati, Nahawand | 12-TET shadow of: Bayati
- candidate ghammaz: Bb (700c, 44% of phrase endings)
- flags: same notes also fit other tonics: Bb (0.97), B (0.97), F# (0.97)  -> relative-mode ambiguity
- sections:
  - Section: verse: Eb low / Nahawand (raised 7th) medium (fit 0.96)  [!] tonic/dominant split: Eb and Bb (a 4th/5th apart) score almost equally; the true tonic could be either
  - Section: chorus: Eb low / Nahawand low (fit 0.909)  [!] same notes also fit other tonics: Bb (0.91), F# (0.91), B (0.91)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): Eb low / Nahawand medium (fit 0.969)
- full report: `work/elissa-2000-wakherta-maak-05-minn-albi-tmanayt/report.md`
## 7. `elissa-2000-wakherta-maak-06-wahyatt-el-hob` — Elissa — Elissa - 2000 Wakherta Maak — "وحياة الحب"
- file: `06.Wahyatt El Hob.mp3` | duration 270.005s | declared key Dm | tempo 104.0 | voice Vocal
- parse: 100% of bars
- pitch classes: F 20%, C 19%, G 16%, Eb 15%, C# 10%, Bb 6%
- tonic: C (low, margin 0.196) | cues: most-used note -> F; phrase endings -> C; tool key & chords* -> C (key) / C (commonest chord root); other voice -> G
- scale: Kurd [Phrygian] (fit 0.809, shape confidence low, name_allowed=False) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- candidate ghammaz: F (500c, 50% of phrase endings)
- flags: same notes also fit other tonics: F (0.81), Bb (0.81)  -> relative-mode ambiguity | no single scale explains this material (best fit 0.81); expect modulation, chromatic writing or quarter tones; do not name one maqam
- sections:
  - Section: verse: C high / Kurd medium (fit 1.0)  [!] same notes also fit other tonics: F (1.00), C# (1.00), Bb (1.00)  -> relative-mode ambiguity
  - Section: chorus: C low / (no standard maqam) low (fit 0.784)  [!] same notes also fit other tonics: D (0.78), Eb (0.78), F (0.78)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): C low / Kurd low (fit 0.809)
- full report: `work/elissa-2000-wakherta-maak-06-wahyatt-el-hob/report.md`
## 8. `elissa-2000-wakherta-maak-07-ramchet-ayn` — Elissa — Elissa - 2000 Wakherta Maak — "رمشة عين"
- file: `07.Ramchet Ayn.mp3` | duration 280.375s | declared key F#m | tempo 121.0 | voice Vocal
- parse: 100% of bars
- pitch classes: Ab 26%, F# 26%, E 16%, D 10%, C# 9%, A 8%
- tonic: F# (low, margin 0.058) | cues: most-used note -> Ab; phrase endings -> Ab; tool key & chords* -> F# (key) / F# (commonest chord root); other voice -> Ab
- scale: Nahawand [natural minor / Aeolian] (fit 0.904, shape confidence low, name_allowed=True) | tied: Bayati, Nahawand | 12-TET shadow of: Bayati
- candidate ghammaz: C# (700c, 8% of phrase endings)
- flags: same notes also fit other tonics: C# (0.90), E (0.90)  -> relative-mode ambiguity
- sections:
  - Section: verse: C# low / Kurd medium (fit 1.0)  [!] same notes also fit other tonics: F# (1.00), E (1.00), D (1.00)  -> relative-mode ambiguity
  - Section: pre-chorus: F# medium / Nahawand medium (fit 0.956)  [!] same notes also fit other tonics: E (0.96), D (0.96)  -> relative-mode ambiguity
  - Section: chorus: F# low / Nahawand low (fit 0.864)  [!] same notes also fit other tonics: A (0.86), E (0.86)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): F# low / Nahawand low (fit 0.904)
- full report: `work/elissa-2000-wakherta-maak-07-ramchet-ayn/report.md`
