# Maqam review — batch-007 (8 songs)

Read `skills/maqam-analysis/SKILL.md` before deciding. Hard rules:
- 12-TET ABC cannot prove quarter tones. Quarter-tone maqamat (Rast, Bayati, Saba, Sikah, Huzam, Iraq, Awj Ara, Suznek, Jiharkah, Bastanikar) are status `possible`, never `consistent`.
- If the analyzer says `name_allowed=false`, a scale is not identified, parse <95%, or pitch classes are too few: use `maqam_status="withheld"`.
- Confidence can be lowered, never raised above the tool's evidence.
- A tonic/dominant split must name the other tonic in `tonic_alternatives`.
- Never import outside knowledge of the song. Evidence is the ABC only.

Fill the sibling template, then run:
```bash
python3 scripts/review.py record --batch work/review/batch-007.json \
  --labels work/review/batch-007.labels.json
```

## 1. `elissa-2006-bastannak-07-taa` — Elissa — Elissa - 2006 Bastannak — "تعا"
- file: `07.Taa.mp3` | duration 276.013s | declared key Gm | tempo 128.0 | voice Vocal
- parse: 100% of bars
- pitch classes: G 23%, F 23%, D 16%, Eb 14%, A 8%, C 8%
- tonic: G (low, margin 0.06) | cues: most-used note -> G; phrase endings -> D; tool key & chords* -> G (key) / G (commonest chord root); other voice -> D
- scale: Nahawand [natural minor / Aeolian] (fit 0.988, shape confidence medium, name_allowed=True) | tied: Bayati, Nahawand | 12-TET shadow of: Bayati
- candidate ghammaz: F (1000c, 20% of phrase endings)
- flags: tonic/dominant split: G and D (a 4th/5th apart) score almost equally; the true tonic could be either | same notes also fit other tonics: D (0.99), F (0.99), C (0.99)  -> relative-mode ambiguity
- sections:
  - Section: verse: D high / Kurd medium (fit 0.983)  [!] same notes also fit other tonics: G (0.98), F (0.98), Eb (0.98)  -> relative-mode ambiguity
  - Section: chorus: G low / Nahawand medium (fit 0.992)  [!] same notes also fit other tonics: D (0.99), F (0.99), C (0.99)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): G low / Nahawand medium (fit 0.988)
- full report: `work/elissa-2006-bastannak-07-taa/report.md`
## 2. `elissa-2006-bastannak-08-matkhafch-minni` — Elissa — Elissa - 2006 Bastannak — "متخافش مني"
- file: `08.Matkhafch Minni.mp3` | duration 259.321s | declared key Fm | tempo 92.0 | voice Vocal
- parse: 100% of bars
- pitch classes: F 34%, C# 15%, C 15%, G 14%, Eb 10%, Ab 8%
- tonic: C (low, margin 0.045) | cues: most-used note -> F; phrase endings -> C; tool key & chords* -> F (key) / F (commonest chord root); other voice -> G
- scale: Kurd [Phrygian] (fit 0.992, shape confidence medium, name_allowed=True) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- candidate ghammaz: F (500c, 14% of phrase endings)
- flags: tonic/dominant split: C and F (a 4th/5th apart) score almost equally; the true tonic could be either | same notes also fit other tonics: F (0.99), Eb (0.99), Bb (0.99)  -> relative-mode ambiguity
- sections:
  - Section: verse: C medium / Kurd medium (fit 1.0)  [!] same notes also fit other tonics: F (1.00), Bb (1.00), C# (1.00)  -> relative-mode ambiguity
  - Section: chorus: F medium / Nahawand medium (fit 0.989)  [!] same notes also fit other tonics: C (0.99), Eb (0.99), C# (0.99)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): C low / Kurd medium (fit 0.992)
