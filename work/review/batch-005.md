# Maqam review — batch-005 (8 songs)

Read `skills/maqam-analysis/SKILL.md` before deciding. Hard rules:
- 12-TET ABC cannot prove quarter tones. Quarter-tone maqamat (Rast, Bayati, Saba, Sikah, Huzam, Iraq, Awj Ara, Suznek, Jiharkah, Bastanikar) are status `possible`, never `consistent`.
- If the analyzer says `name_allowed=false`, a scale is not identified, parse <95%, or pitch classes are too few: use `maqam_status="withheld"`.
- Confidence can be lowered, never raised above the tool's evidence.
- A tonic/dominant split must name the other tonic in `tonic_alternatives`.
- Never import outside knowledge of the song. Evidence is the ABC only.

Fill the sibling template, then run:
```bash
python3 scripts/review.py record --batch work/review/batch-005.json \
  --labels work/review/batch-005.labels.json
```

## 1. `elissa-2004-ahla-donya-04-khaleny-aeesh` — Elissa — Elissa - 2004 Ahla Donya — "خليني اعيش"
- file: `04.Khaleny Aeesh.mp3` | duration 288.526s | declared key Gm | tempo 68.0 | voice Vocal
- parse: 100% of bars
- pitch classes: Bb 27%, D 16%, A 15%, F 12%, G 11%, Eb 11%
- tonic: D (low, margin 0.362) | cues: most-used note -> Bb; phrase endings -> D; tool key & chords* -> G (key) / G (commonest chord root); other voice -> D
- scale: Kurd [Phrygian] (fit 0.985, shape confidence medium, name_allowed=True) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- flags: same notes also fit other tonics: G (0.99), Bb (0.99)  -> relative-mode ambiguity
- sections:
  - Section: verse: G low / Nahawand low (fit 0.898)  [!] tonic/dominant split: G and D (a 4th/5th apart) score almost equally; the true tonic could be either
  - Section: chorus: D low / Kurd medium (fit 1.0)  [!] same notes also fit other tonics: G (1.00), Bb (1.00), C (1.00)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): D low / Kurd medium (fit 0.985)
- full report: `work/elissa-2004-ahla-donya-04-khaleny-aeesh/report.md`
## 2. `elissa-2004-ahla-donya-05-been-el-ein` — Elissa — Elissa - 2004 Ahla Donya — "بين العين"
- file: `05. Been El Ein.mp3` | duration 254.593s | declared key Em | tempo 95.0 | voice Vocal
- parse: 100% of bars
- pitch classes: G 24%, F# 23%, E 23%, B 11%, D 10%, A 6%
- tonic: F# (low, margin 0.071) | cues: most-used note -> G; phrase endings -> F#; tool key & chords* -> E (key) / B (commonest chord root); other voice -> E
- scale: Kurd [Phrygian] (fit 0.904, shape confidence low, name_allowed=True) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- candidate ghammaz: B (500c, 14% of phrase endings)
- flags: same notes also fit other tonics: E (1.00), B (1.00), C (1.00)  -> relative-mode ambiguity
- sections:
  - Section: intro: F# low / Kurd medium (fit 0.98)  [!] same notes also fit other tonics: E (0.98), B (0.98), G (0.98)  -> relative-mode ambiguity
  - Section: verse: F# low / Kurd low (fit 0.884)  [!] same notes also fit other tonics: E (1.00), C (1.00), B (1.00)  -> relative-mode ambiguity
  - Section: chorus: B low / Kurd medium (fit 0.98)  [!] same notes also fit other tonics: E (0.98), D (0.98), G (0.98)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): F# low / Kurd low (fit 0.904)
