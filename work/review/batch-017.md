# Maqam review — batch-017 (8 songs)

Read `skills/maqam-analysis/SKILL.md` before deciding. Hard rules:
- 12-TET ABC cannot prove quarter tones. Quarter-tone maqamat (Rast, Bayati, Saba, Sikah, Huzam, Iraq, Awj Ara, Suznek, Jiharkah, Bastanikar) are status `possible`, never `consistent`.
- If the analyzer says `name_allowed=false`, a scale is not identified, parse <95%, or pitch classes are too few: use `maqam_status="withheld"`.
- Confidence can be lowered, never raised above the tool's evidence.
- A tonic/dominant split must name the other tonic in `tonic_alternatives`.
- Never import outside knowledge of the song. Evidence is the ABC only.

Fill the sibling template, then run:
```bash
python3 scripts/review.py record --batch work/review/batch-017.json \
  --labels work/review/batch-017.labels.json
```

## 1. `fadl-shaker-11-fadl-shaker-yara-akhedny-ma-ak-2006-01-akhedny-ma-ak` — Fadl Shaker — 11.Fadl Shaker&Yara.Akhedny Ma'ak.2006 — "اخدني معاك"
- file: `01.Akhedny Ma'ak.mp3` | duration 314.674s | declared key Em | tempo 91.0 | voice Vocal
- parse: 100% of bars
- pitch classes: B 23%, A 23%, G 21%, C 11%, F# 9%, D 7%
- tonic: B (low, margin 0.04) | cues: most-used note -> B; phrase endings -> B; tool key & chords* -> E (key) / E (commonest chord root); other voice -> G
- scale: Kurd [Phrygian] (fit 1.0, shape confidence medium, name_allowed=True) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- candidate ghammaz: A (1000c, 15% of phrase endings)
- flags: tonic/dominant split: B and E (a 4th/5th apart) score almost equally; the true tonic could be either | same notes also fit other tonics: E (1.00), G (1.00), A (1.00)  -> relative-mode ambiguity
- sections:
  - Section: verse: E high / Nahawand medium (fit 1.0)  [!] same notes also fit other tonics: D (1.00), C (1.00)  -> relative-mode ambiguity
  - Section: chorus: B low / Kurd medium (fit 0.98)  [!] same notes also fit other tonics: G (0.98), C (0.98)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): B low / Kurd medium (fit 1.0)
- full report: `work/fadl-shaker-11-fadl-shaker-yara-akhedny-ma-ak-2006-01-akhedny-ma-ak/report.md`
## 2. `fadl-shaker-12-allah-alam-2006-01-enssa-ille-rah` — Fadl Shaker — 12.Allah Alam.2006 — "انسى اللي راح"
- file: `01.Enssa Ille Rah.mp3` | duration 263.027s | declared key Am | tempo 117.0 | voice Vocal
- parse: 100% of bars
- pitch classes: D 24%, E 22%, C 19%, A 12%, B 12%, F 6%
- tonic: A (low, margin 0.126) | cues: most-used note -> D; phrase endings -> C; tool key & chords* -> A (key) / A (commonest chord root); other voice -> E
- scale: Nahawand [natural minor / Aeolian] (fit 0.981, shape confidence medium, name_allowed=True) | tied: Bayati, Nahawand | 12-TET shadow of: Bayati
- candidate ghammaz: C (300c, 27% of phrase endings)
- flags: same notes also fit other tonics: E (0.98), C (0.98), D (0.98)  -> relative-mode ambiguity
- sections:
  - Section: verse: A low / Nahawand low (fit 0.928)  [!] same notes also fit other tonics: D (0.93), E (0.93)  -> relative-mode ambiguity
  - Section: chorus: C low / Ajam medium (fit 0.961)  [!] same notes also fit other tonics: A (0.98), E (0.98), D (0.98)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): A low / Nahawand medium (fit 0.981)