- full report: `work/elissa-2006-bastannak-08-matkhafch-minni/report.md`
## 3. `elissa-2006-bastannak-09-hikayti-maak` — Elissa — Elissa - 2006 Bastannak — "حكايتي معاك"
- file: `09.Hikayti Maak.mp3` | duration 318.697s | declared key Em | tempo 64.0 | voice Vocal
- parse: 100% of bars
- pitch classes: E 30%, F# 28%, G 15%, D 14%, C 6%, A 4%
- tonic: F# (low, margin 0.124) | cues: most-used note -> E; phrase endings -> F#; tool key & chords* -> E (key) / B (commonest chord root); other voice -> F#
- scale: Kurd [Phrygian] (fit 0.87, shape confidence low, name_allowed=False) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- flags: same notes also fit other tonics: E (1.00), G (1.00), B (1.00)  -> relative-mode ambiguity | no single scale explains this material (best fit 0.87); expect modulation, chromatic writing or quarter tones; do not name one maqam
- sections:
  - Section: chorus: F# low / Kurd low (fit 0.85)  [!] same notes also fit other tonics: E (1.00), G (1.00), B (1.00)  -> relative-mode ambiguity
  - Section: verse: G low / Ajam medium (fit 0.96)  [!] tonic/dominant split: G and D (a 4th/5th apart) score almost equally; the true tonic could be either
- melody-only cross-check (chords removed): F# low / Kurd low (fit 0.87)
- full report: `work/elissa-2006-bastannak-09-hikayti-maak/report.md`
## 4. `elissa-2006-bastannak-10-law-basset-eddamak` — Elissa — Elissa - 2006 Bastannak — "لو بصيت قدامك"
- file: `10.Law Basset Eddamak.mp3` | duration 245.528s | declared key Gm | tempo 75.0 | voice Vocal
- parse: 100% of bars
- pitch classes: D 23%, G 22%, F 17%, A 12%, Eb 10%, C 10%
- tonic: D (low, margin 0.13) | cues: most-used note -> D; phrase endings -> D; tool key & chords* -> G (key) / G (commonest chord root); other voice -> G
- scale: Kurd [Phrygian] (fit 1.0, shape confidence medium, name_allowed=True) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- candidate ghammaz: F (300c, 25% of phrase endings)
- flags: same notes also fit other tonics: G (1.00), F (1.00), Bb (1.00)  -> relative-mode ambiguity
- sections:
  - Section: verse: Bb low / Ajam medium (fit 1.0)  [!] same notes also fit other tonics: D (1.00), G (1.00), C (1.00)  -> relative-mode ambiguity
  - Section: chorus: D low / Kurd medium (fit 1.0)  [!] same notes also fit other tonics: F (1.00), G (1.00), Eb (1.00)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): D low / Kurd medium (fit 1.0)
- full report: `work/elissa-2006-bastannak-10-law-basset-eddamak/report.md`
## 5. `elissa-2006-bastannak-11-law-kan` — Elissa — Elissa - 2006 Bastannak — "لو كان"
- file: `11.Law kan.mp3` | duration 277.424s | declared key Gm | tempo 100.0 | voice Vocal
- parse: 100% of bars
- pitch classes: G 20%, D 18%, Eb 17%, A 14%, F 13%, C 9%
- tonic: G (high, margin 0.415) | cues: most-used note -> G; phrase endings -> G; tool key & chords* -> G (key) / G (commonest chord root); other voice -> G
- scale: Nahawand [natural minor / Aeolian] (fit 1.0, shape confidence medium, name_allowed=True) | tied: Bayati, Nahawand | 12-TET shadow of: Bayati
- candidate ghammaz: F (1000c, 14% of phrase endings)
- flags: same notes also fit other tonics: D (1.00), Eb (1.00), F (1.00)  -> relative-mode ambiguity
- sections:
  - Section: verse: G medium / Nahawand medium (fit 1.0)  [!] same notes also fit other tonics: D (1.00), F (1.00), C (1.00)  -> relative-mode ambiguity
  - Section: chorus: G low / Nahawand medium (fit 1.0)  [!] same notes also fit other tonics: Bb (1.00), D (1.00), Eb (1.00)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): G high / Nahawand medium (fit 1.0)
