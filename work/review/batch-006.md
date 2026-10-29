# Maqam review — batch-006 (8 songs)

Read `skills/maqam-analysis/SKILL.md` before deciding. Hard rules:
- 12-TET ABC cannot prove quarter tones. Quarter-tone maqamat (Rast, Bayati, Saba, Sikah, Huzam, Iraq, Awj Ara, Suznek, Jiharkah, Bastanikar) are status `possible`, never `consistent`.
- If the analyzer says `name_allowed=false`, a scale is not identified, parse <95%, or pitch classes are too few: use `maqam_status="withheld"`.
- Confidence can be lowered, never raised above the tool's evidence.
- A tonic/dominant split must name the other tonic in `tonic_alternatives`.
- Never import outside knowledge of the song. Evidence is the ABC only.

Fill the sibling template, then run:
```bash
python3 scripts/review.py record --batch work/review/batch-006.json \
  --labels work/review/batch-006.labels.json
```

## 1. `elissa-2004-ahla-donya-12-arably` — Elissa — Elissa - 2004 Ahla Donya — "قرب لي"
- file: `12.Arably.mp3` | duration 244.016s | declared key Em | tempo 125.0 | voice Vocal
- parse: 100% of bars
- pitch classes: G 28%, F# 19%, E 17%, A 14%, D 13%, F 3%
- tonic: G (high, margin 0.279) | cues: most-used note -> G; phrase endings -> G; tool key & chords* -> G (key) / D (commonest chord root); other voice -> F#
- scale: Rast (fit 0.799, shape confidence low, name_allowed=False) | tied: Rast | 12-TET shadow of: Rast
- candidate ghammaz: Eb (800c, 14% of phrase endings)
- flags: same notes also fit other tonics: D (0.79), E (0.79), A (0.80)  -> relative-mode ambiguity | no single scale explains this material (best fit 0.80); expect modulation, chromatic writing or quarter tones; do not name one maqam
- sections:
  - Section: chorus: G low / Ajam medium (fit 0.96)  [!] same notes also fit other tonics: E (0.96), D (0.96), F# (0.96)  -> relative-mode ambiguity
  - Section: verse: G low / Rast low (fit 0.765)  [!] same notes also fit other tonics: A (0.76), D (0.75)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): G high / Rast low (fit 0.799)
- full report: `work/elissa-2004-ahla-donya-12-arably/report.md`
## 2. `elissa-2004-ahla-donya-13-law-nergaa-sawa` — Elissa — Elissa - 2004 Ahla Donya — "لو نرجع سوا"
- file: `13.Law Nergaa Sawa.mp3` | duration 277.946s | declared key Em | tempo 125.0 | voice Vocal
- parse: 100% of bars
- pitch classes: E 27%, F# 25%, G 19%, B 9%, D 7%, C 7%
- tonic: E (low, margin 0.03) | cues: most-used note -> E; phrase endings -> B; tool key & chords* -> E (key) / E (commonest chord root); other voice -> B
- scale: Nahawand [natural minor / Aeolian] (fit 0.996, shape confidence medium, name_allowed=True) | tied: Bayati, Nahawand | 12-TET shadow of: Bayati
- candidate ghammaz: B (700c, 32% of phrase endings)
- flags: tonic/dominant split: E and B (a 4th/5th apart) score almost equally; the true tonic could be either | same notes also fit other tonics: B (1.00), C (1.00)  -> relative-mode ambiguity
- sections:
  - Section: verse: E low / Nahawand medium (fit 0.99)  [!] same notes also fit other tonics: B (0.99), C (0.99), D (0.99)  -> relative-mode ambiguity
  - Section: chorus: B low / Kurd medium (fit 1.0)  [!] same notes also fit other tonics: E (1.00), G (1.00)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): E low / Nahawand medium (fit 0.996)
