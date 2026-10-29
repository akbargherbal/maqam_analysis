# Maqam review — batch-019 (8 songs)

Read `skills/maqam-analysis/SKILL.md` before deciding. Hard rules:
- 12-TET ABC cannot prove quarter tones. Quarter-tone maqamat (Rast, Bayati, Saba, Sikah, Huzam, Iraq, Awj Ara, Suznek, Jiharkah, Bastanikar) are status `possible`, never `consistent`.
- If the analyzer says `name_allowed=false`, a scale is not identified, parse <95%, or pitch classes are too few: use `maqam_status="withheld"`.
- Confidence can be lowered, never raised above the tool's evidence.
- A tonic/dominant split must name the other tonic in `tonic_alternatives`.
- Never import outside knowledge of the song. Evidence is the ABC only.

Fill the sibling template, then run:
```bash
python3 scripts/review.py record --batch work/review/batch-019.json \
  --labels work/review/batch-019.labels.json
```

## 1. `fadl-shaker-14-bada-aalbal-2009-04-bafakkar-bel-sa-at` — Fadl Shaker — 14.Ba’da Aalbal.2009 — "بفكر بالساعات"
- file: `04.Bafakkar Bel Sa'at.mp3` | duration 299.131s | declared key Cm | tempo 82.0 | voice Vocal
- parse: 100% of bars
- pitch classes: D 23%, G 22%, Bb 20%, C 18%, F 8%, B 5%
- tonic: G (low, margin 0.06) | cues: most-used note -> D; phrase endings -> D; tool key & chords* -> C (key) / C (commonest chord root); other voice -> G
- scale: Kurd [Phrygian] (fit 0.883, shape confidence low, name_allowed=False) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- candidate ghammaz: F (1000c, 28% of phrase endings)
- flags: tonic/dominant split: G and C (a 4th/5th apart) score almost equally; the true tonic could be either | same notes also fit other tonics: C (0.88), F (0.88)  -> relative-mode ambiguity | no single scale explains this material (best fit 0.88); expect modulation, chromatic writing or quarter tones; do not name one maqam
- sections:
  - Section: verse: G low / Kurd low (fit 0.853)  [!] same notes also fit other tonics: F (0.85), C (0.85)  -> relative-mode ambiguity
  - Section: chorus: G low / Kurd medium (fit 0.96)  [!] same notes also fit other tonics: C (0.96), D (0.94), Bb (0.96)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): G low / Kurd low (fit 0.883)
- full report: `work/fadl-shaker-14-bada-aalbal-2009-04-bafakkar-bel-sa-at/report.md`
## 2. `fadl-shaker-14-bada-aalbal-2009-05-men-akherha` — Fadl Shaker — 14.Ba’da Aalbal.2009 — "من اخرها"
- file: `05.Men Akherha.mp3` | duration 248.114s | declared key Em | tempo 125.0 | voice Vocal
- parse: 100% of bars
- pitch classes: A 31%, B 29%, G 14%, F 7%, C 7%, E 6%
- tonic: E (low, margin 0.169) | cues: most-used note -> A; phrase endings -> A; tool key & chords* -> E (key) / E (commonest chord root); other voice -> E
- scale: Kurd [Phrygian] (fit 1.0, shape confidence medium, name_allowed=True) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- candidate ghammaz: A (500c, 38% of phrase endings)
- flags: same notes also fit other tonics: A (1.00), F (1.00), D (1.00)  -> relative-mode ambiguity
- sections:
  - Section: verse: E high / Kurd medium (fit 1.0)  [!] same notes also fit other tonics: G (1.00), A (1.00)  -> relative-mode ambiguity
  - Section: chorus: F low / (no standard maqam) medium (fit 0.98)  [!] same notes also fit other tonics: D (0.98), A (0.98), C (0.98)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): E low / Kurd medium (fit 1.0)
