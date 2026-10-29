# Maqam review — batch-008 (8 songs)

Read `skills/maqam-analysis/SKILL.md` before deciding. Hard rules:
- 12-TET ABC cannot prove quarter tones. Quarter-tone maqamat (Rast, Bayati, Saba, Sikah, Huzam, Iraq, Awj Ara, Suznek, Jiharkah, Bastanikar) are status `possible`, never `consistent`.
- If the analyzer says `name_allowed=false`, a scale is not identified, parse <95%, or pitch classes are too few: use `maqam_status="withheld"`.
- Confidence can be lowered, never raised above the tool's evidence.
- A tonic/dominant split must name the other tonic in `tonic_alternatives`.
- Never import outside knowledge of the song. Evidence is the ABC only.

Fill the sibling template, then run:
```bash
python3 scripts/review.py record --batch work/review/batch-008.json \
  --labels work/review/batch-008.labels.json
```

## 1. `elissa-2008-ayami-beek-02-khod-balak-alaya` — Elissa — Elissa - 2008 Ayami Beek — "خد بالك عليا"
- file: `02. Khod Balak Alaya.mp3` | duration 329.176s | declared key F#m | tempo 76.0 | voice Vocal
- parse: 100% of bars
- pitch classes: F# 36%, E 22%, D 17%, Ab 12%, C# 7%, B 4%
- tonic: C# (low, margin 0.101) | cues: most-used note -> F#; phrase endings -> C#; tool key & chords* -> F# (key) / F# (commonest chord root); other voice -> F#
- scale: Kurd [Phrygian] (fit 0.98, shape confidence medium, name_allowed=True) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- flags: tonic/dominant split: C# and F# (a 4th/5th apart) score almost equally; the true tonic could be either | same notes also fit other tonics: F# (0.98), D (0.98), E (0.98)  -> relative-mode ambiguity
- sections:
  - Section: verse: C# low / Kurd medium (fit 0.98)  [!] same notes also fit other tonics: F# (0.98), E (0.98), D (0.98)  -> relative-mode ambiguity
  - Section: chorus: D low / (no standard maqam) medium (fit 1.0)  [!] same notes also fit other tonics: C# (1.00), F# (1.00), E (1.00)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): C# low / Kurd medium (fit 0.98)
- full report: `work/elissa-2008-ayami-beek-02-khod-balak-alaya/report.md`
## 2. `elissa-2008-ayami-beek-03-betmon` — Elissa — Elissa - 2008 Ayami Beek — "بتمون"
- file: `03. Betmon.mp3` | duration 244.508s | declared key Fm | tempo 97.0 | voice Vocal
- parse: 100% of bars
- pitch classes: F 26%, G 17%, C# 16%, Eb 15%, C 12%, Ab 10%
- tonic: F (low, margin 0.028) | cues: most-used note -> F; phrase endings -> C; tool key & chords* -> F (key) / Bb (commonest chord root); other voice -> C
- scale: Nahawand [natural minor / Aeolian] (fit 1.0, shape confidence medium, name_allowed=True) | tied: Bayati, Nahawand | 12-TET shadow of: Bayati
- candidate ghammaz: C (700c, 73% of phrase endings)
- flags: tonic/dominant split: F and C (a 4th/5th apart) score almost equally; the true tonic could be either | same notes also fit other tonics: C (1.00), C# (1.00)  -> relative-mode ambiguity
- sections:
  - Section: verse: F low / Nahawand medium (fit 1.0)  [!] tonic/dominant split: F and C (a 4th/5th apart) score almost equally; the true tonic could be either
  - Section: chorus: F low / Nahawand medium (fit 1.0)  [!] tonic/dominant split: F and C (a 4th/5th apart) score almost equally; the true tonic could be either
