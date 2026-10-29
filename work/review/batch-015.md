# Maqam review — batch-015 (8 songs)

Read `skills/maqam-analysis/SKILL.md` before deciding. Hard rules:
- 12-TET ABC cannot prove quarter tones. Quarter-tone maqamat (Rast, Bayati, Saba, Sikah, Huzam, Iraq, Awj Ara, Suznek, Jiharkah, Bastanikar) are status `possible`, never `consistent`.
- If the analyzer says `name_allowed=false`, a scale is not identified, parse <95%, or pitch classes are too few: use `maqam_status="withheld"`.
- Confidence can be lowered, never raised above the tool's evidence.
- A tonic/dominant split must name the other tonic in `tonic_alternatives`.
- Never import outside knowledge of the song. Evidence is the ABC only.

Fill the sibling template, then run:
```bash
python3 scripts/review.py record --batch work/review/batch-015.json \
  --labels work/review/batch-015.labels.json
```

## 1. `fadl-shaker-07-fadl-shaker-2003-08-elli-rahou` — Fadl Shaker — 07.Fadl Shaker.2003 — "اللي راحوا"
- file: `08.Elli Rahou.mp3` | duration 256.522s | declared key Gm | tempo 90.0 | voice Vocal
- parse: 100% of bars
- pitch classes: D 28%, C 26%, A 16%, B 15%, G 9%, F 4%
- tonic: G (low, margin 0.069) | cues: most-used note -> D; phrase endings -> A; tool key & chords* -> G (key) / G (commonest chord root); other voice -> G
- scale: (no standard maqam) [Mixolydian] (fit 1.0, shape confidence medium, name_allowed=True) | tied: Rast, (no standard maqam) | 12-TET shadow of: Rast
- candidate ghammaz: C (500c, 33% of phrase endings)
- flags: same notes also fit other tonics: A (1.00), C (1.00), D (1.00)  -> relative-mode ambiguity
- sections:
  - Section: verse: A low / Nahawand medium (fit 1.0)  [!] same notes also fit other tonics: G (1.00), D (1.00), C (1.00)  -> relative-mode ambiguity
  - Section: chorus: G low / (no standard maqam) medium (fit 1.0)  [!] tonic/dominant split: G and C (a 4th/5th apart) score almost equally; the true tonic could be either
- melody-only cross-check (chords removed): A low / Nahawand medium (fit 1.0)
- full report: `work/fadl-shaker-07-fadl-shaker-2003-08-elli-rahou/report.md`
## 2. `fadl-shaker-07-fadl-shaker-2003-09-khedni-ma-ak` — Fadl Shaker — 07.Fadl Shaker.2003 — "اخدني معاك"
- file: `09.Khedni Ma'ak.mp3` | duration 311.693s | declared key Gm | tempo 107.0 | voice Vocal
- parse: 100% of bars
- pitch classes: G 22%, Bb 20%, D 17%, A 17%, F 10%, C 10%
- tonic: D (low, margin 0.06) | cues: most-used note -> G; phrase endings -> D; tool key & chords* -> G (key) / D (commonest chord root); other voice -> D
- scale: Kurd [Phrygian] (fit 0.994, shape confidence medium, name_allowed=True) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- candidate ghammaz: G (500c, 25% of phrase endings)
- flags: tonic/dominant split: D and G (a 4th/5th apart) score almost equally; the true tonic could be either | same notes also fit other tonics: G (0.99), Bb (0.99), C (0.99)  -> relative-mode ambiguity
- sections:
  - Section: verse: D low / Kurd medium (fit 0.994)  [!] tonic/dominant split: D and G (a 4th/5th apart) score almost equally; the true tonic could be either
  - Section: chorus: G low / Nahawand medium (fit 0.96)  [!] tonic/dominant split: G and D (a 4th/5th apart) score almost equally; the true tonic could be either
