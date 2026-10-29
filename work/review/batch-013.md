# Maqam review — batch-013 (8 songs)

Read `skills/maqam-analysis/SKILL.md` before deciding. Hard rules:
- 12-TET ABC cannot prove quarter tones. Quarter-tone maqamat (Rast, Bayati, Saba, Sikah, Huzam, Iraq, Awj Ara, Suznek, Jiharkah, Bastanikar) are status `possible`, never `consistent`.
- If the analyzer says `name_allowed=false`, a scale is not identified, parse <95%, or pitch classes are too few: use `maqam_status="withheld"`.
- Confidence can be lowered, never raised above the tool's evidence.
- A tonic/dominant split must name the other tonic in `tonic_alternatives`.
- Never import outside knowledge of the song. Evidence is the ABC only.

Fill the sibling template, then run:
```bash
python3 scripts/review.py record --batch work/review/batch-013.json \
  --labels work/review/batch-013.labels.json
```

## 1. `fadl-shaker-02-bayya-a-el-qeloub-1999-07-ahbaby` — Fadl Shaker — 02.Bayya'a El Qeloub.1999 — "احبابي"
- file: `07.Ahbaby.mp3` | duration 354.116s | declared key D#m | tempo 83.0 | voice Vocal
- parse: 100% of bars
- pitch classes: C# 22%, F 18%, B 16%, Bb 15%, Eb 11%, D 7%
- tonic: Eb (low, margin 0.087) | cues: most-used note -> C#; phrase endings -> B; tool key & chords* -> Eb (key) / Eb (commonest chord root); other voice -> Eb
- scale: Nahawand [natural minor / Aeolian] (fit 0.881, shape confidence low, name_allowed=False) | tied: Bayati, Nahawand | 12-TET shadow of: Bayati
- candidate ghammaz: B (800c, 21% of phrase endings)
- flags: same notes also fit other tonics: B (0.88), Bb (0.88)  -> relative-mode ambiguity | no single scale explains this material (best fit 0.88); expect modulation, chromatic writing or quarter tones; do not name one maqam
- sections:
  - Section: chorus: Eb high / Nahawand (raised 7th) low (fit 0.839)  [!] same notes also fit other tonics: B (0.83), C# (0.83)  -> relative-mode ambiguity
  - Section: verse: Bb low / Saba low (fit 0.915)  [!] tonic/dominant split: Bb and Eb (a 4th/5th apart) score almost equally; the true tonic could be either
- melody-only cross-check (chords removed): Eb low / Nahawand low (fit 0.881)
- full report: `work/fadl-shaker-02-bayya-a-el-qeloub-1999-07-ahbaby/report.md`
## 2. `fadl-shaker-03-el-hob-el-qadeem-2000-01-aash-men-shafak` — Fadl Shaker — 03.El Hob El Qadeem.2000 — "عاش من شافك"
- file: `01.Aash Men Shafak.mp3` | duration 324.78s | declared key A | tempo 94.0 | voice Vocal
- parse: 100% of bars
- pitch classes: B 19%, A 18%, D 18%, E 14%, G 14%, F 8%
- tonic: E (high, margin 0.497) | cues: most-used note -> B; phrase endings -> E; tool key & chords* -> E (key) / E (commonest chord root); other voice -> E
- scale: Kurd [Phrygian] (fit 0.911, shape confidence low, name_allowed=True) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- flags: same notes also fit other tonics: A (0.91), D (0.91)  -> relative-mode ambiguity
- sections:
  - Section: verse: E low / Kurd low (fit 0.885)  [!] tonic/dominant split: E and A (a 4th/5th apart) score almost equally; the true tonic could be either
  - Section: chorus: E high / Kurd medium (fit 0.99)  [!] same notes also fit other tonics: A (0.99), D (0.99), G (0.99)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): E high / Kurd low (fit 0.911)
