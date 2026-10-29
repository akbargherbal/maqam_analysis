# Maqam review — batch-020 (8 songs)

Read `skills/maqam-analysis/SKILL.md` before deciding. Hard rules:
- 12-TET ABC cannot prove quarter tones. Quarter-tone maqamat (Rast, Bayati, Saba, Sikah, Huzam, Iraq, Awj Ara, Suznek, Jiharkah, Bastanikar) are status `possible`, never `consistent`.
- If the analyzer says `name_allowed=false`, a scale is not identified, parse <95%, or pitch classes are too few: use `maqam_status="withheld"`.
- Confidence can be lowered, never raised above the tool's evidence.
- A tonic/dominant split must name the other tonic in `tonic_alternatives`.
- Never import outside knowledge of the song. Evidence is the ABC only.

Fill the sibling template, then run:
```bash
python3 scripts/review.py record --batch work/review/batch-020.json \
  --labels work/review/batch-020.labels.json
```

## 1. `fadl-shaker-15-the-best-of-al-rawae3-2010-03-allah-we-allam` — Fadl Shaker — 15.The Best Of (Al Rawae3).2010 — "الله واعلم"
- file: `03.Allah We'allam.mp3` | duration 261.698s | declared key Am | tempo 85.0 | voice Vocal
- parse: 100% of bars
- pitch classes: A 39%, B 35%, G 15%, C 7%, F 2%, D 1%
- tonic: G (low, margin 0.185) | cues: most-used note -> A; phrase endings -> G; tool key & chords* -> A (key) / F (commonest chord root); other voice -> E
- scale: (no standard maqam) [Mixolydian] (fit 0.94, shape confidence low, name_allowed=False) | tied: Rast, (no standard maqam) | 12-TET shadow of: Rast
- flags: same notes also fit other tonics: A (0.94), B (0.92), C (0.94)  -> relative-mode ambiguity | only 4 pitch classes in use: too few to identify a scale; the shape is under-determined
- sections:
  - Section: verse: A low / Nahawand medium (fit 0.96)  [!] same notes also fit other tonics: G (0.96), F (0.96)  -> relative-mode ambiguity
  - Section: chorus: A medium / Nahawand medium (fit 0.96)  [!] same notes also fit other tonics: B (0.95), G (0.96), C (0.96)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): G low / (no standard maqam) low (fit 0.94)
- full report: `work/fadl-shaker-15-the-best-of-al-rawae3-2010-03-allah-we-allam/report.md`
## 2. `fadl-shaker-15-the-best-of-al-rawae3-2010-04-ya-hyat-al-roh` — Fadl Shaker — 15.The Best Of (Al Rawae3).2010 — "يا حياة الروح"
- file: `04.Ya Hyat Al Roh.mp3` | duration 301.143s | declared key F#m | tempo 107.0 | voice Vocal
- parse: 100% of bars
- pitch classes: A 26%, C# 24%, B 24%, D 14%, G 5%, F# 4%
- tonic: F# (high, margin 0.249) | cues: most-used note -> A; phrase endings -> F#; tool key & chords* -> F# (key) / F# (commonest chord root); other voice -> F#
- scale: Kurd [Phrygian] (fit 1.0, shape confidence medium, name_allowed=True) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- candidate ghammaz: C# (700c, 43% of phrase endings)
- flags: same notes also fit other tonics: B (1.00), A (1.00)  -> relative-mode ambiguity
- sections:
  - Section: chorus: F# low / Kurd medium (fit 1.0)  [!] same notes also fit other tonics: B (1.00), A (1.00)  -> relative-mode ambiguity
  - Section: verse: F# low / Kurd medium (fit 0.96)  [!] same notes also fit other tonics: A (0.96), D (0.96), B (0.96)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): F# high / Kurd medium (fit 1.0)