- full report: `work/fadl-shaker-14-bada-aalbal-2009-05-men-akherha/report.md`
## 3. `fadl-shaker-14-bada-aalbal-2009-06-ba-da-aal-baal` — Fadl Shaker — 14.Ba’da Aalbal.2009 — "بعدا عالبال"
- file: `06.Ba'da Aal Baal.mp3` | duration 251.118s | declared key Cm | tempo 135.0 | voice Vocal
- parse: 100% of bars
- pitch classes: C 24%, D 21%, G 17%, B 11%, Ab 10%, F 8%
- tonic: G (low, margin 0.127) | cues: most-used note -> C; phrase endings -> G; tool key & chords* -> C (key) / G (commonest chord root); other voice -> G
- scale: Hijaz (fit 0.981, shape confidence medium, name_allowed=True) | tied: Hijaz
- candidate ghammaz: D (700c, 44% of phrase endings)
- flags: same notes also fit other tonics: C (0.98)  -> relative-mode ambiguity
- sections:
  - Section: verse: D low / Kurd low (fit 0.821)  [!] same notes also fit other tonics: G (0.98), C (0.98), Ab (0.98)  -> relative-mode ambiguity
  - Section: chorus: G low / Hijaz medium (fit 0.96)  [!] same notes also fit other tonics: C (0.96)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): G low / Hijaz medium (fit 0.981)
- full report: `work/fadl-shaker-14-bada-aalbal-2009-06-ba-da-aal-baal/report.md`
## 4. `fadl-shaker-14-bada-aalbal-2009-07-nesseit-ansak` — Fadl Shaker — 14.Ba’da Aalbal.2009 — "نسيت انساك"
- file: `07.Nesseit Ansak.mp3` | duration 293.097s | declared key Cm | tempo 61.0 | voice Vocal
- parse: 100% of bars
- pitch classes: Bb 28%, Ab 19%, C 17%, D 14%, G 12%, Eb 7%
- tonic: C (low, margin 0.029) | cues: most-used note -> Bb; phrase endings -> G; tool key & chords* -> C (key) / G (commonest chord root); other voice -> Bb
- scale: Nahawand [natural minor / Aeolian] (fit 0.974, shape confidence medium, name_allowed=True) | tied: Bayati, Nahawand | 12-TET shadow of: Bayati
- candidate ghammaz: Bb (1000c, 26% of phrase endings)
- flags: tonic/dominant split: C and G (a 4th/5th apart) score almost equally; the true tonic could be either | same notes also fit other tonics: G (0.97), Ab (0.97), Bb (0.97)  -> relative-mode ambiguity
- sections:
  - Section: verse: C low / Nahawand medium (fit 0.968)  [!] tonic/dominant split: C and G (a 4th/5th apart) score almost equally; the true tonic could be either
  - Section: chorus: C low / Nahawand medium (fit 0.98)  [!] same notes also fit other tonics: Bb (0.98), G (0.98), Ab (0.98)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): C low / Nahawand medium (fit 0.974)
- full report: `work/fadl-shaker-14-bada-aalbal-2009-07-nesseit-ansak/report.md`
## 5. `fadl-shaker-14-bada-aalbal-2009-08-we-eftara-na` — Fadl Shaker — 14.Ba’da Aalbal.2009 — "وإفترقنا"
- file: `08.We Eftara'na.mp3` | duration 314.1s | declared key Bm | tempo 90.0 | voice Vocal
- parse: 100% of bars
- pitch classes: B 26%, A 19%, C# 16%, F# 13%, G 12%, D 6%
- tonic: B (low, margin 0.01) | cues: most-used note -> B; phrase endings -> F#; tool key & chords* -> B (key) / F# (commonest chord root); other voice -> F#
- scale: Nahawand [natural minor / Aeolian] (fit 0.918, shape confidence low, name_allowed=True) | tied: Bayati, Nahawand | 12-TET shadow of: Bayati
- candidate ghammaz: F# (700c, 38% of phrase endings)
- flags: tonic/dominant split: B and F# (a 4th/5th apart) score almost equally; the true tonic could be either | same notes also fit other tonics: F# (0.92), G (0.92)  -> relative-mode ambiguity
- sections:
  - Section: verse: B low / Nahawand low (fit 0.906)  [!] tonic/dominant split: B and F# (a 4th/5th apart) score almost equally; the true tonic could be either
  - Section: chorus: B low / Nahawand medium (fit 0.974)  [!] same notes also fit other tonics: G (0.97), F# (0.97)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): B low / Nahawand low (fit 0.918)
