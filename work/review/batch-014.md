# Maqam review — batch-014 (8 songs)

Read `skills/maqam-analysis/SKILL.md` before deciding. Hard rules:
- 12-TET ABC cannot prove quarter tones. Quarter-tone maqamat (Rast, Bayati, Saba, Sikah, Huzam, Iraq, Awj Ara, Suznek, Jiharkah, Bastanikar) are status `possible`, never `consistent`.
- If the analyzer says `name_allowed=false`, a scale is not identified, parse <95%, or pitch classes are too few: use `maqam_status="withheld"`.
- Confidence can be lowered, never raised above the tool's evidence.
- A tonic/dominant split must name the other tonic in `tonic_alternatives`.
- Never import outside knowledge of the song. Evidence is the ABC only.

Fill the sibling template, then run:
```bash
python3 scripts/review.py record --batch work/review/batch-014.json \
  --labels work/review/batch-014.labels.json
```

## 1. `fadl-shaker-06-sidi-rohi-2003-01-ya-habibi-ta-ala` — Fadl Shaker — 06.Sidi Rohi.2003 — "يا حبيبي تعال"
- file: `01.Ya Habibi Ta'ala.mp3` | duration 260.702s | declared key Am | tempo 126.0 | voice Vocal
- parse: 100% of bars
- pitch classes: C 21%, D 17%, A 17%, B 16%, E 13%, F 8%
- tonic: A (low, margin 0.003) | cues: most-used note -> C; phrase endings -> E; tool key & chords* -> A (key) / A (commonest chord root); other voice -> A
- scale: Nahawand [natural minor / Aeolian] (fit 1.0, shape confidence medium, name_allowed=True) | tied: Bayati, Nahawand | 12-TET shadow of: Bayati
- candidate ghammaz: E (700c, 46% of phrase endings)
- flags: tonic/dominant split: A and E (a 4th/5th apart) score almost equally; the true tonic could be either | same notes also fit other tonics: E (1.00), D (1.00)  -> relative-mode ambiguity
- sections:
  - Section: verse: A low / Nahawand medium (fit 1.0)  [!] same notes also fit other tonics: D (1.00), G (1.00), E (1.00)  -> relative-mode ambiguity
  - Section: chorus: E low / Kurd medium (fit 1.0)  [!] tonic/dominant split: E and A (a 4th/5th apart) score almost equally; the true tonic could be either
  - Section: bridge: C low / Ajam medium (fit 0.98)  [!] same notes also fit other tonics: E (0.98), A (0.98), D (0.98)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): E low / Kurd medium (fit 1.0)
- full report: `work/fadl-shaker-06-sidi-rohi-2003-01-ya-habibi-ta-ala/report.md`
## 2. `fadl-shaker-06-sidi-rohi-2003-03-yomi-besana` — Fadl Shaker — 06.Sidi Rohi.2003 — "يومي بسنة"
- file: `03.Yomi Besana.mp3` | duration 255.896s | declared key Am | tempo 134.0 | voice Vocal
- parse: 100% of bars
- pitch classes: A 37%, G 22%, B 21%, F 6%, E 6%, C 4%
- tonic: A (low, margin 0.067) | cues: most-used note -> A; phrase endings -> G; tool key & chords* -> A (key) / E (commonest chord root); other voice -> B
- scale: Nahawand [natural minor / Aeolian] (fit 1.0, shape confidence medium, name_allowed=True) | tied: Bayati, Nahawand | 12-TET shadow of: Bayati
- candidate ghammaz: G (1000c, 67% of phrase endings)
- flags: same notes also fit other tonics: G (1.00), E (1.00)  -> relative-mode ambiguity
- sections:
  - Section: verse: A low / Nahawand medium (fit 1.0)  [!] same notes also fit other tonics: G (1.00), E (1.00)  -> relative-mode ambiguity
  - Section: chorus: A high / Nahawand medium (fit 1.0)  [!] same notes also fit other tonics: G (1.00), E (1.00)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): A low / Nahawand medium (fit 1.0)
