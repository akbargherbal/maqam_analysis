# Maqam review — batch-003 (8 songs)

Read `skills/maqam-analysis/SKILL.md` before deciding. Hard rules:
- 12-TET ABC cannot prove quarter tones. Quarter-tone maqamat (Rast, Bayati, Saba, Sikah, Huzam, Iraq, Awj Ara, Suznek, Jiharkah, Bastanikar) are status `possible`, never `consistent`.
- If the analyzer says `name_allowed=false`, a scale is not identified, parse <95%, or pitch classes are too few: use `maqam_status="withheld"`.
- Confidence can be lowered, never raised above the tool's evidence.
- A tonic/dominant split must name the other tonic in `tonic_alternatives`.
- Never import outside knowledge of the song. Evidence is the ABC only.

Fill the sibling template, then run:
```bash
python3 scripts/review.py record --batch work/review/batch-003.json \
  --labels work/review/batch-003.labels.json
```

## 1. `elissa-2000-wakherta-maak-08-sa-alna` — Elissa — Elissa - 2000 Wakherta Maak — "سألنا"
- file: `08.Sa'alna.mp3` | duration 287.376s | declared key Bm | tempo 145.0 | voice Vocal
- parse: 100% of bars
- pitch classes: E 22%, F# 19%, D 16%, G 16%, B 15%, C 10%
- tonic: F# (low, margin 0.049) | cues: most-used note -> E; phrase endings -> F#; tool key & chords* -> B (key) / B (commonest chord root); other voice -> B
- scale: Kurd [Phrygian] (fit 0.833, shape confidence low, name_allowed=False) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- candidate ghammaz: C (600c, 28% of phrase endings)
- flags: tonic/dominant split: F# and B (a 4th/5th apart) score almost equally; the true tonic could be either | same notes also fit other tonics: B (1.00), C (1.00), E (1.00)  -> relative-mode ambiguity | no single scale explains this material (best fit 0.83); expect modulation, chromatic writing or quarter tones; do not name one maqam
- sections:
  - Section: intro: B high / Nahawand low (fit 0.9)  [!] same notes also fit other tonics: A (0.90)  -> relative-mode ambiguity
  - Section: verse: F# low / Kurd low (fit 0.721)  [!] same notes also fit other tonics: B (0.98), C (0.98), G (0.98)  -> relative-mode ambiguity
  - Section: chorus: B low / Kurd medium (fit 0.96)  [!] same notes also fit other tonics: F# (0.94), E (0.96), D (0.96)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): F# low / Kurd low (fit 0.833)
- full report: `work/elissa-2000-wakherta-maak-08-sa-alna/report.md`
## 2. `elissa-2000-wakherta-maak-09-saharni-habibi` — Elissa — Elissa - 2000 Wakherta Maak — "سهرني حبيبي"
- file: `09.Saharni Habibi.mp3` | duration 275.491s | declared key G#m | tempo 131.0 | voice Vocal
- parse: 100% of bars
- pitch classes: Eb 27%, C# 20%, E 14%, B 13%, Bb 9%, Ab 7%
- tonic: Ab (low, margin 0.057) | cues: most-used note -> Eb; phrase endings -> Bb; tool key & chords* -> Ab (key) / Ab (commonest chord root); other voice -> C#
- scale: Nahawand [natural minor / Aeolian] (fit 0.901, shape confidence low, name_allowed=True) | tied: Bayati, Nahawand | 12-TET shadow of: Bayati
- candidate ghammaz: C# (500c, 22% of phrase endings)
- flags: tonic/dominant split: Ab and Eb (a 4th/5th apart) score almost equally; the true tonic could be either | same notes also fit other tonics: Eb (0.90), C# (0.90)  -> relative-mode ambiguity
- sections:
  - Section: verse: Ab low / Nahawand (raised 7th) medium (fit 0.997)  [!] tonic/dominant split: Ab and Eb (a 4th/5th apart) score almost equally; the true tonic could be either
  - Section: chorus: B low / Ajam medium (fit 0.96)  [!] same notes also fit other tonics: C# (0.96), E (0.96), F# (0.96)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): Ab low / Nahawand low (fit 0.901)
