# Maqam review — batch-018 (8 songs)

Read `skills/maqam-analysis/SKILL.md` before deciding. Hard rules:
- 12-TET ABC cannot prove quarter tones. Quarter-tone maqamat (Rast, Bayati, Saba, Sikah, Huzam, Iraq, Awj Ara, Suznek, Jiharkah, Bastanikar) are status `possible`, never `consistent`.
- If the analyzer says `name_allowed=false`, a scale is not identified, parse <95%, or pitch classes are too few: use `maqam_status="withheld"`.
- Confidence can be lowered, never raised above the tool's evidence.
- A tonic/dominant split must name the other tonic in `tonic_alternatives`.
- Never import outside knowledge of the song. Evidence is the ABC only.

Fill the sibling template, then run:
```bash
python3 scripts/review.py record --batch work/review/batch-018.json \
  --labels work/review/batch-018.labels.json
```

## 1. `fadl-shaker-12-allah-alam-2006-08-kent-mfakkar` — Fadl Shaker — 12.Allah Alam.2006 — "كنت مفكر"
- file: `08.Kent Mfakkar.mp3` | duration 279.066s | declared key Am | tempo 87.0 | voice Vocal
- parse: 100% of bars
- pitch classes: A 29%, B 21%, C 16%, G 14%, D 10%, F 5%
- tonic: A (medium, margin 0.028) | cues: most-used note -> A; phrase endings -> C; tool key & chords* -> A (key) / A (commonest chord root); other voice -> A
- scale: Nahawand [natural minor / Aeolian] (fit 1.0, shape confidence medium, name_allowed=True) | tied: Bayati, Nahawand | 12-TET shadow of: Bayati
- candidate ghammaz: C (300c, 29% of phrase endings)
- flags: same notes also fit other tonics: C (1.00), E (1.00), F (1.00)  -> relative-mode ambiguity
- sections:
  - Section: verse: E low / Kurd medium (fit 0.98)  [!] same notes also fit other tonics: F (0.98), G (0.98), A (0.98)  -> relative-mode ambiguity
  - Section: chorus: C low / Ajam medium (fit 1.0)  [!] same notes also fit other tonics: A (1.00), G (1.00), D (1.00)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): A medium / Nahawand medium (fit 1.0)
- full report: `work/fadl-shaker-12-allah-alam-2006-08-kent-mfakkar/report.md`
## 2. `fadl-shaker-12-allah-alam-2006-09-bousni-wo-salehni` — Fadl Shaker — 12.Allah Alam.2006 — "بوسني وصالحني"
- file: `09.Bousni Wo Salehni.mp3` | duration 272.248s | declared key Bm | tempo 85.0 | voice Vocal
- parse: 100% of bars
- pitch classes: A 36%, B 32%, C# 16%, G 10%, F# 4%, E 2%
- tonic: B (low, margin 0.211) | cues: most-used note -> A; phrase endings -> G; tool key & chords* -> B (key) / B (commonest chord root); other voice -> B
- scale: Nahawand [natural minor / Aeolian] (fit 0.96, shape confidence medium, name_allowed=True) | tied: Bayati, Nahawand | 12-TET shadow of: Bayati
- candidate ghammaz: G (800c, 73% of phrase endings)
- flags: same notes also fit other tonics: G (0.96), F# (0.96), A (0.96)  -> relative-mode ambiguity
- sections:
  - Section: verse: B low / Nahawand medium (fit 0.98)  [!] same notes also fit other tonics: A (0.98), G (0.98), F# (0.98)  -> relative-mode ambiguity
  - Section: chorus: B low / Nahawand low (fit 0.94)  [!] same notes also fit other tonics: G (0.94), F# (0.94), A (0.94)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): B low / Nahawand medium (fit 0.96)