- full report: `work/fadl-shaker-06-sidi-rohi-2003-03-yomi-besana/report.md`
## 3. `fadl-shaker-06-sidi-rohi-2003-04-law-faker` — Fadl Shaker — 06.Sidi Rohi.2003 — "لو فاكر"
- file: `04.Law Faker.mp3` | duration 191.029s | declared key Gm | tempo 103.0 | voice Vocal
- parse: 100% of bars
- pitch classes: Bb 26%, Ab 19%, G 18%, C 17%, D 14%, F 5%
- tonic: G (low, margin 0.398) | cues: most-used note -> Bb; phrase endings -> G; tool key & chords* -> G (key) / G (commonest chord root); other voice -> Bb
- scale: Kurd [Phrygian] (fit 1.0, shape confidence medium, name_allowed=True) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- flags: same notes also fit other tonics: Ab (1.00), Bb (1.00), C (1.00)  -> relative-mode ambiguity
- sections:
  - Section: verse: G low / Kurd medium (fit 1.0)  [!] same notes also fit other tonics: Bb (1.00), C (1.00), Ab (1.00)  -> relative-mode ambiguity
  - Section: chorus: Ab low / (no standard maqam) medium (fit 0.98)  [!] same notes also fit other tonics: G (0.98), Bb (0.98), C (0.98)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): G low / Kurd medium (fit 1.0)
- full report: `work/fadl-shaker-06-sidi-rohi-2003-04-law-faker/report.md`
## 4. `fadl-shaker-06-sidi-rohi-2003-05-ma-khalas` — Fadl Shaker — 06.Sidi Rohi.2003 — "ما خلاص"
- file: `05.Ma Khalas.mp3` | duration 283.945s | declared key Cm | tempo 169.0 | voice Vocal
- parse: 100% of bars
- pitch classes: Bb 21%, Ab 20%, C 19%, D 18%, G 16%, Eb 4%
- tonic: G (low, margin 0.059) | cues: most-used note -> Bb; phrase endings -> G; tool key & chords* -> C (key) / F (commonest chord root); other voice -> G
- scale: Kurd [Phrygian] (fit 0.98, shape confidence medium, name_allowed=True) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- candidate ghammaz: Bb (300c, 24% of phrase endings)
- flags: tonic/dominant split: G and C (a 4th/5th apart) score almost equally; the true tonic could be either | same notes also fit other tonics: C (0.98), Ab (0.98), Bb (0.98)  -> relative-mode ambiguity
- sections:
  - Section: verse: Bb low / (no standard maqam) medium (fit 0.98)  [!] same notes also fit other tonics: G (0.98), Ab (0.98), C (0.98)  -> relative-mode ambiguity
  - Section: chorus: G low / Kurd medium (fit 0.98)  [!] same notes also fit other tonics: C (0.98), F (0.98)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): G low / Kurd medium (fit 0.98)
- full report: `work/fadl-shaker-06-sidi-rohi-2003-05-ma-khalas/report.md`
## 5. `fadl-shaker-06-sidi-rohi-2003-08-laih-ya-zaman` — Fadl Shaker — 06.Sidi Rohi.2003 — "ليه يا زمان"
- file: `08.Laih Ya Zaman.mp3` | duration 308.584s | declared key Am | tempo 121.0 | voice Vocal
- parse: 100% of bars
- pitch classes: A 24%, B 17%, G 14%, F 13%, E 12%, C 11%
- tonic: A (low, margin 0.053) | cues: most-used note -> A; phrase endings -> B; tool key & chords* -> A (key) / A (commonest chord root); other voice -> B
- scale: Nahawand [natural minor / Aeolian] (fit 1.0, shape confidence medium, name_allowed=True) | tied: Bayati, Nahawand | 12-TET shadow of: Bayati
- candidate ghammaz: F (800c, 17% of phrase endings)
- flags: same notes also fit other tonics: F (1.00), G (1.00)  -> relative-mode ambiguity
- sections:
  - Section: verse: A high / Nahawand medium (fit 0.98)  [!] same notes also fit other tonics: F (0.98), G (0.98)  -> relative-mode ambiguity
  - Section: chorus: B high / Kurd low (fit 0.852)  [!] same notes also fit other tonics: A (1.00), C (1.00), E (1.00)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): A low / Nahawand medium (fit 1.0)
