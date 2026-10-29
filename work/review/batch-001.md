# Maqam review — batch-001 (8 songs)

Read `skills/maqam-analysis/SKILL.md` before deciding. Hard rules:
- 12-TET ABC cannot prove quarter tones. Quarter-tone maqamat (Rast, Bayati, Saba, Sikah, Huzam, Iraq, Awj Ara, Suznek, Jiharkah, Bastanikar) are status `possible`, never `consistent`.
- If the analyzer says `name_allowed=false`, a scale is not identified, parse <95%, or pitch classes are too few: use `maqam_status="withheld"`.
- Confidence can be lowered, never raised above the tool's evidence.
- A tonic/dominant split must name the other tonic in `tonic_alternatives`.
- Never import outside knowledge of the song. Evidence is the ABC only.

Fill the sibling template, then run:
```bash
python3 scripts/review.py record --batch work/review/batch-001.json \
  --labels work/review/batch-001.labels.json
```

## 1. `elissa-1998-baddy-doub-01-baddy-doub` — Elissa — Elissa - 1998 Baddy Doub — "بدي دوب"
- file: `01. Baddy Doub.mp3` | duration 236.8s | declared key Em | tempo 101.0 | voice Vocal
- parse: 100% of bars
- pitch classes: F# 32%, G 25%, E 20%, D 9%, C 7%, B 6%
- tonic: E (low, margin 0.019) | cues: most-used note -> F#; phrase endings -> F#; tool key & chords* -> E (key) / D (commonest chord root); other voice -> B
- scale: Nahawand [natural minor / Aeolian] (fit 0.98, shape confidence medium, name_allowed=True) | tied: Bayati, Nahawand | 12-TET shadow of: Bayati
- candidate ghammaz: B (700c, 46% of phrase endings)
- flags: same notes also fit other tonics: B (0.98), D (0.98)  -> relative-mode ambiguity
- sections:
  - Section: verse: F# low / Kurd low (fit 0.714)  [!] same notes also fit other tonics: E (0.98), B (0.98), C (0.98)  -> relative-mode ambiguity
  - Section: pre-chorus: E low / Nahawand medium (fit 1.0)  [!] tonic/dominant split: E and B (a 4th/5th apart) score almost equally; the true tonic could be either
  - Section: chorus: E low / Nahawand low (fit 0.94)  [!] same notes also fit other tonics: F# (0.93), G (0.94), D (0.94)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): F# low / Kurd low (fit 0.844)
- full report: `work/elissa-1998-baddy-doub-01-baddy-doub/report.md`
## 2. `elissa-1998-baddy-doub-02-da-lolak` — Elissa — Elissa - 1998 Baddy Doub — "ده لولاك"
- file: `02. Da Lolak.mp3` | duration 292.911s | declared key Fm | tempo 115.0 | voice Vocal
- parse: 100% of bars
- pitch classes: Eb 23%, F 22%, G 22%, C 16%, C# 11%, Bb 5%
- tonic: C (low, margin 0.115) | cues: most-used note -> Eb; phrase endings -> C; tool key & chords* -> F (key) / C (commonest chord root); other voice -> F
- scale: Kurd [Phrygian] (fit 0.967, shape confidence medium, name_allowed=True) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- candidate ghammaz: G (700c, 25% of phrase endings)
- flags: tonic/dominant split: C and F (a 4th/5th apart) score almost equally; the true tonic could be either | same notes also fit other tonics: F (0.97), Eb (0.97)  -> relative-mode ambiguity
- sections:
  - Section: chorus: C low / Kurd low (fit 0.946)  [!] same notes also fit other tonics: F (0.95), Eb (0.95)  -> relative-mode ambiguity
  - Section: verse: G low / Nahawand low (fit 0.785)  [!] same notes also fit other tonics: F (0.97), C (0.97), Eb (0.97)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): C low / Kurd medium (fit 0.967)
