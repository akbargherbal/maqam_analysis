# Maqam review — batch-009 (8 songs)

Read `skills/maqam-analysis/SKILL.md` before deciding. Hard rules:
- 12-TET ABC cannot prove quarter tones. Quarter-tone maqamat (Rast, Bayati, Saba, Sikah, Huzam, Iraq, Awj Ara, Suznek, Jiharkah, Bastanikar) are status `possible`, never `consistent`.
- If the analyzer says `name_allowed=false`, a scale is not identified, parse <95%, or pitch classes are too few: use `maqam_status="withheld"`.
- Confidence can be lowered, never raised above the tool's evidence.
- A tonic/dominant split must name the other tonic in `tonic_alternatives`.
- Never import outside knowledge of the song. Evidence is the ABC only.

Fill the sibling template, then run:
```bash
python3 scripts/review.py record --batch work/review/batch-009.json \
  --labels work/review/batch-009.labels.json
```

## 1. `elissa-2008-ayami-beek-10-sahar-einy` — Elissa — Elissa - 2008 Ayami Beek — "سهر عيني"
- file: `10. Sahar Einy.mp3` | duration 274.993s | declared key Dm | tempo 84.0 | voice Vocal
- parse: 100% of bars
- pitch classes: A 19%, C 16%, G 15%, E 14%, F 13%, D 12%
- tonic: A (low, margin 0.313) | cues: most-used note -> A; phrase endings -> A; tool key & chords* -> D (key) / D (commonest chord root); other voice -> E
- scale: Kurd [Phrygian] (fit 1.0, shape confidence medium, name_allowed=True) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- candidate ghammaz: E (700c, 20% of phrase endings)
- flags: same notes also fit other tonics: D (1.00), C (1.00)  -> relative-mode ambiguity
- sections:
  - Section: verse: A low / Kurd medium (fit 1.0)  [!] same notes also fit other tonics: D (1.00), C (1.00)  -> relative-mode ambiguity
  - Section: chorus: A low / Kurd medium (fit 1.0)  [!] same notes also fit other tonics: D (1.00), Bb (1.00), G (1.00)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): A low / Kurd medium (fit 1.0)
- full report: `work/elissa-2008-ayami-beek-10-sahar-einy/report.md`
## 2. `elissa-2008-ayami-beek-11-awakhir-el-shity` — Elissa — Elissa - 2008 Ayami Beek — "أواخر الشتا"
- file: `11. Awakhir El Shity.mp3` | duration 272.565s | declared key Am | tempo 133.0 | voice Vocal
- parse: 100% of bars
- pitch classes: E 22%, F 19%, G 16%, D 14%, A 10%, B 9%
- tonic: E (low, margin 0.102) | cues: most-used note -> E; phrase endings -> E; tool key & chords* -> A (key) / A (commonest chord root); other voice -> A
- scale: Kurd [Phrygian] (fit 0.984, shape confidence medium, name_allowed=True) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- candidate ghammaz: B (700c, 40% of phrase endings)
- flags: same notes also fit other tonics: A (0.98), F (0.98)  -> relative-mode ambiguity
- sections:
  - Section: verse: E low / Kurd medium (fit 0.985)  [!] tonic/dominant split: E and B (a 4th/5th apart) score almost equally; the true tonic could be either
  - Section: chorus: E low / Kurd low (fit 0.941)  [!] same notes also fit other tonics: A (0.94), F (0.94), G (0.94)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): E low / Kurd medium (fit 0.984)
