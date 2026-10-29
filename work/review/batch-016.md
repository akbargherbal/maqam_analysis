# Maqam review — batch-016 (8 songs)

Read `skills/maqam-analysis/SKILL.md` before deciding. Hard rules:
- 12-TET ABC cannot prove quarter tones. Quarter-tone maqamat (Rast, Bayati, Saba, Sikah, Huzam, Iraq, Awj Ara, Suznek, Jiharkah, Bastanikar) are status `possible`, never `consistent`.
- If the analyzer says `name_allowed=false`, a scale is not identified, parse <95%, or pitch classes are too few: use `maqam_status="withheld"`.
- Confidence can be lowered, never raised above the tool's evidence.
- A tonic/dominant split must name the other tonic in `tonic_alternatives`.
- Never import outside knowledge of the song. Evidence is the ABC only.

Fill the sibling template, then run:
```bash
python3 scripts/review.py record --batch work/review/batch-016.json \
  --labels work/review/batch-016.labels.json
```

## 1. `fadl-shaker-08-hafla-2004-08-dehkat-al-donya` — Fadl Shaker — 08.Hafla 2004 — "ضحكت الدنيا"
- file: `08.Dehkat Al Donya.mp3` | duration 259.579s | declared key Cm | tempo 145.0 | voice Vocal
- parse: 100% of bars
- pitch classes: C 28%, D 23%, Bb 18%, Eb 11%, Ab 9%, G 7%
- tonic: D (low, margin 0.01) | cues: most-used note -> C; phrase endings -> D; tool key & chords* -> C (key) / G (commonest chord root); other voice -> G
- scale: Kurd [Phrygian] (fit 0.837, shape confidence low, name_allowed=False) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- candidate ghammaz: Bb (800c, 40% of phrase endings)
- flags: same notes also fit other tonics: C (1.00), Bb (1.00), G (1.00)  -> relative-mode ambiguity | no single scale explains this material (best fit 0.84); expect modulation, chromatic writing or quarter tones; do not name one maqam
- sections:
  - Section: verse: Bb low / (no standard maqam) medium (fit 0.997)  [!] same notes also fit other tonics: C (1.00), Eb (1.00)  -> relative-mode ambiguity
  - Section: chorus: D low / Kurd low (fit 0.77)  [!] same notes also fit other tonics: Bb (1.00), C (1.00), G (1.00)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): D low / Kurd low (fit 0.837)
- full report: `work/fadl-shaker-08-hafla-2004-08-dehkat-al-donya/report.md`
## 2. `fadl-shaker-08-hafla-2004-10-baya-a-al-qoloub` — Fadl Shaker — 08.Hafla 2004 — "بياع القلوب"
- file: `10.Baya'a Al Qoloub.mp3` | duration 263.184s | declared key Cm | tempo 94.0 | voice Vocal
- parse: 100% of bars
- pitch classes: Bb 38%, C 18%, Ab 18%, G 13%, D 9%, F 2%
- tonic: C (low, margin 0.132) | cues: most-used note -> Bb; phrase endings -> G; tool key & chords* -> C (key) / C (commonest chord root); other voice -> G
- scale: Nahawand [natural minor / Aeolian] (fit 0.98, shape confidence medium, name_allowed=True) | tied: Bayati, Nahawand | 12-TET shadow of: Bayati
- candidate ghammaz: Bb (1000c, 32% of phrase endings)
- flags: same notes also fit other tonics: G (0.98), Bb (0.98), Ab (0.98)  -> relative-mode ambiguity
- sections:
  - Section: verse: C low / Nahawand medium (fit 0.98)  [!] same notes also fit other tonics: Bb (0.98), G (0.98), Ab (0.98)  -> relative-mode ambiguity
  - Section: chorus: C low / Nahawand medium (fit 0.96)  [!] tonic/dominant split: C and G (a 4th/5th apart) score almost equally; the true tonic could be either