- full report: `work/elissa-2004-ahla-donya-13-law-nergaa-sawa/report.md`
## 3. `elissa-2006-bastannak-01-bastanak` — Elissa — Elissa - 2006 Bastannak — "بستناك"
- file: `01.Bastanak.mp3` | duration 236.098s | declared key Em | tempo 99.0 | voice Vocal
- parse: 100% of bars
- pitch classes: B 27%, F# 15%, E 15%, G 13%, A 11%, C 11%
- tonic: E (low, margin 0.085) | cues: most-used note -> B; phrase endings -> F#; tool key & chords* -> E (key) / E (commonest chord root); other voice -> A
- scale: Nahawand [natural minor / Aeolian] (fit 0.909, shape confidence low, name_allowed=True) | tied: Bayati, Nahawand | 12-TET shadow of: Bayati
- candidate ghammaz: B (700c, 10% of phrase endings)
- flags: tonic/dominant split: E and B (a 4th/5th apart) score almost equally; the true tonic could be either | same notes also fit other tonics: B (0.91), G (0.91)  -> relative-mode ambiguity
- sections:
  - Section: verse: E low / Nahawand (raised 7th) low (fit 0.812)  [!] same notes also fit other tonics: B (0.81), C (0.80)  -> relative-mode ambiguity
  - Section: chorus: F# low / Kurd low (fit 0.786)  [!] tonic/dominant split: F# and B (a 4th/5th apart) score almost equally; the true tonic could be either
  - Section: bridge: G low / Ajam medium (fit 0.98)  [!] same notes also fit other tonics: B (0.98), E (0.98), C (0.98)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): E low / Nahawand low (fit 0.909)
- full report: `work/elissa-2006-bastannak-01-bastanak/report.md`
## 4. `elissa-2006-bastannak-02-kermalak` — Elissa — Elissa - 2006 Bastannak — "كرمالك"
- file: `02.Kermalak.mp3` | duration 298.557s | declared key F#m | tempo 125.0 | voice Vocal
- parse: 100% of bars
- pitch classes: F# 21%, Ab 20%, D 17%, E 17%, A 11%, C# 10%
- tonic: C# (low, margin 0.235) | cues: most-used note -> F#; phrase endings -> C#; tool key & chords* -> F# (key) / B (commonest chord root); other voice -> C#
- scale: Kurd [Phrygian] (fit 1.0, shape confidence medium, name_allowed=True) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- candidate ghammaz: F# (500c, 17% of phrase endings)
- flags: same notes also fit other tonics: F# (1.00), D (1.00), B (1.00)  -> relative-mode ambiguity
- sections:
  - Section: intro: C# low / Kurd medium (fit 1.0)  [!] same notes also fit other tonics: F# (1.00), D (1.00)  -> relative-mode ambiguity
  - Section: verse: C# low / Kurd medium (fit 0.96)  [!] same notes also fit other tonics: F# (0.96), D (0.96), E (0.96)  -> relative-mode ambiguity
  - Section: chorus: C# low / Kurd medium (fit 1.0)  [!] same notes also fit other tonics: F# (1.00), D (1.00), B (1.00)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): C# low / Kurd medium (fit 1.0)
- full report: `work/elissa-2006-bastannak-02-kermalak/report.md`
## 5. `elissa-2006-bastannak-03-fatet-sineen` — Elissa — Elissa - 2006 Bastannak — "فاتت سنين"
- file: `03.Fatet Sineen.mp3` | duration 245.92s | declared key Gm | tempo 76.0 | voice Vocal
- parse: 100% of bars
- pitch classes: F 32%, Eb 25%, G 23%, D 13%, A 5%, Bb 2%
- tonic: D (low, margin 0.297) | cues: most-used note -> F; phrase endings -> D; tool key & chords* -> G (key) / D (commonest chord root); other voice -> Bb
- scale: Kurd [Phrygian] (fit 0.96, shape confidence medium, name_allowed=True) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- flags: same notes also fit other tonics: G (0.96), Eb (0.96), F (0.96)  -> relative-mode ambiguity
- sections:
  - Section: verse: G low / Nahawand medium (fit 0.98)  [!] same notes also fit other tonics: Bb (0.98), F (0.98), D (0.98)  -> relative-mode ambiguity
  - Section: chorus: D low / Kurd medium (fit 0.96)  [!] same notes also fit other tonics: G (0.96), Eb (0.96), F (0.96)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): D low / Kurd medium (fit 0.96)