- full report: `work/elissa-2008-ayami-beek-11-awakhir-el-shity/report.md`
## 3. `elissa-2009-tesada-a-bemeen-01-tesada-a-bemeen` — Elissa — Elissa - 2009 Tesada'a Bemeen — "تصدق بمين"
- file: `01.Tesada'a Bemeen.mp3` | duration 277.603s | declared key Am | tempo 131.0 | voice Vocal
- parse: 100% of bars
- pitch classes: E 19%, D 18%, C 15%, A 13%, F 12%, B 11%
- tonic: A (low, margin 0.036) | cues: most-used note -> E; phrase endings -> A; tool key & chords* -> A (key) / E (commonest chord root); other voice -> E
- scale: Nahawand [natural minor / Aeolian] (fit 0.982, shape confidence medium, name_allowed=True) | tied: Bayati, Nahawand | 12-TET shadow of: Bayati
- candidate ghammaz: E (700c, 37% of phrase endings)
- flags: tonic/dominant split: A and E (a 4th/5th apart) score almost equally; the true tonic could be either | same notes also fit other tonics: E (0.98), F (0.98)  -> relative-mode ambiguity
- sections:
  - Section: verse: E low / Kurd medium (fit 0.954)  [!] tonic/dominant split: E and B (a 4th/5th apart) score almost equally; the true tonic could be either
  - Section: chorus: A high / Nahawand medium (fit 0.96)  [!] same notes also fit other tonics: E (0.96), G (0.96), F (0.96)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): A low / Nahawand medium (fit 0.982)
- full report: `work/elissa-2009-tesada-a-bemeen-01-tesada-a-bemeen/report.md`
## 4. `elissa-2009-tesada-a-bemeen-02-aa-bali-habibi` — Elissa — Elissa - 2009 Tesada'a Bemeen — "ع بالي حبيبي"
- file: `02.Aa Bali Habibi.mp3` | duration 322.743s | declared key Gm | tempo 86.0 | voice Vocal
- parse: 100% of bars
- pitch classes: A 18%, D 17%, G 17%, Eb 16%, Bb 15%, F 12%
- tonic: A (low, margin 0.025) | cues: most-used note -> A; phrase endings -> Eb; tool key & chords* -> G (key) / G (commonest chord root); other voice -> A
- scale: Kurd [Phrygian] (fit 0.771, shape confidence low, name_allowed=False) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- candidate ghammaz: Eb (600c, 48% of phrase endings)
- flags: same notes also fit other tonics: G (0.99), Eb (0.99), D (0.99)  -> relative-mode ambiguity | no single scale explains this material (best fit 0.77); expect modulation, chromatic writing or quarter tones; do not name one maqam
- sections:
  - Section: verse: G low / Nahawand medium (fit 0.985)  [!] same notes also fit other tonics: Eb (0.99), D (0.99), Bb (0.99)  -> relative-mode ambiguity
  - Section: chorus: A low / Kurd low (fit 0.832)  [!] tonic/dominant split: A and D (a 4th/5th apart) score almost equally; the true tonic could be either
- melody-only cross-check (chords removed): A low / Kurd low (fit 0.771)
- full report: `work/elissa-2009-tesada-a-bemeen-02-aa-bali-habibi/report.md`
## 5. `elissa-2009-tesada-a-bemeen-03-min-gheir-mounasba` — Elissa — Elissa - 2009 Tesada'a Bemeen — "من غير مناسبه"
- file: `03.Min Gheir Mounasba.mp3` | duration 289.698s | declared key Em | tempo 71.0 | voice Vocal
- parse: 100% of bars
- pitch classes: E 26%, F# 18%, D 17%, G 15%, C 11%, B 6%
- tonic: E (low, margin 0.063) | cues: most-used note -> E; phrase endings -> B; tool key & chords* -> E (key) / E (commonest chord root); other voice -> E
- scale: Nahawand [natural minor / Aeolian] (fit 0.993, shape confidence medium, name_allowed=True) | tied: Bayati, Nahawand | 12-TET shadow of: Bayati
- candidate ghammaz: C (800c, 28% of phrase endings)
- flags: tonic/dominant split: E and B (a 4th/5th apart) score almost equally; the true tonic could be either | same notes also fit other tonics: B (0.99), C (0.99), D (0.99)  -> relative-mode ambiguity
- sections:
  - Section: verse: B low / Kurd medium (fit 1.0)  [!] same notes also fit other tonics: C (1.00), E (1.00)  -> relative-mode ambiguity
  - Section: chorus: E low / Nahawand medium (fit 0.969)  [!] same notes also fit other tonics: C (0.97), D (0.97), G (0.97)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): E low / Nahawand medium (fit 0.993)