- full report: `work/fadl-shaker-06-sidi-rohi-2003-08-laih-ya-zaman/report.md`
## 6. `fadl-shaker-06-sidi-rohi-2003-10-zalamoni` — Fadl Shaker — 06.Sidi Rohi.2003 — "ظلموني"
- file: `10.Zalamoni.mp3` | duration 288.069s | declared key D#m | tempo 137.0 | voice Vocal
- parse: 100% of bars
- pitch classes: B 34%, C# 29%, Bb 21%, Eb 10%, Ab 3%, F# 1%
- tonic: Bb (low, margin 0.448) | cues: most-used note -> B; phrase endings -> Bb; tool key & chords* -> Eb (key) / Bb (commonest chord root); other voice -> Bb
- scale: Kurd [Phrygian] (fit 0.96, shape confidence medium, name_allowed=True) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- flags: same notes also fit other tonics: Eb (0.96), C# (0.96), B (0.96)  -> relative-mode ambiguity
- sections:
  - Section: verse: Eb low / Nahawand medium (fit 0.98)  [!] same notes also fit other tonics: B (0.98), Bb (0.98), C# (0.98)  -> relative-mode ambiguity
  - Section: chorus: Bb low / Kurd low (fit 0.94)  [!] same notes also fit other tonics: Eb (0.94), C# (0.94), B (0.94)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): Bb low / Kurd medium (fit 0.96)
- full report: `work/fadl-shaker-06-sidi-rohi-2003-10-zalamoni/report.md`
## 7. `fadl-shaker-06-sidi-rohi-2003-11-sidi-rohi` — Fadl Shaker — 06.Sidi Rohi.2003 — "سيدي روحي"
- file: `11.Sidi Rohi.mp3` | duration 250.984s | declared key Fm | tempo 101.0 | voice Vocal
- parse: 100% of bars
- pitch classes: Bb 29%, C 24%, Ab 18%, F 13%, G 13%, Eb 3%
- tonic: F (low, margin 0.152) | cues: most-used note -> Bb; phrase endings -> Eb; tool key & chords* -> F (key) / F (commonest chord root); other voice -> F
- scale: Nahawand [natural minor / Aeolian] (fit 0.98, shape confidence medium, name_allowed=True) | tied: Bayati, Nahawand, Rast, (no standard maqam) | 12-TET shadow of: Bayati, Rast
- candidate ghammaz: Eb (1000c, 46% of phrase endings)
- flags: same notes also fit other tonics: Eb (0.98), C (0.98), Bb (0.98)  -> relative-mode ambiguity
- sections:
  - Section: verse: F low / Nahawand medium (fit 0.96)  [!] same notes also fit other tonics: G (0.96), Bb (0.96), C (0.96)  -> relative-mode ambiguity
  - Section: chorus: F low / Nahawand medium (fit 0.98)  [!] same notes also fit other tonics: Eb (0.98), C (0.98), Bb (0.98)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): F low / Nahawand medium (fit 0.98)
- full report: `work/fadl-shaker-06-sidi-rohi-2003-11-sidi-rohi/report.md`
## 8. `fadl-shaker-07-fadl-shaker-2003-01-tayer-ya-hawa` — Fadl Shaker — 07.Fadl Shaker.2003 — "طاير يا هوى"
- file: `01.Tayer Ya Hawa.mp3` | duration 291.683s | declared key Bm | tempo 74.0 | voice Vocal
- parse: 100% of bars
- pitch classes: E 17%, D 17%, B 17%, G 16%, A 16%, C 9%
- tonic: D (low, margin 0.014) | cues: most-used note -> E; phrase endings -> D; tool key & chords* -> B (key) / B (commonest chord root); other voice -> B
- scale: (no standard maqam) [Mixolydian] (fit 1.0, shape confidence medium, name_allowed=True) | tied: Rast, (no standard maqam) | 12-TET shadow of: Rast
- candidate ghammaz: G (500c, 22% of phrase endings)
- flags: same notes also fit other tonics: B (1.00), E (1.00), G (1.00)  -> relative-mode ambiguity
- sections:
  - Section: verse: D low / (no standard maqam) medium (fit 1.0)  [!] same notes also fit other tonics: B (1.00), C (1.00), G (1.00)  -> relative-mode ambiguity
  - Section: chorus: B low / Kurd medium (fit 1.0)  [!] same notes also fit other tonics: D (1.00), G (1.00), E (1.00)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): D low / (no standard maqam) medium (fit 1.0)
- full report: `work/fadl-shaker-07-fadl-shaker-2003-01-tayer-ya-hawa/report.md`