- melody-only cross-check (chords removed): C low / Nahawand medium (fit 0.98)
- full report: `work/fadl-shaker-08-hafla-2004-10-baya-a-al-qoloub/report.md`
## 3. `fadl-shaker-09-arabian-night-2004-09-tayer-ya-hawa` — Fadl Shaker — 09.Arabian Night.2004 — "طاير يا هوى"
- file: `09.Tayer Ya Hawa.mp3` | duration 291.634s | declared key Bm | tempo 75.0 | voice Vocal
- parse: 100% of bars
- pitch classes: E 19%, D 19%, A 17%, B 17%, G 14%, C 7%
- tonic: B (low, margin 0.113) | cues: most-used note -> E; phrase endings -> D; tool key & chords* -> B (key) / B (commonest chord root); other voice -> B
- scale: Kurd [Phrygian] (fit 1.0, shape confidence medium, name_allowed=True) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- candidate ghammaz: D (300c, 52% of phrase endings)
- flags: same notes also fit other tonics: D (1.00), E (1.00), G (1.00)  -> relative-mode ambiguity
- sections:
  - Section: verse: B low / Kurd medium (fit 1.0)  [!] same notes also fit other tonics: D (1.00), E (1.00), A (1.00)  -> relative-mode ambiguity
  - Section: chorus: B medium / Kurd medium (fit 1.0)  [!] same notes also fit other tonics: D (1.00), G (1.00), E (1.00)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): B low / Kurd medium (fit 1.0)
- full report: `work/fadl-shaker-09-arabian-night-2004-09-tayer-ya-hawa/report.md`
## 4. `fadl-shaker-10-saharni-el-shoq-2005-02-gowwaya` — Fadl Shaker — 10.Saharni El Shoq.2005 — "جوايا"
- file: `02.Gowwaya.mp3` | duration 284.238s | declared key Bbm | tempo 133.0 | voice Vocal
- parse: 100% of bars
- pitch classes: C# 26%, C 24%, Bb 20%, Eb 12%, F 8%, Ab 6%
- tonic: Bb (low, margin 0.296) | cues: most-used note -> C#; phrase endings -> Bb; tool key & chords* -> Bb (key) / F (commonest chord root); other voice -> F
- scale: Nahawand [natural minor / Aeolian] (fit 0.99, shape confidence medium, name_allowed=True) | tied: Bayati, Nahawand | 12-TET shadow of: Bayati
- flags: same notes also fit other tonics: F (0.99), C# (0.99)  -> relative-mode ambiguity
- sections:
  - Section: verse: Bb low / Nahawand medium (fit 0.96)  [!] same notes also fit other tonics: C (0.96), F (0.96), Eb (0.96)  -> relative-mode ambiguity
  - Section: chorus: Bb medium / Nahawand medium (fit 0.987)  [!] same notes also fit other tonics: F (0.99), C# (0.99)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): Bb low / Nahawand medium (fit 0.99)
- full report: `work/fadl-shaker-10-saharni-el-shoq-2005-02-gowwaya/report.md`
## 5. `fadl-shaker-10-saharni-el-shoq-2005-11-el-hal` — Fadl Shaker — 10.Saharni El Shoq.2005 — "الحال"
- file: `11.El-Hal.mp3` | duration 246.622s | declared key Gm | tempo 90.0 | voice Vocal
- parse: 100% of bars
- pitch classes: D 33%, A 22%, C 20%, Bb 19%, F 3%, Eb 2%
- tonic: D (high, margin 0.66) | cues: most-used note -> D; phrase endings -> D; tool key & chords* -> G (key) / G (commonest chord root); other voice -> D
- scale: Kurd [Phrygian] (fit 0.96, shape confidence medium, name_allowed=True) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- flags: same notes also fit other tonics: A (0.94), Bb (0.96), F (0.96)  -> relative-mode ambiguity
- sections:
  - Section: verse: D low / Kurd medium (fit 0.96)  [!] same notes also fit other tonics: A (0.95), Bb (0.96), F (0.96)  -> relative-mode ambiguity
  - Section: chorus: D low / Kurd medium (fit 0.98)  [!] same notes also fit other tonics: Bb (0.98), F (0.98)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): D high / Kurd medium (fit 0.96)