- melody-only cross-check (chords removed): F low / Nahawand medium (fit 1.0)
- full report: `work/elissa-2008-ayami-beek-03-betmon/report.md`
## 3. `elissa-2008-ayami-beek-04-ya-alam` — Elissa — Elissa - 2008 Ayami Beek — "يا عالم"
- file: `04. Ya Alam.mp3` | duration 313.36s | declared key Am | tempo 107.0 | voice Vocal
- parse: 100% of bars
- pitch classes: A 28%, E 18%, G 17%, B 17%, F 10%, D 6%
- tonic: A (low, margin 0.054) | cues: most-used note -> A; phrase endings -> E; tool key & chords* -> A (key) / A (commonest chord root); other voice -> A
- scale: Nahawand [natural minor / Aeolian] (fit 1.0, shape confidence medium, name_allowed=True) | tied: Bayati, Nahawand | 12-TET shadow of: Bayati
- candidate ghammaz: E (700c, 40% of phrase endings)
- flags: tonic/dominant split: A and E (a 4th/5th apart) score almost equally; the true tonic could be either | same notes also fit other tonics: E (1.00), G (1.00)  -> relative-mode ambiguity
- sections:
  - Section: verse: A low / Nahawand medium (fit 1.0)  [!] same notes also fit other tonics: E (1.00), G (1.00)  -> relative-mode ambiguity
  - Section: chorus: E low / Kurd medium (fit 1.0)  [!] tonic/dominant split: E and A (a 4th/5th apart) score almost equally; the true tonic could be either
- melody-only cross-check (chords removed): A low / Nahawand medium (fit 1.0)
- full report: `work/elissa-2008-ayami-beek-04-ya-alam/report.md`
## 4. `elissa-2008-ayami-beek-05-law-ma-tegi` — Elissa — Elissa - 2008 Ayami Beek — "لو ما تيجي"
- file: `05. Law Ma Tegi.mp3` | duration 274.21s | declared key Am | tempo 88.0 | voice Vocal
- parse: 100% of bars
- pitch classes: E 27%, D 18%, F 16%, G 13%, C 12%, A 8%
- tonic: E (low, margin 0.109) | cues: most-used note -> E; phrase endings -> E; tool key & chords* -> A (key) / A (commonest chord root); other voice -> A
- scale: Kurd [Phrygian] (fit 1.0, shape confidence medium, name_allowed=True) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- candidate ghammaz: D (1000c, 23% of phrase endings)
- flags: tonic/dominant split: E and A (a 4th/5th apart) score almost equally; the true tonic could be either | same notes also fit other tonics: A (1.00), D (1.00), C (1.00)  -> relative-mode ambiguity
- sections:
  - Section: verse: E medium / Kurd medium (fit 0.98)  [!] same notes also fit other tonics: D (0.98), C (0.98), F (0.98)  -> relative-mode ambiguity
  - Section: pre-chorus: E low / Kurd medium (fit 1.0)  [!] tonic/dominant split: E and A (a 4th/5th apart) score almost equally; the true tonic could be either
  - Section: chorus: A low / Nahawand medium (fit 1.0)  [!] tonic/dominant split: A and E (a 4th/5th apart) score almost equally; the true tonic could be either
- melody-only cross-check (chords removed): E low / Kurd medium (fit 1.0)
- full report: `work/elissa-2008-ayami-beek-05-law-ma-tegi/report.md`
## 5. `elissa-2008-ayami-beek-06-mish-ktir-alayk` — Elissa — Elissa - 2008 Ayami Beek — "مش كثير عليك"
- file: `06. Mish Ktir Alayk.mp3` | duration 268.938s | declared key Em | tempo 123.0 | voice Vocal
- parse: 100% of bars
- pitch classes: E 23%, D 21%, F# 19%, G 15%, C 12%, B 6%
- tonic: E (low, margin 0.155) | cues: most-used note -> E; phrase endings -> F#; tool key & chords* -> E (key) / B (commonest chord root); other voice -> F#
- scale: Nahawand [natural minor / Aeolian] (fit 1.0, shape confidence medium, name_allowed=True) | tied: Bayati, Nahawand | 12-TET shadow of: Bayati
- candidate ghammaz: G (300c, 22% of phrase endings)
- flags: same notes also fit other tonics: B (1.00), G (1.00)  -> relative-mode ambiguity
- sections:
  - Section: verse: E low / Nahawand medium (fit 0.98)  [!] same notes also fit other tonics: B (0.98), D (0.98)  -> relative-mode ambiguity
  - Section: chorus: F# low / Kurd low (fit 0.886)  [!] same notes also fit other tonics: G (1.00), E (1.00), B (1.00)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): E low / Nahawand medium (fit 1.0)