- full report: `work/fadl-shaker-12-allah-alam-2006-09-bousni-wo-salehni/report.md`
## 3. `fadl-shaker-12-allah-alam-2006-10-embareh-belleil` — Fadl Shaker — 12.Allah Alam.2006 — "امبارح بالليل"
- file: `10.Embareh Belleil.mp3` | duration 273.502s | declared key Am | tempo 109.0 | voice Vocal
- parse: 100% of bars
- pitch classes: B 26%, A 21%, C 16%, G 14%, D 12%, E 6%
- tonic: A (low, margin 0.056) | cues: most-used note -> B; phrase endings -> G; tool key & chords* -> A (key) / E (commonest chord root); other voice -> E
- scale: Nahawand [natural minor / Aeolian] (fit 0.99, shape confidence medium, name_allowed=True) | tied: Bayati, Nahawand | 12-TET shadow of: Bayati
- candidate ghammaz: E (700c, 18% of phrase endings)
- flags: same notes also fit other tonics: G (0.99), E (0.99)  -> relative-mode ambiguity
- sections:
  - Section: verse: A low / Nahawand medium (fit 0.99)  [!] same notes also fit other tonics: G (0.99), E (0.99)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): A low / Nahawand medium (fit 0.99)
- full report: `work/fadl-shaker-12-allah-alam-2006-10-embareh-belleil/report.md`
## 4. `fadl-shaker-12-allah-alam-2006-11-waddaatak` — Fadl Shaker — 12.Allah Alam.2006 — "ودعتك"
- file: `11.Waddaatak.mp3` | duration 281.339s | declared key Dm | tempo 94.0 | voice Vocal
- parse: 100% of bars
- pitch classes: A 25%, C 20%, Bb 20%, D 18%, E 7%, G 6%
- tonic: D (low, margin 0.039) | cues: most-used note -> A; phrase endings -> C; tool key & chords* -> D (key) / D (commonest chord root); other voice -> A
- scale: Nahawand [natural minor / Aeolian] (fit 1.0, shape confidence medium, name_allowed=True) | tied: Bayati, Nahawand | 12-TET shadow of: Bayati
- candidate ghammaz: C (1000c, 40% of phrase endings)
- flags: same notes also fit other tonics: C (1.00), A (1.00), Bb (1.00)  -> relative-mode ambiguity
- sections:
  - Section: verse: D low / Nahawand medium (fit 1.0)  [!] same notes also fit other tonics: C (1.00), A (1.00), Bb (1.00)  -> relative-mode ambiguity
  - Section: chorus: A medium / Kurd medium (fit 0.98)  [!] same notes also fit other tonics: D (0.98), Bb (0.98), C (0.98)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): D low / Nahawand medium (fit 1.0)
- full report: `work/fadl-shaker-12-allah-alam-2006-11-waddaatak/report.md`
## 5. `fadl-shaker-12-allah-alam-2006-12-akhedne-maak` — Fadl Shaker — 12.Allah Alam.2006 — "اخدني معاك"
- file: `12.Akhedne Maak.mp3` | duration 313.94s | declared key Em | tempo 92.0 | voice Vocal
- parse: 100% of bars
- pitch classes: B 23%, A 23%, G 21%, C 12%, F# 9%, E 6%
- tonic: E (low, margin 0.004) | cues: most-used note -> B; phrase endings -> B; tool key & chords* -> E (key) / E (commonest chord root); other voice -> G
- scale: Nahawand [natural minor / Aeolian] (fit 1.0, shape confidence medium, name_allowed=True) | tied: Bayati, Nahawand | 12-TET shadow of: Bayati
- candidate ghammaz: B (700c, 24% of phrase endings)
- flags: tonic/dominant split: E and B (a 4th/5th apart) score almost equally; the true tonic could be either | same notes also fit other tonics: B (1.00), G (1.00), A (1.00)  -> relative-mode ambiguity
- sections:
  - Section: verse: E high / Nahawand medium (fit 1.0)  [!] same notes also fit other tonics: C (1.00), D (1.00), G (1.00)  -> relative-mode ambiguity
  - Section: chorus: B low / Kurd medium (fit 0.96)  [!] same notes also fit other tonics: G (0.96), C (0.96)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): B low / Kurd medium (fit 1.0)