- full report: `work/elissa-2006-bastannak-11-law-kan/report.md`
## 6. `elissa-2006-bastannak-12-law-teaarafou` — Elissa — Elissa - 2006 Bastannak — "لو تعرفوه"
- file: `12.Law Teaarafou.mp3` | duration 254.958s | declared key Am | tempo 94.0 | voice Vocal
- parse: 100% of bars
- pitch classes: E 30%, F 22%, G 18%, D 12%, A 10%, B 4%
- tonic: E (low, margin 0.228) | cues: most-used note -> E; phrase endings -> E; tool key & chords* -> A (key) / E (commonest chord root); other voice -> A
- scale: Kurd [Phrygian] (fit 1.0, shape confidence medium, name_allowed=True) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- flags: same notes also fit other tonics: A (1.00), F (1.00), G (1.00)  -> relative-mode ambiguity
- sections:
  - Section: verse: E low / Kurd medium (fit 0.98)  [!] same notes also fit other tonics: A (0.98), G (0.98), D (0.98)  -> relative-mode ambiguity
  - Section: chorus: F low / (no standard maqam) medium (fit 1.0)  [!] same notes also fit other tonics: E (1.00), A (1.00), D (1.00)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): E low / Kurd medium (fit 1.0)
- full report: `work/elissa-2006-bastannak-12-law-teaarafou/report.md`
## 7. `elissa-2006-bastannak-13-kermalak-remix` — Elissa — Elissa - 2006 Bastannak — "كرمالك"
- file: `13.Kermalak [Remix].mp3` | duration 298.034s | declared key F#m | tempo 125.0 | voice Vocal
- parse: 100% of bars
- pitch classes: F# 22%, Ab 20%, D 17%, E 16%, C# 11%, A 10%
- tonic: F# (low, margin 0.01) | cues: most-used note -> F#; phrase endings -> C#; tool key & chords* -> F# (key) / F# (commonest chord root); other voice -> C#
- scale: Nahawand [natural minor / Aeolian] (fit 1.0, shape confidence medium, name_allowed=True) | tied: Bayati, Nahawand | 12-TET shadow of: Bayati
- candidate ghammaz: C# (700c, 50% of phrase endings)
- flags: tonic/dominant split: F# and C# (a 4th/5th apart) score almost equally; the true tonic could be either | same notes also fit other tonics: C# (1.00), D (1.00), E (1.00)  -> relative-mode ambiguity
- sections:
  - Section: verse: C# low / Kurd medium (fit 0.96)  [!] same notes also fit other tonics: F# (0.96), D (0.96), E (0.96)  -> relative-mode ambiguity
  - Section: chorus: C# low / Kurd medium (fit 1.0)  [!] tonic/dominant split: C# and F# (a 4th/5th apart) score almost equally; the true tonic could be either
- melody-only cross-check (chords removed): C# low / Kurd medium (fit 1.0)
- full report: `work/elissa-2006-bastannak-13-kermalak-remix/report.md`
## 8. `elissa-2008-ayami-beek-01-ayami-bik` — Elissa — Elissa - 2008 Ayami Beek — "ايامي بيك"
- file: `01. Ayami Bik.mp3` | duration 279.665s | declared key Fm | tempo 138.0 | voice Vocal
- parse: 100% of bars
- pitch classes: F 33%, G 19%, C# 15%, Ab 11%, Eb 11%, Bb 6%
- tonic: F (high, margin 0.107) | cues: most-used note -> F; phrase endings -> C; tool key & chords* -> F (key) / F (commonest chord root); other voice -> F
- scale: Nahawand [natural minor / Aeolian] (fit 1.0, shape confidence medium, name_allowed=True) | tied: Bayati, Nahawand | 12-TET shadow of: Bayati
- candidate ghammaz: C (700c, 27% of phrase endings)
- flags: same notes also fit other tonics: C (1.00), C# (1.00), Ab (1.00)  -> relative-mode ambiguity
- sections:
  - Section: verse: F low / Nahawand medium (fit 1.0)  [!] tonic/dominant split: F and C (a 4th/5th apart) score almost equally; the true tonic could be either
  - Section: chorus: C low / Kurd medium (fit 1.0)  [!] same notes also fit other tonics: F (1.00), Eb (1.00), Ab (1.00)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): F medium / Nahawand medium (fit 1.0)
- full report: `work/elissa-2008-ayami-beek-01-ayami-bik/report.md`