- full report: `work/elissa-1998-baddy-doub-02-da-lolak/report.md`
## 3. `elissa-1998-baddy-doub-03-helm-alahlam` — Elissa — Elissa - 1998 Baddy Doub — "حلم الاحلام"
- file: `03. Helm Alahlam.mp3` | duration 256.287s | declared key Dm | tempo 94.0 | voice Vocal
- parse: 100% of bars
- pitch classes: E 23%, D 20%, F 20%, C 17%, Bb 8%, A 7%
- tonic: D (low, margin 0.284) | cues: most-used note -> E; phrase endings -> D; tool key & chords* -> D (key) / C (commonest chord root); other voice -> A
- scale: Nahawand [natural minor / Aeolian] (fit 1.0, shape confidence medium, name_allowed=True) | tied: Bayati, Nahawand | 12-TET shadow of: Bayati
- candidate ghammaz: A (700c, 22% of phrase endings)
- flags: same notes also fit other tonics: A (1.00), C (1.00)  -> relative-mode ambiguity
- sections:
  - Section: chorus: D low / Nahawand medium (fit 0.98)  [!] same notes also fit other tonics: A (0.98), C (0.98), E (0.97)  -> relative-mode ambiguity
  - Section: verse: D medium / Nahawand medium (fit 0.98)  [!] same notes also fit other tonics: C (0.98), Bb (0.98)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): D low / Nahawand medium (fit 1.0)
- full report: `work/elissa-1998-baddy-doub-03-helm-alahlam/report.md`
## 4. `elissa-1998-baddy-doub-04-wenak-habiby` — Elissa — Elissa - 1998 Baddy Doub — "وينك حبيبي"
- file: `04. Wenak Habiby.mp3` | duration 278.204s | declared key Em | tempo 108.0 | voice Vocal
- parse: 100% of bars
- pitch classes: E 24%, D 21%, G 19%, F# 18%, C 7%, B 6%
- tonic: E (low, margin 0.07) | cues: most-used note -> E; phrase endings -> B; tool key & chords* -> E (key) / E (commonest chord root); other voice -> E
- scale: Nahawand [natural minor / Aeolian] (fit 1.0, shape confidence medium, name_allowed=True) | tied: Bayati, Nahawand | 12-TET shadow of: Bayati
- candidate ghammaz: B (700c, 64% of phrase endings)
- flags: tonic/dominant split: E and B (a 4th/5th apart) score almost equally; the true tonic could be either | same notes also fit other tonics: B (1.00), D (1.00), G (1.00)  -> relative-mode ambiguity
- sections:
  - Section: verse: B low / Kurd medium (fit 1.0)  [!] tonic/dominant split: B and E (a 4th/5th apart) score almost equally; the true tonic could be either
  - Section: chorus: E high / Nahawand medium (fit 1.0)  [!] same notes also fit other tonics: B (1.00), G (1.00), D (1.00)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): E low / Nahawand medium (fit 1.0)
- full report: `work/elissa-1998-baddy-doub-04-wenak-habiby/report.md`
## 5. `elissa-1998-baddy-doub-06-sho-ma-sar` — Elissa — Elissa - 1998 Baddy Doub — "شو ما صار"
- file: `06. Sho Ma Sar.mp3` | duration 214.465s | declared key Bm | tempo 124.0 | voice Vocal
- parse: 100% of bars
- pitch classes: E 30%, B 19%, D 15%, F# 13%, C 12%, G 7%
- tonic: B (high, margin 0.352) | cues: most-used note -> E; phrase endings -> B; tool key & chords* -> B (key) / B (commonest chord root); other voice -> B
- scale: Kurd [Phrygian] (fit 1.0, shape confidence medium, name_allowed=True) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- candidate ghammaz: E (500c, 8% of phrase endings)
- flags: same notes also fit other tonics: E (1.00), C (1.00)  -> relative-mode ambiguity
- sections:
  - Section: verse: B high / Kurd medium (fit 1.0)  [!] same notes also fit other tonics: E (1.00), C (1.00), D (1.00)  -> relative-mode ambiguity
  - Section: chorus: E low / Nahawand medium (fit 0.96)  [!] tonic/dominant split: E and B (a 4th/5th apart) score almost equally; the true tonic could be either