- full report: `work/fadl-shaker-12-allah-alam-2006-12-akhedne-maak/report.md`
## 6. `fadl-shaker-13-ya-mesaharny-el-lail-2007-01-ya-mesaharny-el-lail` — Fadl Shaker — 13.Ya Mesaharny El Lail.2007 — "يا مسهرني الليل"
- file: `01.Ya Mesaharny El Lail.mp3` | duration 246.207s | declared key G#m | tempo 90.0 | voice Vocal
- parse: 100% of bars
- pitch classes: Ab 25%, B 22%, Bb 19%, C# 15%, F# 6%, E 6%
- tonic: Ab (high, margin 0.275) | cues: most-used note -> Ab; phrase endings -> Bb; tool key & chords* -> Ab (key) / Ab (commonest chord root); other voice -> Ab
- scale: Nahawand [natural minor / Aeolian] (fit 0.912, shape confidence low, name_allowed=True) | tied: Bayati, Nahawand | 12-TET shadow of: Bayati
- candidate ghammaz: E (800c, 11% of phrase endings)
- flags: same notes also fit other tonics: B (0.91), C# (0.91)  -> relative-mode ambiguity
- sections:
  - Section: verse: Ab low / Nahawand low (fit 0.862)  [!] same notes also fit other tonics: B (0.86), E (0.86)  -> relative-mode ambiguity
  - Section: chorus: Ab high / Nahawand medium (fit 1.0)  [!] same notes also fit other tonics: C# (1.00), B (1.00)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): Ab high / Nahawand low (fit 0.912)
- full report: `work/fadl-shaker-13-ya-mesaharny-el-lail-2007-01-ya-mesaharny-el-lail/report.md`
## 7. `fadl-shaker-14-bada-aalbal-2009-01-faker-lamma-te-ouly` — Fadl Shaker — 14.Ba’da Aalbal.2009 — "فاكر لما تقولي"
- file: `01.Faker Lamma Te'ouly.mp3` | duration 302.109s | declared key Gm | tempo 98.0 | voice Vocal
- parse: 100% of bars
- pitch classes: Bb 28%, C 25%, Ab 19%, G 18%, D 5%, Eb 3%
- tonic: G (low, margin 0.201) | cues: most-used note -> Bb; phrase endings -> Ab; tool key & chords* -> G (key) / Ab (commonest chord root); other voice -> G
- scale: Kurd [Phrygian] (fit 0.98, shape confidence medium, name_allowed=True) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- candidate ghammaz: Bb (300c, 19% of phrase endings)
- flags: same notes also fit other tonics: Ab (0.98), C (0.98), Bb (0.98)  -> relative-mode ambiguity
- sections:
  - Section: verse: Ab low / (no standard maqam) medium (fit 1.0)  [!] same notes also fit other tonics: G (1.00), Bb (1.00), C (1.00)  -> relative-mode ambiguity
  - Section: chorus: G low / Kurd medium (fit 0.96)  [!] same notes also fit other tonics: C (0.96), Bb (0.96), Ab (0.96)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): G low / Kurd medium (fit 0.98)
- full report: `work/fadl-shaker-14-bada-aalbal-2009-01-faker-lamma-te-ouly/report.md`
## 8. `fadl-shaker-14-bada-aalbal-2009-02-hakhally-baly` — Fadl Shaker — 14.Ba’da Aalbal.2009 — "هخلي بالي"
- file: `02.Hakhally Baly.mp3` | duration 345.133s | declared key Gm | tempo 73.0 | voice Vocal
- parse: 100% of bars
- pitch classes: Bb 21%, D 18%, G 18%, A 17%, F 13%, C 10%
- tonic: G (high, margin 0.134) | cues: most-used note -> Bb; phrase endings -> G; tool key & chords* -> G (key) / Eb (commonest chord root); other voice -> G
- scale: Nahawand [natural minor / Aeolian] (fit 1.0, shape confidence medium, name_allowed=True) | tied: Bayati, Nahawand | 12-TET shadow of: Bayati
- candidate ghammaz: D (700c, 33% of phrase endings)
- flags: same notes also fit other tonics: F (1.00), D (1.00), Bb (1.00)  -> relative-mode ambiguity
- sections:
  - Section: verse: F low / (no standard maqam) medium (fit 0.98)  [!] same notes also fit other tonics: C (0.98), G (0.98), Eb (0.98)  -> relative-mode ambiguity
  - Section: chorus: G high / Nahawand medium (fit 1.0)  [!] same notes also fit other tonics: D (1.00), Bb (1.00), C (1.00)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): G high / Nahawand medium (fit 1.0)
- full report: `work/fadl-shaker-14-bada-aalbal-2009-02-hakhally-baly/report.md`