- melody-only cross-check (chords removed): D low / Kurd medium (fit 0.994)
- full report: `work/fadl-shaker-07-fadl-shaker-2003-09-khedni-ma-ak/report.md`
## 3. `fadl-shaker-08-hafla-2004-01-law-faker` — Fadl Shaker — 08.Hafla 2004 — "لو فاكر"
- file: `01.Law Faker.mp3` | duration 202.344s | declared key Cm | tempo 105.0 | voice Vocal
- parse: 100% of bars
- pitch classes: Bb 24%, C 21%, G 21%, Ab 15%, D 10%, F 5%
- tonic: G (low, margin 0.394) | cues: most-used note -> Bb; phrase endings -> G; tool key & chords* -> C (key) / C (commonest chord root); other voice -> G
- scale: Kurd [Phrygian] (fit 1.0, shape confidence medium, name_allowed=True) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- flags: same notes also fit other tonics: C (1.00), Bb (1.00), Ab (1.00)  -> relative-mode ambiguity
- sections:
  - Section: verse: G high / Kurd medium (fit 1.0)  [!] same notes also fit other tonics: C (1.00), Bb (1.00), Ab (1.00)  -> relative-mode ambiguity
  - Section: chorus: G low / Kurd medium (fit 0.98)  [!] same notes also fit other tonics: C (0.98), Bb (0.98)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): G low / Kurd medium (fit 1.0)
- full report: `work/fadl-shaker-08-hafla-2004-01-law-faker/report.md`
## 4. `fadl-shaker-08-hafla-2004-02-sidi-rohi` — Fadl Shaker — 08.Hafla 2004 — "سيدي روحي"
- file: `02.Sidi Rohi.mp3` | duration 217.104s | declared key Gm | tempo 104.0 | voice Vocal
- parse: 100% of bars
- pitch classes: C 32%, D 23%, Bb 18%, G 15%, A 10%, F 2%
- tonic: G (low, margin 0.161) | cues: most-used note -> C; phrase endings -> Bb; tool key & chords* -> G (key) / G (commonest chord root); other voice -> G
- scale: Nahawand [natural minor / Aeolian] (fit 0.96, shape confidence medium, name_allowed=True) | tied: Rast, Bayati, Nahawand, (no standard maqam) | 12-TET shadow of: Rast, Bayati
- candidate ghammaz: Bb (300c, 54% of phrase endings)
- flags: same notes also fit other tonics: D (0.96), C (0.96), Bb (0.96)  -> relative-mode ambiguity
- sections:
  - Section: verse: G low / Nahawand medium (fit 0.96)  [!] same notes also fit other tonics: C (0.96), D (0.96), A (0.96)  -> relative-mode ambiguity
  - Section: chorus: C low / (no standard maqam) medium (fit 0.96)  [!] tonic/dominant split: C and G (a 4th/5th apart) score almost equally; the true tonic could be either
- melody-only cross-check (chords removed): G low / Nahawand medium (fit 0.96)
- full report: `work/fadl-shaker-08-hafla-2004-02-sidi-rohi/report.md`
## 5. `fadl-shaker-08-hafla-2004-03-ma-agool` — Fadl Shaker — 08.Hafla 2004 — "معقول"
- file: `03.Ma'agool.mp3` | duration 341.656s | declared key Am | tempo 107.0 | voice Vocal
- parse: 100% of bars
- pitch classes: A 30%, B 28%, G 13%, C 12%, D 6%, E 5%
- tonic: A (high, margin 0.308) | cues: most-used note -> A; phrase endings -> A; tool key & chords* -> A (key) / A (commonest chord root); other voice -> A
- scale: Nahawand [natural minor / Aeolian] (fit 0.981, shape confidence medium, name_allowed=True) | tied: Bayati, Nahawand | 12-TET shadow of: Bayati
- flags: same notes also fit other tonics: G (0.98), E (0.98)  -> relative-mode ambiguity
- sections:
  - Section: verse: A low / Nahawand low (fit 0.924)  [!] same notes also fit other tonics: G (0.92), C (0.92)  -> relative-mode ambiguity
  - Section: chorus: A high / Nahawand medium (fit 1.0)  [!] same notes also fit other tonics: G (1.00), F (1.00), C (1.00)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): A high / Nahawand medium (fit 0.981)