- full report: `work/fadl-shaker-03-el-hob-el-qadeem-2000-01-aash-men-shafak/report.md`
## 3. `fadl-shaker-03-el-hob-el-qadeem-2000-02-aadiha` — Fadl Shaker — 03.El Hob El Qadeem.2000 — "عديها"
- file: `02.Aadiha.mp3` | duration 292.023s | declared key Gm | tempo 90.0 | voice Vocal
- parse: 100% of bars
- pitch classes: Bb 27%, C 24%, D 19%, Ab 15%, G 14%, F 2%
- tonic: G (high, margin 0.624) | cues: most-used note -> Bb; phrase endings -> G; tool key & chords* -> G (key) / G (commonest chord root); other voice -> G
- scale: Kurd [Phrygian] (fit 0.96, shape confidence medium, name_allowed=True) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- flags: same notes also fit other tonics: C (0.96), Bb (0.96)  -> relative-mode ambiguity
- sections:
  - Section: verse: G low / Kurd medium (fit 0.96)  [!] same notes also fit other tonics: C (0.96), Ab (0.96)  -> relative-mode ambiguity
  - Section: chorus: G medium / Kurd medium (fit 0.98)  [!] same notes also fit other tonics: C (0.98), Bb (0.98), F (0.98)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): G high / Kurd medium (fit 0.96)
- full report: `work/fadl-shaker-03-el-hob-el-qadeem-2000-02-aadiha/report.md`
## 4. `fadl-shaker-03-el-hob-el-qadeem-2000-04-ma-fi-magal` — Fadl Shaker — 03.El Hob El Qadeem.2000 — "ما في مجال"
- file: `04.Ma Fi Magal.mp3` | duration 259.997s | declared key C#m | tempo 94.0 | voice Vocal
- parse: 100% of bars
- pitch classes: C# 32%, B 16%, A 13%, E 11%, Ab 8%, F# 8%
- tonic: C# (low, margin 0.128) | cues: most-used note -> C#; phrase endings -> E; tool key & chords* -> C# (key) / C# (commonest chord root); other voice -> Ab
- scale: Nahawand [natural minor / Aeolian] (fit 0.976, shape confidence medium, name_allowed=True) | tied: Bayati, Nahawand | 12-TET shadow of: Bayati
- candidate ghammaz: E (300c, 33% of phrase endings)
- flags: same notes also fit other tonics: E (0.98), F# (0.98), B (0.98)  -> relative-mode ambiguity
- sections:
  - Section: verse: C# medium / Nahawand medium (fit 0.982)  [!] same notes also fit other tonics: F# (0.98), B (0.98), Ab (0.98)  -> relative-mode ambiguity
  - Section: chorus: E low / Ajam low (fit 0.917)  [!] same notes also fit other tonics: C# (0.92), Ab (0.92), B (0.92)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): C# low / Nahawand medium (fit 0.976)
- full report: `work/fadl-shaker-03-el-hob-el-qadeem-2000-04-ma-fi-magal/report.md`
## 5. `fadl-shaker-03-el-hob-el-qadeem-2000-05-habaytoh` — Fadl Shaker — 03.El Hob El Qadeem.2000 — "حبيته"
- file: `05.Habaytoh.mp3` | duration 261.433s | declared key Bm | tempo 99.0 | voice Vocal
- parse: 100% of bars
- pitch classes: B 47%, D 23%, C# 14%, E 8%, Bb 3%, Ab 3%
- tonic: B (high, margin 0.749) | cues: most-used note -> B; phrase endings -> B; tool key & chords* -> B (key) / B (commonest chord root); other voice -> B
- scale: Rast (fit 1.0, shape confidence medium, name_allowed=True) | tied: Rast | 12-TET shadow of: Rast
- sections:
  - Section: chorus: B high / Rast medium (fit 1.0)
  - Section: verse: B high / Rast medium (fit 0.96)  [!] same notes also fit other tonics: C# (0.96)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): B high / Rast medium (fit 1.0)