- full report: `work/elissa-2004-ahla-donya-05-been-el-ein/report.md`
## 3. `elissa-2004-ahla-donya-06-hobak-wagaa` — Elissa — Elissa - 2004 Ahla Donya — "حبك وجع"
- file: `06.Hobak Wagaa.mp3` | duration 288.16s | declared key Gm | tempo 74.0 | voice Vocal
- parse: 100% of bars
- pitch classes: F 23%, G 20%, D 19%, C 14%, Bb 10%, Eb 10%
- tonic: G (low, margin 0.166) | cues: most-used note -> F; phrase endings -> G; tool key & chords* -> G (key) / G (commonest chord root); other voice -> F
- scale: Nahawand [natural minor / Aeolian] (fit 1.0, shape confidence medium, name_allowed=True) | tied: Bayati, Nahawand | 12-TET shadow of: Bayati
- candidate ghammaz: F (1000c, 31% of phrase endings)
- flags: same notes also fit other tonics: D (1.00), F (1.00), Eb (1.00)  -> relative-mode ambiguity
- sections:
  - Section: verse: G high / Nahawand medium (fit 1.0)  [!] same notes also fit other tonics: F (1.00), D (1.00), C (1.00)  -> relative-mode ambiguity
  - Section: chorus: D low / Kurd medium (fit 1.0)  [!] same notes also fit other tonics: G (1.00), Eb (1.00), F (1.00)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): G low / Nahawand medium (fit 1.0)
- full report: `work/elissa-2004-ahla-donya-06-hobak-wagaa/report.md`
## 4. `elissa-2004-ahla-donya-07-ad-mabashtaklak` — Elissa — Elissa - 2004 Ahla Donya — "قد ما بشتقلك"
- file: `07.Ad Mabashtaklak.mp3` | duration 228.679s | declared key F | tempo 125.0 | voice Vocal
- parse: 100% of bars
- pitch classes: F 25%, E 24%, G 18%, D 17%, A 8%, C 7%
- tonic: F (medium, margin 0.078) | cues: most-used note -> F; phrase endings -> D; tool key & chords* -> F (key) / F (commonest chord root); other voice -> F
- scale: Ajam [major / Ionian] (fit 0.978, shape confidence medium, name_allowed=True) | tied: Rast, Ajam | 12-TET shadow of: Rast
- candidate ghammaz: D (900c, 56% of phrase endings)
- flags: same notes also fit other tonics: D (0.98), E (0.97), G (0.98)  -> relative-mode ambiguity
- sections:
  - Section: verse: D low / Nahawand medium (fit 0.98)  [!] same notes also fit other tonics: F (0.98), E (0.97), G (0.98)  -> relative-mode ambiguity
  - Section: chorus: F low / Ajam medium (fit 0.976)  [!] same notes also fit other tonics: D (0.98), C (0.98), G (0.98)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): F medium / Ajam medium (fit 0.978)
- full report: `work/elissa-2004-ahla-donya-07-ad-mabashtaklak/report.md`
## 5. `elissa-2004-ahla-donya-08-kan-nifsy-aaraf` — Elissa — Elissa - 2004 Ahla Donya — "كان نفسي اعرف"
- file: `08. Kan Nifsy Aaraf.mp3` | duration 301.9s | declared key Em | tempo 74.0 | voice Vocal
- parse: 100% of bars
- pitch classes: E 33%, D 30%, F# 17%, C 8%, B 7%, G 5%
- tonic: E (low, margin 0.043) | cues: most-used note -> E; phrase endings -> B; tool key & chords* -> E (key) / E (commonest chord root); other voice -> E
- scale: Nahawand [natural minor / Aeolian] (fit 0.98, shape confidence medium, name_allowed=True) | tied: Bayati, Nahawand, Saba | 12-TET shadow of: Bayati, Saba
- candidate ghammaz: D (1000c, 43% of phrase endings)
- flags: tonic/dominant split: E and B (a 4th/5th apart) score almost equally; the true tonic could be either | same notes also fit other tonics: B (0.98), D (0.98)  -> relative-mode ambiguity
- sections:
  - Section: verse: E low / Nahawand medium (fit 0.98)  [!] tonic/dominant split: E and B (a 4th/5th apart) score almost equally; the true tonic could be either
  - Section: chorus: B low / Kurd medium (fit 0.98)  [!] tonic/dominant split: B and E (a 4th/5th apart) score almost equally; the true tonic could be either