- full report: `work/fadl-shaker-12-allah-alam-2006-01-enssa-ille-rah/report.md`
## 3. `fadl-shaker-12-allah-alam-2006-02-elli-enta-shayfou` — Fadl Shaker — 12.Allah Alam.2006 — "اللي انت شايفه"
- file: `02.Elli Enta Shayfou.mp3` | duration 281.626s | declared key Am | tempo 87.0 | voice Vocal
- parse: 100% of bars
- pitch classes: B 26%, A 24%, C 17%, D 11%, G 10%, E 9%
- tonic: A (low, margin 0.327) | cues: most-used note -> B; phrase endings -> A; tool key & chords* -> A (key) / F (commonest chord root); other voice -> C
- scale: Nahawand [natural minor / Aeolian] (fit 1.0, shape confidence medium, name_allowed=True) | tied: Bayati, Nahawand | 12-TET shadow of: Bayati
- candidate ghammaz: F (800c, 27% of phrase endings)
- flags: same notes also fit other tonics: E (1.00), F (1.00)  -> relative-mode ambiguity
- sections:
  - Section: verse: A high / Nahawand medium (fit 0.98)  [!] same notes also fit other tonics: E (0.98), C (0.98), G (0.98)  -> relative-mode ambiguity
  - Section: chorus: A high / Nahawand medium (fit 1.0)  [!] same notes also fit other tonics: F (1.00), E (1.00), G (1.00)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): A low / Nahawand medium (fit 1.0)
- full report: `work/fadl-shaker-12-allah-alam-2006-02-elli-enta-shayfou/report.md`
## 4. `fadl-shaker-12-allah-alam-2006-03-allah-alam` — Fadl Shaker — 12.Allah Alam.2006 — "الله واعلم"
- file: `03.Allah Alam.mp3` | duration 261.59s | declared key Am | tempo 84.0 | voice Vocal
- parse: 100% of bars
- pitch classes: A 40%, B 34%, G 14%, C 8%, D 2%, F 1%
- tonic: G (low, margin 0.128) | cues: most-used note -> A; phrase endings -> G; tool key & chords* -> A (key) / F (commonest chord root); other voice -> F
- scale: (no standard maqam) [Mixolydian] (fit 0.94, shape confidence low, name_allowed=False) | tied: Rast, (no standard maqam) | 12-TET shadow of: Rast
- flags: same notes also fit other tonics: A (0.94), B (0.93), C (0.94)  -> relative-mode ambiguity | only 4 pitch classes in use: too few to identify a scale; the shape is under-determined
- sections:
  - Section: verse: A low / Nahawand low (fit 0.94)  [!] same notes also fit other tonics: G (0.94), F (0.94)  -> relative-mode ambiguity
  - Section: chorus: A medium / Nahawand medium (fit 0.96)  [!] same notes also fit other tonics: B (0.95), G (0.96), C (0.96)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): G low / (no standard maqam) low (fit 0.94)
- full report: `work/fadl-shaker-12-allah-alam-2006-03-allah-alam/report.md`
## 5. `fadl-shaker-12-allah-alam-2006-04-ana-bahhebbak` — Fadl Shaker — 12.Allah Alam.2006 — "انا بحبك"
- file: `04.Ana Bahhebbak.mp3` | duration 287.007s | declared key Cm | tempo 125.0 | voice Vocal
- parse: 100% of bars
- pitch classes: D 23%, C 19%, Bb 18%, Eb 13%, Ab 12%, G 8%
- tonic: C (low, margin 0.207) | cues: most-used note -> D; phrase endings -> C; tool key & chords* -> C (key) / C (commonest chord root); other voice -> G
- scale: Nahawand [natural minor / Aeolian] (fit 1.0, shape confidence medium, name_allowed=True) | tied: Bayati, Nahawand | 12-TET shadow of: Bayati
- candidate ghammaz: Ab (800c, 20% of phrase endings)
- flags: same notes also fit other tonics: G (1.00), Ab (1.00)  -> relative-mode ambiguity
- sections:
  - Section: intro: C low / Nahawand medium (fit 0.98)  [!] tonic/dominant split: C and G (a 4th/5th apart) score almost equally; the true tonic could be either
  - Section: verse: C low / Nahawand medium (fit 1.0)  [!] same notes also fit other tonics: Eb (1.00), F (1.00)  -> relative-mode ambiguity
  - Section: chorus: G low / Kurd medium (fit 0.98)  [!] tonic/dominant split: G and C (a 4th/5th apart) score almost equally; the true tonic could be either