- full report: `work/elissa-2008-ayami-beek-06-mish-ktir-alayk/report.md`
## 6. `elissa-2008-ayami-beek-07-adik-erift` — Elissa — Elissa - 2008 Ayami Beek — "اديك عرفت"
- file: `07. Adik Erift.mp3` | duration 290.601s | declared key D#m | tempo 68.0 | voice Vocal
- parse: 100% of bars
- pitch classes: F 29%, F# 21%, C# 15%, Eb 13%, B 8%, Bb 8%
- tonic: F (low, margin 0.027) | cues: most-used note -> F; phrase endings -> Bb; tool key & chords* -> Eb (key) / C# (commonest chord root); other voice -> F
- scale: Kurd [Phrygian] (fit 0.85, shape confidence low, name_allowed=False) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- candidate ghammaz: Bb (500c, 27% of phrase endings)
- flags: tonic/dominant split: F and Bb (a 4th/5th apart) score almost equally; the true tonic could be either | same notes also fit other tonics: Bb (1.00), Eb (1.00), B (1.00)  -> relative-mode ambiguity | no single scale explains this material (best fit 0.85); expect modulation, chromatic writing or quarter tones; do not name one maqam
- sections:
  - Section: verse: Bb low / Kurd medium (fit 0.98)  [!] same notes also fit other tonics: Eb (0.98), F# (0.98)  -> relative-mode ambiguity
  - Section: chorus: F low / Kurd low (fit 0.841)  [!] tonic/dominant split: F and Bb (a 4th/5th apart) score almost equally; the true tonic could be either
- melody-only cross-check (chords removed): F low / Kurd low (fit 0.85)
- full report: `work/elissa-2008-ayami-beek-07-adik-erift/report.md`
## 7. `elissa-2008-ayami-beek-08-ala-hobbak` — Elissa — Elissa - 2008 Ayami Beek — "على حبك"
- file: `08. Ala Hobbak.mp3` | duration 218.069s | declared key Fm | tempo 139.0 | voice Vocal
- parse: 100% of bars
- pitch classes: G 30%, F 26%, Eb 16%, Ab 15%, C# 5%, C 4%
- tonic: C (low, margin 0.003) | cues: most-used note -> G; phrase endings -> C; tool key & chords* -> F (key) / F (commonest chord root); other voice -> C
- scale: Kurd [Phrygian] (fit 1.0, shape confidence medium, name_allowed=True) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- candidate ghammaz: G (700c, 36% of phrase endings)
- flags: tonic/dominant split: C and F (a 4th/5th apart) score almost equally; the true tonic could be either | same notes also fit other tonics: F (1.00), Eb (1.00)  -> relative-mode ambiguity
- sections:
  - Section: verse: G medium / Kurd medium (fit 0.98)  [!] same notes also fit other tonics: F (0.98), C (0.98), Ab (0.98)  -> relative-mode ambiguity
  - Section: chorus: C low / Kurd medium (fit 0.98)  [!] same notes also fit other tonics: Eb (0.98), F (0.98), C# (0.98)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): C low / Kurd medium (fit 1.0)
- full report: `work/elissa-2008-ayami-beek-08-ala-hobbak/report.md`
## 8. `elissa-2008-ayami-beek-09-ana-bastaghrib-aleh` — Elissa — Elissa - 2008 Ayami Beek — "انا بستغرب"
- file: `09. Ana Bastaghrib Aleh.mp3` | duration 268.102s | declared key Em | tempo 68.0 | voice Vocal
- parse: 100% of bars
- pitch classes: E 28%, D 20%, F# 17%, G 15%, B 9%, C 6%
- tonic: E (high, margin 0.315) | cues: most-used note -> E; phrase endings -> E; tool key & chords* -> E (key) / B (commonest chord root); other voice -> G
- scale: Nahawand [natural minor / Aeolian] (fit 1.0, shape confidence medium, name_allowed=True) | tied: Bayati, Nahawand | 12-TET shadow of: Bayati
- candidate ghammaz: D (1000c, 11% of phrase endings)
- flags: same notes also fit other tonics: G (1.00), B (1.00), D (1.00)  -> relative-mode ambiguity
- sections:
  - Section: verse: E high / Nahawand medium (fit 0.98)  [!] same notes also fit other tonics: G (0.98), B (0.98)  -> relative-mode ambiguity
  - Section: chorus: B low / Kurd medium (fit 1.0)  [!] same notes also fit other tonics: D (1.00), E (1.00), C (1.00)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): E high / Nahawand medium (fit 1.0)
- full report: `work/elissa-2008-ayami-beek-09-ana-bastaghrib-aleh/report.md`