- full report: `work/fadl-shaker-14-bada-aalbal-2009-08-we-eftara-na/report.md`
## 6. `fadl-shaker-14-bada-aalbal-2009-09-rouh` — Fadl Shaker — 14.Ba’da Aalbal.2009 — "روح"
- file: `09.Rouh.mp3` | duration 327.108s | declared key D#m | tempo 88.0 | voice Vocal
- parse: 100% of bars
- pitch classes: Bb 31%, F# 17%, Ab 16%, F 15%, B 13%, C# 5%
- tonic: Bb (high, margin 0.149) | cues: most-used note -> Bb; phrase endings -> Bb; tool key & chords* -> Eb (key) / Eb (commonest chord root); other voice -> Bb
- scale: Kurd [Phrygian] (fit 0.993, shape confidence medium, name_allowed=True) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- candidate ghammaz: F# (800c, 21% of phrase endings)
- flags: same notes also fit other tonics: Eb (0.99), F# (0.99)  -> relative-mode ambiguity
- sections:
  - Section: verse: Bb low / Kurd medium (fit 0.987)  [!] tonic/dominant split: Bb and F (a 4th/5th apart) score almost equally; the true tonic could be either
  - Section: chorus: Bb high / Kurd medium (fit 0.98)  [!] same notes also fit other tonics: B (0.98), F# (0.98)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): Bb high / Kurd medium (fit 0.993)
- full report: `work/fadl-shaker-14-bada-aalbal-2009-09-rouh/report.md`
## 7. `fadl-shaker-14-bada-aalbal-2009-10-magrouh` — Fadl Shaker — 14.Ba’da Aalbal.2009 — "مجروح"
- file: `10.Magrouh.mp3` | duration 319.115s | declared key Fm | tempo 84.0 | voice Vocal
- parse: 100% of bars
- pitch classes: Bb 22%, Ab 22%, C 19%, G 14%, F 10%, C# 8%
- tonic: Ab (low, margin 0.008) | cues: most-used note -> Bb; phrase endings -> Ab; tool key & chords* -> F (key) / F (commonest chord root); other voice -> C
- scale: Ajam [major / Ionian] (fit 0.991, shape confidence medium, name_allowed=True) | tied: Rast, Ajam | 12-TET shadow of: Rast
- candidate ghammaz: C (400c, 23% of phrase endings)
- flags: same notes also fit other tonics: F (0.99), C (0.99), Bb (0.99)  -> relative-mode ambiguity
- sections:
  - Section: verse: F low / Nahawand medium (fit 1.0)  [!] tonic/dominant split: F and C (a 4th/5th apart) score almost equally; the true tonic could be either
  - Section: chorus: Ab low / Ajam low (fit 0.946)  [!] same notes also fit other tonics: C (0.95), Bb (0.95)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): Ab low / Ajam medium (fit 0.991)
- full report: `work/fadl-shaker-14-bada-aalbal-2009-10-magrouh/report.md`
## 8. `fadl-shaker-15-the-best-of-al-rawae3-2010-02-ya-mesaharny-el-lail` — Fadl Shaker — 15.The Best Of (Al Rawae3).2010 — "يا مسهرني الليل"
- file: `02.Ya Mesaharny El Lail.mp3` | duration 246.416s | declared key G#m | tempo 89.0 | voice Vocal
- parse: 100% of bars
- pitch classes: Ab 27%, B 22%, Bb 19%, C# 14%, F# 6%, E 5%
- tonic: Ab (high, margin 0.304) | cues: most-used note -> Ab; phrase endings -> Bb; tool key & chords* -> Ab (key) / Ab (commonest chord root); other voice -> Ab
- scale: Nahawand [natural minor / Aeolian] (fit 0.911, shape confidence low, name_allowed=True) | tied: Bayati, Nahawand | 12-TET shadow of: Bayati
- candidate ghammaz: E (800c, 12% of phrase endings)
- flags: same notes also fit other tonics: B (0.91), E (0.91)  -> relative-mode ambiguity
- sections:
  - Section: verse: B low / Ajam low (fit 0.839)  [!] same notes also fit other tonics: Ab (0.86), E (0.84)  -> relative-mode ambiguity
  - Section: chorus: Ab high / Nahawand medium (fit 1.0)  [!] same notes also fit other tonics: C# (1.00), B (1.00)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): Ab high / Nahawand low (fit 0.911)
- full report: `work/fadl-shaker-15-the-best-of-al-rawae3-2010-02-ya-mesaharny-el-lail/report.md`