- melody-only cross-check (chords removed): B high / Kurd medium (fit 1.0)
- full report: `work/elissa-1998-baddy-doub-06-sho-ma-sar/report.md`
## 6. `elissa-1998-baddy-doub-07-zaalan` — Elissa — Elissa - 1998 Baddy Doub — "زعلان"
- file: `07. Zaalan.mp3` | duration 198.217s | declared key Em | tempo 94.0 | voice Vocal
- parse: 100% of bars
- pitch classes: F# 23%, G 22%, E 17%, D 14%, A 12%, B 7%
- tonic: E (low, margin 0.008) | cues: most-used note -> F#; phrase endings -> B; tool key & chords* -> E (key) / E (commonest chord root); other voice -> A
- scale: Nahawand [natural minor / Aeolian] (fit 1.0, shape confidence medium, name_allowed=True) | tied: Bayati, Nahawand | 12-TET shadow of: Bayati
- candidate ghammaz: A (500c, 38% of phrase endings)
- flags: tonic/dominant split: E and A (a 4th/5th apart) score almost equally; the true tonic could be either | same notes also fit other tonics: A (1.00), B (1.00), C (1.00)  -> relative-mode ambiguity
- sections:
  - Section: verse: A low / (no standard maqam) medium (fit 1.0)  [!] same notes also fit other tonics: C (1.00), E (1.00)  -> relative-mode ambiguity
  - Section: chorus: B low / Kurd medium (fit 1.0)  [!] tonic/dominant split: B and E (a 4th/5th apart) score almost equally; the true tonic could be either
- melody-only cross-check (chords removed): A low / (no standard maqam) medium (fit 1.0)
- full report: `work/elissa-1998-baddy-doub-07-zaalan/report.md`
## 7. `elissa-1998-baddy-doub-08-ghaly` — Elissa — Elissa - 1998 Baddy Doub — "غالي"
- file: `08. Ghaly.mp3` | duration 237.688s | declared key Dm | tempo 82.0 | voice Vocal
- parse: 100% of bars
- pitch classes: F 24%, A 21%, G 19%, Eb 12%, D 11%, Bb 10%
- tonic: D (low, margin 0.092) | cues: most-used note -> F; phrase endings -> F; tool key & chords* -> D (key) / D (commonest chord root); other voice -> D
- scale: Kurd [Phrygian] (fit 1.0, shape confidence medium, name_allowed=True) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- candidate ghammaz: F (300c, 34% of phrase endings)
- flags: same notes also fit other tonics: F (1.00), Eb (1.00), G (1.00)  -> relative-mode ambiguity
- sections:
  - Section: chorus: D low / Kurd medium (fit 1.0)  [!] same notes also fit other tonics: Eb (1.00), F (1.00)  -> relative-mode ambiguity
  - Section: verse: F low / (no standard maqam) medium (fit 0.96)  [!] same notes also fit other tonics: G (0.96), Eb (0.96)  -> relative-mode ambiguity
  - Section: bridge: D medium / Kurd medium (fit 1.0)  [!] same notes also fit other tonics: G (1.00), Bb (1.00)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): D low / Kurd medium (fit 1.0)
- full report: `work/elissa-1998-baddy-doub-08-ghaly/report.md`
## 8. `elissa-1998-baddy-doub-09-dalolak-mix` — Elissa — Elissa - 1998 Baddy Doub — "ده لولاك"
- file: `09. Dalolak Mix.mp3` | duration 292.859s | declared key Fm | tempo 112.0 | voice Vocal
- parse: 100% of bars
- pitch classes: Eb 24%, F 23%, G 22%, C 14%, C# 10%, Bb 4%
- tonic: C (low, margin 0.107) | cues: most-used note -> Eb; phrase endings -> C; tool key & chords* -> F (key) / C (commonest chord root); other voice -> F
- scale: Kurd [Phrygian] (fit 0.968, shape confidence medium, name_allowed=True) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- candidate ghammaz: G (700c, 25% of phrase endings)
- flags: tonic/dominant split: C and F (a 4th/5th apart) score almost equally; the true tonic could be either | same notes also fit other tonics: F (0.97), Eb (0.97)  -> relative-mode ambiguity
- sections:
  - Section: chorus: C low / Kurd low (fit 0.948)  [!] same notes also fit other tonics: F (0.95), Eb (0.95)  -> relative-mode ambiguity
  - Section: verse: G low / Nahawand low (fit 0.789)  [!] same notes also fit other tonics: F (0.97), C (0.97), Eb (0.97)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): C low / Kurd medium (fit 0.968)
- full report: `work/elissa-1998-baddy-doub-09-dalolak-mix/report.md`