- full report: `work/fadl-shaker-08-hafla-2004-03-ma-agool/report.md`
## 6. `fadl-shaker-08-hafla-2004-04-ya-ghayeb` — Fadl Shaker — 08.Hafla 2004 — "يا غايب"
- file: `04.Ya Ghayeb.mp3` | duration 326.896s | declared key Cm | tempo 111.0 | voice Vocal
- parse: 100% of bars
- pitch classes: C 33%, D 19%, Eb 13%, G 11%, F 11%, Bb 10%
- tonic: C (medium, margin 0.052) | cues: most-used note -> C; phrase endings -> Bb; tool key & chords* -> C (key) / C (commonest chord root); other voice -> C
- scale: Nahawand [natural minor / Aeolian] (fit 1.0, shape confidence medium, name_allowed=True) | tied: Bayati, Nahawand | 12-TET shadow of: Bayati
- candidate ghammaz: Bb (1000c, 50% of phrase endings)
- flags: same notes also fit other tonics: Bb (1.00), G (1.00)  -> relative-mode ambiguity
- sections:
  - Section: verse: Bb low / (no standard maqam) medium (fit 0.98)  [!] same notes also fit other tonics: Ab (0.98), C (0.98), Eb (0.98)  -> relative-mode ambiguity
  - Section: chorus: G medium / Kurd medium (fit 0.98)  [!] same notes also fit other tonics: Bb (0.98), C (0.98), Eb (0.98)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): C medium / Nahawand medium (fit 1.0)
- full report: `work/fadl-shaker-08-hafla-2004-04-ya-ghayeb/report.md`
## 7. `fadl-shaker-08-hafla-2004-06-ya-habibi-ta-ala` — Fadl Shaker — 08.Hafla 2004 — "يا حبيبي تعال"
- file: `06.Ya Habibi Ta'ala.mp3` | duration 360.02s | declared key Am | tempo 136.0 | voice Vocal
- parse: 100% of bars
- pitch classes: C 20%, B 18%, A 18%, E 15%, D 15%, G 7%
- tonic: E (low, margin 0.047) | cues: most-used note -> C; phrase endings -> E; tool key & chords* -> A (key) / A (commonest chord root); other voice -> A
- scale: Kurd [Phrygian] (fit 0.997, shape confidence medium, name_allowed=True) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- candidate ghammaz: A (500c, 21% of phrase endings)
- flags: tonic/dominant split: E and A (a 4th/5th apart) score almost equally; the true tonic could be either | same notes also fit other tonics: A (1.00), C (1.00), D (1.00)  -> relative-mode ambiguity
- sections:
  - Section: verse: A medium / Nahawand medium (fit 0.991)  [!] same notes also fit other tonics: D (0.99), C (0.99)  -> relative-mode ambiguity
  - Section: chorus: E low / Kurd medium (fit 1.0)  [!] same notes also fit other tonics: A (1.00), D (1.00), C (1.00)  -> relative-mode ambiguity
  - Section: bridge: E low / Kurd medium (fit 0.98)  [!] tonic/dominant split: E and A (a 4th/5th apart) score almost equally; the true tonic could be either
- melody-only cross-check (chords removed): E low / Kurd medium (fit 0.997)
- full report: `work/fadl-shaker-08-hafla-2004-06-ya-habibi-ta-ala/report.md`
## 8. `fadl-shaker-08-hafla-2004-07-meta-habibi` — Fadl Shaker — 08.Hafla 2004 — "متى حبيبي متى"
- file: `07.Meta Habibi.mp3` | duration 266.762s | declared key Cm | tempo 108.0 | voice Vocal
- parse: 100% of bars
- pitch classes: Bb 27%, C 25%, D 21%, G 12%, Ab 12%, Eb 2%
- tonic: C (low, margin 0.061) | cues: most-used note -> Bb; phrase endings -> G; tool key & chords* -> C (key) / G (commonest chord root); other voice -> G
- scale: Nahawand [natural minor / Aeolian] (fit 0.98, shape confidence medium, name_allowed=True) | tied: Bayati, Nahawand, Saba | 12-TET shadow of: Bayati, Saba
- candidate ghammaz: G (700c, 50% of phrase endings)
- flags: tonic/dominant split: C and G (a 4th/5th apart) score almost equally; the true tonic could be either | same notes also fit other tonics: G (0.98), Bb (0.98)  -> relative-mode ambiguity
- sections:
  - Section: verse: G low / Kurd medium (fit 0.96)  [!] same notes also fit other tonics: C (0.96), Ab (0.96)  -> relative-mode ambiguity
  - Section: chorus: C high / Nahawand medium (fit 0.98)  [!] same notes also fit other tonics: G (0.98), Bb (0.98)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): C low / Nahawand medium (fit 0.98)
- full report: `work/fadl-shaker-08-hafla-2004-07-meta-habibi/report.md`