- full report: `work/elissa-2009-tesada-a-bemeen-03-min-gheir-mounasba/report.md`
## 6. `elissa-2009-tesada-a-bemeen-04-amri-la-rabbi` — Elissa — Elissa - 2009 Tesada'a Bemeen — "امري لربي"
- file: `04.Amri La Rabbi.mp3` | duration 236.434s | declared key Bm | tempo 115.0 | voice Vocal
- parse: 100% of bars
- pitch classes: F# 24%, A 20%, B 17%, G 11%, D 11%, C# 9%
- tonic: F# (high, margin 0.423) | cues: most-used note -> F#; phrase endings -> F#; tool key & chords* -> B (key) / A (commonest chord root); other voice -> F#
- scale: Kurd [Phrygian] (fit 1.0, shape confidence medium, name_allowed=True) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- flags: same notes also fit other tonics: B (1.00), A (1.00), G (1.00)  -> relative-mode ambiguity
- sections:
  - Section: verse: F# low / Kurd medium (fit 1.0)  [!] same notes also fit other tonics: B (1.00), A (1.00), D (1.00)  -> relative-mode ambiguity
  - Section: chorus: F# high / Kurd medium (fit 1.0)  [!] same notes also fit other tonics: B (1.00), A (1.00), G (1.00)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): F# high / Kurd medium (fit 1.0)
- full report: `work/elissa-2009-tesada-a-bemeen-04-amri-la-rabbi/report.md`
## 7. `elissa-2009-tesada-a-bemeen-05-fi-shi-nkasar` — Elissa — Elissa - 2009 Tesada'a Bemeen — "في شي انكسر"
- file: `05.Fi Shi Nkasar.mp3` | duration 207.83s | declared key D#m | tempo 106.0 | voice Vocal
- parse: 100% of bars
- pitch classes: Bb 27%, F 17%, B 14%, Ab 13%, Eb 13%, F# 9%
- tonic: Bb (high, margin 0.179) | cues: most-used note -> Bb; phrase endings -> Bb; tool key & chords* -> Eb (key) / Eb (commonest chord root); other voice -> Bb
- scale: Kurd [Phrygian] (fit 1.0, shape confidence medium, name_allowed=True) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- candidate ghammaz: Eb (500c, 17% of phrase endings)
- flags: same notes also fit other tonics: Eb (1.00), B (1.00), F# (1.00)  -> relative-mode ambiguity
- sections:
  - Section: verse: Bb high / Kurd medium (fit 1.0)  [!] same notes also fit other tonics: Eb (1.00), B (1.00), F# (1.00)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): Bb high / Kurd medium (fit 1.0)
- full report: `work/elissa-2009-tesada-a-bemeen-05-fi-shi-nkasar/report.md`
## 8. `elissa-2009-tesada-a-bemeen-07-sallimli-aleh` — Elissa — Elissa - 2009 Tesada'a Bemeen — "سلملي عليه"
- file: `07.Sallimli Aleh.mp3` | duration 288.418s | declared key Bbm | tempo 137.0 | voice Vocal
- parse: 100% of bars
- pitch classes: F 22%, Eb 16%, Ab 15%, F# 14%, C 13%, C# 11%
- tonic: F (high, margin 0.247) | cues: most-used note -> F; phrase endings -> F; tool key & chords* -> Bb (key) / F (commonest chord root); other voice -> F
- scale: Kurd [Phrygian] (fit 1.0, shape confidence medium, name_allowed=True) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- candidate ghammaz: C (700c, 38% of phrase endings)
- flags: same notes also fit other tonics: Bb (1.00), Ab (1.00)  -> relative-mode ambiguity
- sections:
  - Section: chorus: F high / Kurd medium (fit 1.0)  [!] same notes also fit other tonics: Bb (1.00), Ab (1.00)  -> relative-mode ambiguity
  - Section: verse: F high / Kurd medium (fit 1.0)  [!] same notes also fit other tonics: Ab (1.00), Bb (1.00)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): F high / Kurd medium (fit 1.0)
- full report: `work/elissa-2009-tesada-a-bemeen-07-sallimli-aleh/report.md`