- full report: `work/fadl-shaker-15-the-best-of-al-rawae3-2010-04-ya-hyat-al-roh/report.md`
## 3. `fadl-shaker-15-the-best-of-al-rawae3-2010-05-akhedny-ma-ak` — Fadl Shaker — 15.The Best Of (Al Rawae3).2010 — "اخدني معاك"
- file: `05.Akhedny Ma'ak.mp3` | duration 316.816s | declared key Gm | tempo 106.0 | voice Vocal
- parse: 100% of bars
- pitch classes: Bb 22%, G 21%, A 19%, D 15%, F 12%, C 8%
- tonic: D (low, margin 0.017) | cues: most-used note -> Bb; phrase endings -> D; tool key & chords* -> G (key) / D (commonest chord root); other voice -> D
- scale: Kurd [Phrygian] (fit 0.992, shape confidence medium, name_allowed=True) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- candidate ghammaz: G (500c, 14% of phrase endings)
- flags: tonic/dominant split: D and G (a 4th/5th apart) score almost equally; the true tonic could be either | same notes also fit other tonics: G (0.99), Bb (0.99), F (0.99)  -> relative-mode ambiguity
- sections:
  - Section: verse: G low / Nahawand medium (fit 0.991)  [!] tonic/dominant split: G and D (a 4th/5th apart) score almost equally; the true tonic could be either
  - Section: chorus: D low / Kurd medium (fit 0.98)  [!] same notes also fit other tonics: G (0.98), Bb (0.98)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): D low / Kurd medium (fit 0.992)
- full report: `work/fadl-shaker-15-the-best-of-al-rawae3-2010-05-akhedny-ma-ak/report.md`
## 4. `fadl-shaker-15-the-best-of-al-rawae3-2010-09-law-ala-albi` — Fadl Shaker — 15.The Best Of (Al Rawae3).2010 — "لو على قلبي"
- file: `09.Law Ala Albi.mp3` | duration 293.881s | declared key Dm | tempo 106.0 | voice Vocal
- parse: 100% of bars
- pitch classes: A 21%, G 19%, F 17%, E 15%, D 11%, C 8%
- tonic: A (low, margin 0.176) | cues: most-used note -> A; phrase endings -> A; tool key & chords* -> D (key) / D (commonest chord root); other voice -> D
- scale: Kurd [Phrygian] (fit 0.998, shape confidence medium, name_allowed=True) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- flags: same notes also fit other tonics: D (1.00), G (1.00), C (1.00)  -> relative-mode ambiguity
- sections:
  - Section: verse: A low / Hijaz medium (fit 0.98)  [!] same notes also fit other tonics: D (0.98), G (0.98)  -> relative-mode ambiguity
  - Section: chorus: D low / Nahawand medium (fit 1.0)  [!] tonic/dominant split: D and G (a 4th/5th apart) score almost equally; the true tonic could be either
- melody-only cross-check (chords removed): A low / Kurd medium (fit 0.998)
- full report: `work/fadl-shaker-15-the-best-of-al-rawae3-2010-09-law-ala-albi/report.md`
## 5. `fadl-shaker-15-the-best-of-al-rawae3-2010-10-el-am-el-gedeed` — Fadl Shaker — 15.The Best Of (Al Rawae3).2010 — "العام الجديد"
- file: `10.El'am El Gedeed.mp3` | duration 314.779s | declared key D#m | tempo 125.0 | voice Vocal
- parse: 100% of bars
- pitch classes: F# 20%, Bb 20%, Ab 16%, F 13%, Eb 10%, C# 10%
- tonic: Bb (low, margin 0.19) | cues: most-used note -> F#; phrase endings -> Bb; tool key & chords* -> Eb (key) / Bb (commonest chord root); other voice -> F
- scale: Kurd [Phrygian] (fit 0.997, shape confidence medium, name_allowed=True) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- candidate ghammaz: F (700c, 21% of phrase endings)
- flags: same notes also fit other tonics: Eb (1.00), Ab (1.00)  -> relative-mode ambiguity
- sections:
  - Section: verse: Bb low / Kurd medium (fit 0.996)  [!] same notes also fit other tonics: Eb (1.00), F# (1.00)  -> relative-mode ambiguity
  - Section: chorus: Bb low / Kurd medium (fit 1.0)  [!] same notes also fit other tonics: Eb (1.00), Ab (1.00), C# (1.00)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): Bb low / Kurd medium (fit 0.997)