- melody-only cross-check (chords removed): C low / Nahawand medium (fit 1.0)
- full report: `work/fadl-shaker-12-allah-alam-2006-04-ana-bahhebbak/report.md`
## 6. `fadl-shaker-12-allah-alam-2006-05-albi-ayesh` — Fadl Shaker — 12.Allah Alam.2006 — "قلبي عايش"
- file: `05.Albi Ayesh.mp3` | duration 339.383s | declared key Am | tempo 91.0 | voice Vocal
- parse: 100% of bars
- pitch classes: A 28%, B 19%, C 16%, E 12%, G 12%, F 8%
- tonic: A (high, margin 0.204) | cues: most-used note -> A; phrase endings -> C; tool key & chords* -> A (key) / E (commonest chord root); other voice -> A
- scale: Nahawand [natural minor / Aeolian] (fit 1.0, shape confidence medium, name_allowed=True) | tied: Bayati, Nahawand | 12-TET shadow of: Bayati
- candidate ghammaz: C (300c, 40% of phrase endings)
- flags: same notes also fit other tonics: C (1.00), F (1.00), E (1.00)  -> relative-mode ambiguity
- sections:
  - Section: verse: A high / Nahawand medium (fit 0.98)  [!] same notes also fit other tonics: E (0.98), C (0.98)  -> relative-mode ambiguity
  - Section: chorus: F low / (no standard maqam) medium (fit 1.0)  [!] same notes also fit other tonics: A (1.00), G (1.00)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): A high / Nahawand medium (fit 1.0)
- full report: `work/fadl-shaker-12-allah-alam-2006-05-albi-ayesh/report.md`
## 7. `fadl-shaker-12-allah-alam-2006-06-ghayeb-anni-leih` — Fadl Shaker — 12.Allah Alam.2006 — "غايب عني ليه"
- file: `06.Ghayeb Anni Leih.mp3` | duration 286.537s | declared key Cm | tempo 128.0 | voice Vocal
- parse: 100% of bars
- pitch classes: F 26%, G 24%, Eb 17%, D 15%, C 9%, Ab 4%
- tonic: G (low, margin 0.05) | cues: most-used note -> F; phrase endings -> D; tool key & chords* -> C (key) / C (commonest chord root); other voice -> G
- scale: Hijaz (fit 0.926, shape confidence low, name_allowed=True) | tied: Hijaz, Bayati, Kurd | 12-TET shadow of: Bayati
- candidate ghammaz: D (700c, 44% of phrase endings)
- flags: tonic/dominant split: G and D (a 4th/5th apart) score almost equally; the true tonic could be either | same notes also fit other tonics: F (0.93), C (0.93)  -> relative-mode ambiguity
- sections:
  - Section: verse: G low / Kurd medium (fit 1.0)  [!] tonic/dominant split: G and D (a 4th/5th apart) score almost equally; the true tonic could be either
  - Section: chorus: G low / Hijaz low (fit 0.925)  [!] tonic/dominant split: G and C (a 4th/5th apart) score almost equally; the true tonic could be either
- melody-only cross-check (chords removed): D low / Kurd low (fit 0.817)
- full report: `work/fadl-shaker-12-allah-alam-2006-06-ghayeb-anni-leih/report.md`
## 8. `fadl-shaker-12-allah-alam-2006-07-lahzet-lou-a` — Fadl Shaker — 12.Allah Alam.2006 — "لحظة لقاء"
- file: `07.Lahzet Lou'a.mp3` | duration 212.741s | declared key Em | tempo 105.0 | voice Vocal
- parse: 100% of bars
- pitch classes: G 33%, F# 18%, B 16%, A 14%, E 12%, D 4%
- tonic: G (medium, margin 0.027) | cues: most-used note -> G; phrase endings -> G; tool key & chords* -> E (key) / E (commonest chord root); other voice -> G
- scale: Ajam [major / Ionian] (fit 1.0, shape confidence medium, name_allowed=True) | tied: Rast, Ajam | 12-TET shadow of: Rast
- candidate ghammaz: B (400c, 11% of phrase endings)
- flags: same notes also fit other tonics: A (1.00), E (1.00), B (1.00)  -> relative-mode ambiguity
- sections:
  - Section: verse: B low / Kurd medium (fit 1.0)  [!] tonic/dominant split: B and E (a 4th/5th apart) score almost equally; the true tonic could be either
  - Section: chorus: A low / (no standard maqam) medium (fit 0.98)  [!] same notes also fit other tonics: E (0.98), G (0.98), B (0.98)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): G medium / Ajam medium (fit 1.0)
- full report: `work/fadl-shaker-12-allah-alam-2006-07-lahzet-lou-a/report.md`