- full report: `work/fadl-shaker-03-el-hob-el-qadeem-2000-05-habaytoh/report.md`
## 6. `fadl-shaker-03-el-hob-el-qadeem-2000-06-el-hob-shey-tany` — Fadl Shaker — 03.El Hob El Qadeem.2000 — "الحب شي ثاني"
- file: `06.El Hob Shey' Tany.mp3` | duration 293.46s | declared key Cm | tempo 139.0 | voice Vocal
- parse: 100% of bars
- pitch classes: Bb 38%, C 26%, Ab 16%, D 9%, G 9%, Eb 2%
- tonic: C (low, margin 0.079) | cues: most-used note -> Bb; phrase endings -> G; tool key & chords* -> C (key) / G (commonest chord root); other voice -> G
- scale: Nahawand [natural minor / Aeolian] (fit 0.948, shape confidence low, name_allowed=True) | tied: Bayati, Nahawand | 12-TET shadow of: Bayati
- candidate ghammaz: Bb (1000c, 38% of phrase endings)
- flags: tonic/dominant split: C and G (a 4th/5th apart) score almost equally; the true tonic could be either | same notes also fit other tonics: G (0.95), Bb (0.95)  -> relative-mode ambiguity
- sections:
  - Section: verse: C low / Nahawand low (fit 0.943)  [!] same notes also fit other tonics: Bb (0.94), G (0.94)  -> relative-mode ambiguity
  - Section: chorus: C low / Nahawand medium (fit 0.98)  [!] tonic/dominant split: C and G (a 4th/5th apart) score almost equally; the true tonic could be either
- melody-only cross-check (chords removed): C low / Nahawand low (fit 0.948)
- full report: `work/fadl-shaker-03-el-hob-el-qadeem-2000-06-el-hob-shey-tany/report.md`
## 7. `fadl-shaker-03-el-hob-el-qadeem-2000-07-men-gher-sabab` — Fadl Shaker — 03.El Hob El Qadeem.2000 — "من غير سبب"
- file: `07.Men Gher Sabab.mp3` | duration 281.234s | declared key C#m | tempo 85.0 | voice Vocal
- parse: 100% of bars
- pitch classes: A 34%, B 24%, C# 10%, F# 10%, Ab 9%, E 6%
- tonic: A (low, margin 0.149) | cues: most-used note -> A; phrase endings -> A; tool key & chords* -> C# (key) / Ab (commonest chord root); other voice -> Ab
- scale: Ajam [major / Ionian] (fit 0.862, shape confidence low, name_allowed=False) | tied: Rast, Ajam, (no standard maqam) | 12-TET shadow of: Rast
- candidate ghammaz: E (700c, 14% of phrase endings)
- flags: same notes also fit other tonics: C# (0.86), B (0.86), Ab (0.86)  -> relative-mode ambiguity | no single scale explains this material (best fit 0.86); expect modulation, chromatic writing or quarter tones; do not name one maqam
- sections:
  - Section: verse: B low / (no standard maqam) medium (fit 0.98)  [!] same notes also fit other tonics: C# (0.98), Ab (0.98), A (0.98)  -> relative-mode ambiguity
  - Section: chorus: A low / Rast low (fit 0.76)  [!] same notes also fit other tonics: C# (0.88), Ab (0.88)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): A low / Ajam low (fit 0.862)
- full report: `work/fadl-shaker-03-el-hob-el-qadeem-2000-07-men-gher-sabab/report.md`
## 8. `fadl-shaker-05-hobak-khayal-2001-01-hobak-khayal` — Fadl Shaker — 05.Hobak Khayal.2001 — "حبك خيال"
- file: `01.Hobak Khayal.mp3` | duration 281.783s | declared key Gm | tempo 126.0 | voice Vocal
- parse: 100% of bars
- pitch classes: Bb 30%, C 27%, D 20%, Ab 10%, G 9%, Eb 2%
- tonic: G (high, margin 0.412) | cues: most-used note -> Bb; phrase endings -> G; tool key & chords* -> G (key) / G (commonest chord root); other voice -> G
- scale: Kurd [Phrygian] (fit 0.949, shape confidence low, name_allowed=True) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- candidate ghammaz: Bb (300c, 20% of phrase endings)
- flags: same notes also fit other tonics: C (0.95), Bb (0.95)  -> relative-mode ambiguity
- sections:
  - Section: verse: G low / Kurd low (fit 0.905)  [!] same notes also fit other tonics: Bb (0.90), Ab (0.90)  -> relative-mode ambiguity
  - Section: chorus: G low / Kurd medium (fit 0.957)  [!] same notes also fit other tonics: C (0.96), Bb (0.96)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): G high / Kurd low (fit 0.949)
- full report: `work/fadl-shaker-05-hobak-khayal-2001-01-hobak-khayal/report.md`