- melody-only cross-check (chords removed): E low / Nahawand medium (fit 0.98)
- full report: `work/elissa-2004-ahla-donya-08-kan-nifsy-aaraf/report.md`
## 6. `elissa-2004-ahla-donya-09-zikra` — Elissa — Elissa - 2004 Ahla Donya — "ذكرى"
- file: `09.Zikra.mp3` | duration 304.016s | declared key Dm | tempo 125.0 | voice Vocal
- parse: 100% of bars
- pitch classes: E 21%, D 17%, F 17%, Bb 13%, A 12%, C 8%
- tonic: E (low, margin 0.06) | cues: most-used note -> E; phrase endings -> F; tool key & chords* -> D (key) / C (commonest chord root); other voice -> D
- scale: Kurd [Phrygian] (fit 0.649, shape confidence low, name_allowed=False) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- candidate ghammaz: Bb (600c, 24% of phrase endings)
- flags: same notes also fit other tonics: F (0.85), D (0.85), Bb (0.85)  -> relative-mode ambiguity | no single scale explains this material (best fit 0.65); expect modulation, chromatic writing or quarter tones; do not name one maqam
- sections:
  - Section: verse: F low / Ajam low (fit 0.929)  [!] same notes also fit other tonics: D (0.93), C (0.93), G (0.93)  -> relative-mode ambiguity
  - Section: chorus: E medium / Kurd low (fit 0.621)  [!] same notes also fit other tonics: F (0.84), D (0.84), Bb (0.84)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): E low / Kurd low (fit 0.649)
- full report: `work/elissa-2004-ahla-donya-09-zikra/report.md`
## 7. `elissa-2004-ahla-donya-10-erham-abi` — Elissa — Elissa - 2004 Ahla Donya — "ارحم قلبي"
- file: `10.Erham Abi.mp3` | duration 237.456s | declared key Dm | tempo 105.0 | voice Vocal
- parse: 100% of bars
- pitch classes: F 30%, G 22%, Eb 21%, D 14%, A 8%, Bb 4%
- tonic: D (low, margin 0.459) | cues: most-used note -> F; phrase endings -> D; tool key & chords* -> D (key) / D (commonest chord root); other voice -> G
- scale: Kurd [Phrygian] (fit 0.98, shape confidence medium, name_allowed=True) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- flags: same notes also fit other tonics: G (0.98), F (0.98), Eb (0.98)  -> relative-mode ambiguity
- sections:
  - Section: chorus: D low / Kurd medium (fit 0.98)  [!] same notes also fit other tonics: G (0.98), F (0.98), Eb (0.98)  -> relative-mode ambiguity
  - Section: verse: D medium / Kurd medium (fit 0.98)  [!] same notes also fit other tonics: G (0.98), F (0.98)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): D low / Kurd medium (fit 0.98)
- full report: `work/elissa-2004-ahla-donya-10-erham-abi/report.md`
## 8. `elissa-2004-ahla-donya-11-gowaya-leek` — Elissa — Elissa - 2004 Ahla Donya — "جوايا ليك"
- file: `11.Gowaya Leek.mp3` | duration 275.909s | declared key D#m | tempo 78.0 | voice Vocal
- parse: 100% of bars
- pitch classes: F 24%, F# 23%, C# 14%, Eb 13%, Ab 9%, Bb 8%
- tonic: F (low, margin 0.046) | cues: most-used note -> F; phrase endings -> Bb; tool key & chords* -> Eb (key) / Bb (commonest chord root); other voice -> F
- scale: Kurd [Phrygian] (fit 0.848, shape confidence low, name_allowed=False) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- candidate ghammaz: Bb (500c, 38% of phrase endings)
- flags: tonic/dominant split: F and Bb (a 4th/5th apart) score almost equally; the true tonic could be either | same notes also fit other tonics: Bb (1.00), Eb (1.00), F# (1.00)  -> relative-mode ambiguity | no single scale explains this material (best fit 0.85); expect modulation, chromatic writing or quarter tones; do not name one maqam
- sections:
  - Section: chorus: Bb low / Kurd medium (fit 1.0)  [!] same notes also fit other tonics: Eb (1.00), F# (1.00)  -> relative-mode ambiguity
  - Section: verse: F high / Kurd low (fit 0.853)  [!] same notes also fit other tonics: Eb (1.00), Bb (1.00), Ab (1.00)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): F low / Kurd low (fit 0.848)
- full report: `work/elissa-2004-ahla-donya-11-gowaya-leek/report.md`