- full report: `work/elissa-2000-wakherta-maak-09-saharni-habibi/report.md`
## 3. `elissa-2000-wakherta-maak-10-chafouna-tneyn` — Elissa — Elissa - 2000 Wakherta Maak — "شافونا اتنين"
- file: `10.Chafouna Tneyn.mp3` | duration 263.526s | declared key F#m | tempo 128.0 | voice Vocal
- parse: 100% of bars
- pitch classes: C# 31%, F# 16%, D 14%, E 12%, A 12%, Ab 9%
- tonic: C# (low, margin 0.265) | cues: most-used note -> C#; phrase endings -> C#; tool key & chords* -> F# (key) / F# (commonest chord root); other voice -> F#
- scale: Kurd [Phrygian] (fit 1.0, shape confidence medium, name_allowed=True) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- flags: same notes also fit other tonics: F# (1.00), A (1.00), B (1.00)  -> relative-mode ambiguity
- sections:
  - Section: chorus: C# low / Kurd medium (fit 1.0)  [!] same notes also fit other tonics: F# (1.00), A (1.00), B (1.00)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): C# low / Kurd medium (fit 1.0)
- full report: `work/elissa-2000-wakherta-maak-10-chafouna-tneyn/report.md`
## 4. `elissa-2002-aayshalak-01-a-ayshalak` — Elissa — Elissa - 2002 Aayshalak — "عايشالك"
- file: `01. A ayshalak.mp3` | duration 278.26s | declared key Dm | tempo 127.0 | voice Vocal
- parse: 100% of bars
- pitch classes: F 23%, E 16%, D 16%, G 15%, A 12%, C 10%
- tonic: A (low, margin 0.291) | cues: most-used note -> F; phrase endings -> A; tool key & chords* -> D (key) / A (commonest chord root); other voice -> D
- scale: Kurd [Phrygian] (fit 1.0, shape confidence medium, name_allowed=True) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- flags: same notes also fit other tonics: D (1.00), F (1.00), G (1.00)  -> relative-mode ambiguity
- sections:
  - Section: verse: A low / Kurd medium (fit 1.0)  [!] same notes also fit other tonics: D (1.00), F (1.00), G (1.00)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): A low / Kurd medium (fit 1.0)
- full report: `work/elissa-2002-aayshalak-01-a-ayshalak/report.md`
## 5. `elissa-2002-aayshalak-02-ah-min-hawak` — Elissa — Elissa - 2002 Aayshalak — "اه من هواك"
- file: `02. Ah Min Hawak.mp3` | duration 284.059s | declared key Am | tempo 74.0 | voice Vocal
- parse: 100% of bars
- pitch classes: A 20%, E 17%, B 16%, F 14%, G 14%, C 12%
- tonic: A (high, margin 0.116) | cues: most-used note -> A; phrase endings -> E; tool key & chords* -> A (key) / A (commonest chord root); other voice -> A
- scale: Nahawand [natural minor / Aeolian] (fit 1.0, shape confidence medium, name_allowed=True) | tied: Bayati, Nahawand | 12-TET shadow of: Bayati
- candidate ghammaz: D (500c, 21% of phrase endings)
- flags: same notes also fit other tonics: E (1.00), D (1.00), F (1.00)  -> relative-mode ambiguity
- sections:
  - Section: verse: A low / Nahawand medium (fit 0.98)  [!] same notes also fit other tonics: D (0.98), E (0.98), F (0.98)  -> relative-mode ambiguity
  - Section: chorus: A low / Nahawand medium (fit 0.98)  [!] tonic/dominant split: A and E (a 4th/5th apart) score almost equally; the true tonic could be either