- full report: `work/elissa-2006-bastannak-03-fatet-sineen/report.md`
## 6. `elissa-2006-bastannak-04-zanbi-ana` — Elissa — Elissa - 2006 Bastannak — "ذنبي أنا"
- file: `04.Zanbi Ana.mp3` | duration 276.091s | declared key C#m | tempo 103.0 | voice Vocal
- parse: 100% of bars
- pitch classes: E 26%, F# 21%, Ab 17%, C# 12%, Eb 10%, B 8%
- tonic: E (low, margin 0.156) | cues: most-used note -> E; phrase endings -> E; tool key & chords* -> C# (key) / Ab (commonest chord root); other voice -> Ab
- scale: Ajam [major / Ionian] (fit 1.0, shape confidence medium, name_allowed=True) | tied: Rast, Ajam | 12-TET shadow of: Rast
- candidate ghammaz: Ab (400c, 15% of phrase endings)
- flags: same notes also fit other tonics: F# (1.00), Ab (1.00), C# (1.00)  -> relative-mode ambiguity
- sections:
  - Section: verse: E low / Ajam medium (fit 1.0)  [!] same notes also fit other tonics: Ab (1.00), F# (1.00), C# (1.00)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): E low / Ajam medium (fit 1.0)
- full report: `work/elissa-2006-bastannak-04-zanbi-ana/report.md`
## 7. `elissa-2006-bastannak-05-baaeh-ala-hissak` — Elissa — Elissa - 2006 Bastannak — "بعيش على هواك"
- file: `05.Baaeh Ala Hissak.mp3` | duration 261.933s | declared key Gm | tempo 104.0 | voice Vocal
- parse: 100% of bars
- pitch classes: G 29%, A 20%, D 18%, Eb 10%, C 8%, Bb 6%
- tonic: D (low, margin 0.359) | cues: most-used note -> G; phrase endings -> D; tool key & chords* -> G (key) / G (commonest chord root); other voice -> D
- scale: Kurd [Phrygian] (fit 0.91, shape confidence low, name_allowed=True) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- flags: same notes also fit other tonics: G (0.91), C (0.91)  -> relative-mode ambiguity
- sections:
  - Section: verse: D high / Hijaz medium (fit 1.0)  [!] same notes also fit other tonics: G (1.00), C (1.00)  -> relative-mode ambiguity
  - Section: chorus: D low / Kurd low (fit 0.909)  [!] same notes also fit other tonics: G (0.91), F (0.91)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): D low / Kurd low (fit 0.91)
- full report: `work/elissa-2006-bastannak-05-baaeh-ala-hissak/report.md`
## 8. `elissa-2006-bastannak-06-tlob-itmana` — Elissa — Elissa - 2006 Bastannak — "اطلب اتمنى"
- file: `06.Tlob Itmana.mp3` | duration 262.429s | declared key Dm | tempo 86.0 | voice Vocal
- parse: 100% of bars
- pitch classes: F 21%, G 21%, E 19%, D 14%, A 10%, C 9%
- tonic: A (low, margin 0.304) | cues: most-used note -> F; phrase endings -> A; tool key & chords* -> D (key) / A (commonest chord root); other voice -> A
- scale: Kurd [Phrygian] (fit 0.994, shape confidence medium, name_allowed=True) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- flags: same notes also fit other tonics: D (0.99), G (0.99), F (0.99)  -> relative-mode ambiguity
- sections:
  - Section: verse: A low / Kurd medium (fit 0.992)  [!] same notes also fit other tonics: D (0.99), F (0.99)  -> relative-mode ambiguity
  - Section: chorus: A low / Kurd medium (fit 1.0)  [!] same notes also fit other tonics: D (1.00), G (1.00), F (1.00)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): A low / Kurd medium (fit 0.994)
- full report: `work/elissa-2006-bastannak-06-tlob-itmana/report.md`