- full report: `work/fadl-shaker-15-the-best-of-al-rawae3-2010-10-el-am-el-gedeed/report.md`
## 6. `fadl-shaker-15-the-best-of-al-rawae3-2010-11-ma-oul` — Fadl Shaker — 15.The Best Of (Al Rawae3).2010 — "معقول"
- file: `11.Ma'oul.mp3` | duration 238.815s | declared key G#m | tempo 104.0 | voice Vocal
- parse: 100% of bars
- pitch classes: Ab 28%, Bb 26%, F# 16%, B 14%, C# 5%, E 5%
- tonic: F# (low, margin 0.177) | cues: most-used note -> Ab; phrase endings -> F#; tool key & chords* -> Ab (key) / Ab (commonest chord root); other voice -> Ab
- scale: (no standard maqam) [Mixolydian] (fit 0.987, shape confidence medium, name_allowed=True) | tied: Rast, (no standard maqam) | 12-TET shadow of: Rast
- candidate ghammaz: Bb (400c, 25% of phrase endings)
- flags: same notes also fit other tonics: Ab (0.99), Eb (0.99)  -> relative-mode ambiguity
- sections:
  - Section: verse: Ab low / Nahawand medium (fit 0.984)  [!] same notes also fit other tonics: F# (0.98), Eb (0.98)  -> relative-mode ambiguity
  - Section: chorus: F# low / (no standard maqam) medium (fit 1.0)  [!] same notes also fit other tonics: Ab (1.00), E (1.00), B (1.00)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): F# low / (no standard maqam) medium (fit 0.987)
- full report: `work/fadl-shaker-15-the-best-of-al-rawae3-2010-11-ma-oul/report.md`
## 7. `fadl-shaker-15-the-best-of-al-rawae3-2010-12-dehket-el-donya` — Fadl Shaker — 15.The Best Of (Al Rawae3).2010 — "ضحكت الدنيا"
- file: `12.Dehket El Donya.mp3` | duration 257.78s | declared key Cm | tempo 145.0 | voice Vocal
- parse: 100% of bars
- pitch classes: C 28%, D 25%, Bb 16%, Eb 12%, Ab 8%, G 7%
- tonic: D (low, margin 0.177) | cues: most-used note -> C; phrase endings -> D; tool key & chords* -> C (key) / G (commonest chord root); other voice -> G
- scale: Kurd [Phrygian] (fit 0.847, shape confidence low, name_allowed=False) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- candidate ghammaz: Bb (800c, 17% of phrase endings)
- flags: same notes also fit other tonics: C (1.00), Bb (1.00), Eb (1.00)  -> relative-mode ambiguity | no single scale explains this material (best fit 0.85); expect modulation, chromatic writing or quarter tones; do not name one maqam
- sections:
  - Section: verse: Bb low / (no standard maqam) medium (fit 1.0)  [!] same notes also fit other tonics: C (1.00), Eb (1.00)  -> relative-mode ambiguity
  - Section: chorus: D low / Kurd low (fit 0.777)  [!] same notes also fit other tonics: C (1.00), Bb (1.00), G (1.00)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): D low / Kurd low (fit 0.847)
- full report: `work/fadl-shaker-15-the-best-of-al-rawae3-2010-12-dehket-el-donya/report.md`
## 8. `fadl-shaker-15-the-best-of-al-rawae3-2010-13-ya-ghayib` — Fadl Shaker — 15.The Best Of (Al Rawae3).2010 — "يا غايب"
- file: `13.Ya Ghayib.mp3` | duration 233.251s | declared key Cm | tempo 107.0 | voice Vocal
- parse: 100% of bars
- pitch classes: C 29%, D 21%, G 14%, Eb 13%, F 10%, Bb 9%
- tonic: C (low, margin 0.132) | cues: most-used note -> C; phrase endings -> Bb; tool key & chords* -> C (key) / F (commonest chord root); other voice -> G
- scale: Nahawand [natural minor / Aeolian] (fit 1.0, shape confidence medium, name_allowed=True) | tied: Bayati, Nahawand | 12-TET shadow of: Bayati
- candidate ghammaz: Bb (1000c, 50% of phrase endings)
- flags: same notes also fit other tonics: Bb (1.00), Eb (1.00)  -> relative-mode ambiguity
- sections:
  - Section: verse: Eb low / Ajam medium (fit 0.98)  [!] tonic/dominant split: Eb and Ab (a 4th/5th apart) score almost equally; the true tonic could be either
  - Section: chorus: C low / Nahawand medium (fit 1.0)  [!] tonic/dominant split: C and G (a 4th/5th apart) score almost equally; the true tonic could be either
- melody-only cross-check (chords removed): C low / Nahawand medium (fit 1.0)
- full report: `work/fadl-shaker-15-the-best-of-al-rawae3-2010-13-ya-ghayib/report.md`