- melody-only cross-check (chords removed): A high / Nahawand medium (fit 1.0)
- full report: `work/elissa-2002-aayshalak-02-ah-min-hawak/report.md`
## 6. `elissa-2002-aayshalak-03-ajmal-ihssas` — Elissa — Elissa - 2002 Aayshalak — "اجمل احساس"
- file: `03. Ajmal Ihssas.mp3` | duration 354.981s | declared key Fm | tempo 86.0 | voice Vocal
- parse: 100% of bars
- pitch classes: C# 21%, F 18%, Eb 17%, C 15%, G 15%, Ab 11%
- tonic: C (low, margin 0.107) | cues: most-used note -> C#; phrase endings -> C; tool key & chords* -> F (key) / F (commonest chord root); other voice -> Ab
- scale: Kurd [Phrygian] (fit 1.0, shape confidence medium, name_allowed=True) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- candidate ghammaz: G (700c, 27% of phrase endings)
- flags: same notes also fit other tonics: F (1.00), C# (1.00)  -> relative-mode ambiguity
- sections:
  - Section: verse: C low / Kurd medium (fit 0.98)  [!] same notes also fit other tonics: C# (0.98), F (0.98)  -> relative-mode ambiguity
  - Section: chorus: C low / Kurd medium (fit 1.0)  [!] same notes also fit other tonics: F (1.00), Eb (1.00)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): C low / Kurd medium (fit 1.0)
- full report: `work/elissa-2002-aayshalak-03-ajmal-ihssas/report.md`
## 7. `elissa-2002-aayshalak-04-shaghilni` — Elissa — Elissa - 2002 Aayshalak — "شاغلني"
- file: `04. Shaghilni.mp3` | duration 252.869s | declared key Dm | tempo 95.0 | voice Vocal
- parse: 100% of bars
- pitch classes: D 29%, F 25%, E 18%, G 17%, C 10%, A 1%
- tonic: D (high, margin 0.516) | cues: most-used note -> D; phrase endings -> D; tool key & chords* -> D (key) / D (commonest chord root); other voice -> D
- scale: Nahawand [natural minor / Aeolian] (fit 0.959, shape confidence medium, name_allowed=True) | tied: Rast, Bayati, Nahawand, (no standard maqam) | 12-TET shadow of: Rast, Bayati
- candidate ghammaz: C (1000c, 16% of phrase endings)
- flags: same notes also fit other tonics: C (0.96), G (0.96), F (0.96)  -> relative-mode ambiguity
- sections:
  - Section: verse: D high / Nahawand medium (fit 0.958)  [!] same notes also fit other tonics: G (0.96), C (0.96), F (0.96)  -> relative-mode ambiguity
  - Section: chorus: D low / Nahawand medium (fit 0.96)  [!] same notes also fit other tonics: C (0.96), G (0.96), F (0.96)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): D high / Nahawand medium (fit 0.959)
- full report: `work/elissa-2002-aayshalak-04-shaghilni/report.md`
## 8. `elissa-2002-aayshalak-05-shiltak-min-albi` — Elissa — Elissa - 2002 Aayshalak — "شلتك من قلبي"
- file: `05. Shiltak min Albi.mp3` | duration 297.773s | declared key Dm | tempo 126.0 | voice Vocal
- parse: 100% of bars
- pitch classes: E 26%, F 20%, D 16%, G 14%, A 13%, C 4%
- tonic: D (low, margin 0.126) | cues: most-used note -> E; phrase endings -> F; tool key & chords* -> D (key) / A (commonest chord root); other voice -> G
- scale: Nahawand [natural minor / Aeolian] (fit 0.915, shape confidence low, name_allowed=True) | tied: Bayati, Nahawand, Nahawand (raised 7th) | 12-TET shadow of: Bayati
- candidate ghammaz: F (300c, 29% of phrase endings)
- flags: same notes also fit other tonics: A (0.91), F (0.91)  -> relative-mode ambiguity
- sections:
  - Section: verse: D low / Nahawand (raised 7th) low (fit 0.902)  [!] same notes also fit other tonics: A (0.90), G (0.90)  -> relative-mode ambiguity
  - Section: pre-chorus: Bb low / (no standard maqam) medium (fit 0.98)  [!] same notes also fit other tonics: A (0.98), D (0.98)  -> relative-mode ambiguity
  - Section: chorus: D low / Nahawand low (fit 0.924)  [!] same notes also fit other tonics: F (0.92), A (0.92), C (0.92)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): D low / Nahawand low (fit 0.915)
- full report: `work/elissa-2002-aayshalak-05-shiltak-min-albi/report.md`