- full report: `work/fadl-shaker-10-saharni-el-shoq-2005-11-el-hal/report.md`
## 6. `fadl-shaker-10-saharni-el-shoq-2005-12-fein-layalik` — Fadl Shaker — 10.Saharni El Shoq.2005 — "فين لياليك"
- file: `12.Fein Layalik.mp3` | duration 282.175s | declared key Gm | tempo 96.0 | voice Vocal
- parse: 100% of bars
- pitch classes: A 26%, Bb 25%, C 16%, G 16%, D 11%, F 5%
- tonic: A (low, margin 0.021) | cues: most-used note -> A; phrase endings -> D; tool key & chords* -> G (key) / F (commonest chord root); other voice -> D
- scale: Kurd [Phrygian] (fit 0.966, shape confidence medium, name_allowed=True) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- candidate ghammaz: D (500c, 33% of phrase endings)
- flags: same notes also fit other tonics: Bb (0.98), D (0.98), G (0.98)  -> relative-mode ambiguity
- sections:
  - Section: verse: D low / Nahawand medium (fit 0.98)  [!] same notes also fit other tonics: G (0.98), Bb (0.98), A (0.98)  -> relative-mode ambiguity
  - Section: chorus: A low / Kurd medium (fit 0.96)  [!] same notes also fit other tonics: Bb (0.98), G (0.98), C (0.98)  -> relative-mode ambiguity
  - Section: bridge: D low / Nahawand medium (fit 0.98)  [!] same notes also fit other tonics: G (0.98), Bb (0.98), A (0.98)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): A low / Kurd medium (fit 0.966)
- full report: `work/fadl-shaker-10-saharni-el-shoq-2005-12-fein-layalik/report.md`
## 7. `fadl-shaker-10-saharni-el-shoq-2005-13-ya-hayat-el-roh` — Fadl Shaker — 10.Saharni El Shoq.2005 — "يا حياة الروح"
- file: `13.Ya Hayat El-Roh.mp3` | duration 300.957s | declared key F#m | tempo 107.0 | voice Vocal
- parse: 100% of bars
- pitch classes: A 27%, C# 25%, B 23%, D 13%, G 6%, F# 4%
- tonic: F# (high, margin 0.236) | cues: most-used note -> A; phrase endings -> F#; tool key & chords* -> F# (key) / F# (commonest chord root); other voice -> F#
- scale: Kurd [Phrygian] (fit 1.0, shape confidence medium, name_allowed=True) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- candidate ghammaz: C# (700c, 38% of phrase endings)
- flags: same notes also fit other tonics: B (1.00), A (1.00)  -> relative-mode ambiguity
- sections:
  - Section: chorus: F# low / Kurd medium (fit 1.0)  [!] same notes also fit other tonics: B (1.00), A (1.00)  -> relative-mode ambiguity
  - Section: verse: F# low / Kurd medium (fit 0.96)  [!] same notes also fit other tonics: A (0.96), D (0.96), B (0.96)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): F# high / Kurd medium (fit 1.0)
- full report: `work/fadl-shaker-10-saharni-el-shoq-2005-13-ya-hayat-el-roh/report.md`
## 8. `fadl-shaker-10-saharni-el-shoq-2005-14-meen-allak` — Fadl Shaker — 10.Saharni El Shoq.2005 — "مين قالك"
- file: `14.Meen Allak.mp3` | duration 269.61s | declared key Gm | tempo 75.0 | voice Vocal
- parse: 100% of bars
- pitch classes: D 21%, G 19%, F 14%, C 12%, A 12%, Eb 11%
- tonic: G (low, margin 0.135) | cues: most-used note -> D; phrase endings -> G; tool key & chords* -> G (key) / D (commonest chord root); other voice -> A
- scale: Nahawand [natural minor / Aeolian] (fit 1.0, shape confidence medium, name_allowed=True) | tied: Bayati, Nahawand | 12-TET shadow of: Bayati
- candidate ghammaz: D (700c, 14% of phrase endings)
- flags: same notes also fit other tonics: D (1.00), Eb (1.00)  -> relative-mode ambiguity
- sections:
  - Section: verse: G high / Nahawand medium (fit 0.98)  [!] same notes also fit other tonics: A (0.98), F (0.98), Bb (0.98)  -> relative-mode ambiguity
  - Section: chorus: D low / Kurd medium (fit 0.98)  [!] tonic/dominant split: D and A (a 4th/5th apart) score almost equally; the true tonic could be either
- melody-only cross-check (chords removed): G low / Nahawand medium (fit 1.0)
- full report: `work/fadl-shaker-10-saharni-el-shoq-2005-14-meen-allak/report.md`
