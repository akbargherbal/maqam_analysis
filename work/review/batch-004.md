# Maqam review — batch-004 (8 songs)

Read `skills/maqam-analysis/SKILL.md` before deciding. Hard rules:
- 12-TET ABC cannot prove quarter tones. Quarter-tone maqamat (Rast, Bayati, Saba, Sikah, Huzam, Iraq, Awj Ara, Suznek, Jiharkah, Bastanikar) are status `possible`, never `consistent`.
- If the analyzer says `name_allowed=false`, a scale is not identified, parse <95%, or pitch classes are too few: use `maqam_status="withheld"`.
- Confidence can be lowered, never raised above the tool's evidence.
- A tonic/dominant split must name the other tonic in `tonic_alternatives`.
- Never import outside knowledge of the song. Evidence is the ABC only.

Fill the sibling template, then run:
```bash
python3 scripts/review.py record --batch work/review/batch-004.json \
  --labels work/review/batch-004.labels.json
```

## 1. `elissa-2002-aayshalak-06-million-ahibbak` — Elissa — Elissa - 2002 Aayshalak — "مليون احبك"
- file: `06. Million Ahibbak.mp3` | duration 359.997s | declared key Am | tempo 135.0 | voice Vocal
- parse: 100% of bars
- pitch classes: E 38%, F 19%, D 18%, G 12%, A 7%, C 5%
- tonic: E (low, margin 0.001) | cues: most-used note -> E; phrase endings -> E; tool key & chords* -> A (key) / A (commonest chord root); other voice -> E
- scale: Kurd [Phrygian] (fit 0.965, shape confidence medium, name_allowed=True) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- candidate ghammaz: D (1000c, 26% of phrase endings)
- flags: tonic/dominant split: E and A (a 4th/5th apart) score almost equally; the true tonic could be either | same notes also fit other tonics: A (0.98), D (0.98), G (0.98)  -> relative-mode ambiguity
- sections:
  - Section: verse: E high / Kurd medium (fit 0.96)  [!] same notes also fit other tonics: D (0.96), G (0.96), F (0.96)  -> relative-mode ambiguity
  - Section: chorus: A low / Kurd medium (fit 0.98)  [!] same notes also fit other tonics: G (0.98), F (0.98)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): E medium / Kurd medium (fit 0.965)
- full report: `work/elissa-2002-aayshalak-06-million-ahibbak/report.md`
## 2. `elissa-2002-aayshalak-07-baada` — Elissa — Elissa - 2002 Aayshalak — "بعدا"
- file: `07. Baada.mp3` | duration 255.193s | declared key Gm | tempo 87.0 | voice Vocal
- parse: 100% of bars
- pitch classes: D 35%, Eb 14%, C 13%, F 12%, A 10%, Bb 9%
- tonic: D (low, margin 0.253) | cues: most-used note -> D; phrase endings -> D; tool key & chords* -> G (key) / D (commonest chord root); other voice -> Bb
- scale: Kurd [Phrygian] (fit 1.0, shape confidence medium, name_allowed=True) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- candidate ghammaz: A (700c, 12% of phrase endings)
- flags: same notes also fit other tonics: G (1.00), C (1.00)  -> relative-mode ambiguity
- sections:
  - Section: verse: D high / Kurd medium (fit 0.98)  [!] same notes also fit other tonics: G (0.98), F (0.98)  -> relative-mode ambiguity
  - Section: chorus: D low / Kurd medium (fit 0.98)  [!] same notes also fit other tonics: C (0.98), Bb (0.98), Eb (0.98)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): D low / Kurd medium (fit 1.0)
- full report: `work/elissa-2002-aayshalak-07-baada/report.md`
## 3. `elissa-2002-aayshalak-08-kilmit-hob` — Elissa — Elissa - 2002 Aayshalak — "كلمة حب"
- file: `08. Kilmit Hob.mp3` | duration 238.057s | declared key Cm | tempo 128.0 | voice Vocal
- parse: 100% of bars
- pitch classes: Eb 20%, G 20%, D 19%, F 16%, C 15%, Ab 8%
- tonic: C (low, margin 0.106) | cues: most-used note -> Eb; phrase endings -> G; tool key & chords* -> C (key) / C (commonest chord root); other voice -> C
- scale: Nahawand [natural minor / Aeolian] (fit 1.0, shape confidence medium, name_allowed=True) | tied: Bayati, Nahawand | 12-TET shadow of: Bayati
- candidate ghammaz: G (700c, 60% of phrase endings)
- flags: tonic/dominant split: C and G (a 4th/5th apart) score almost equally; the true tonic could be either | same notes also fit other tonics: G (1.00), Eb (1.00)  -> relative-mode ambiguity
- sections:
  - Section: verse: G low / Kurd medium (fit 1.0)  [!] tonic/dominant split: G and C (a 4th/5th apart) score almost equally; the true tonic could be either
  - Section: chorus: C low / Nahawand medium (fit 1.0)  [!] same notes also fit other tonics: F (1.00), G (1.00)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): C low / Nahawand medium (fit 1.0)
- full report: `work/elissa-2002-aayshalak-08-kilmit-hob/report.md`
## 4. `elissa-2002-aayshalak-09-la-trouh` — Elissa — Elissa - 2002 Aayshalak — "لا تروح"
- file: `09. La Trouh.mp3` | duration 246.913s | declared key Em | tempo 98.0 | voice Vocal
- parse: 100% of bars
- pitch classes: E 20%, D 19%, B 19%, C 15%, F# 15%, G 10%
- tonic: B (low, margin 0.062) | cues: most-used note -> E; phrase endings -> B; tool key & chords* -> E (key) / E (commonest chord root); other voice -> B
- scale: Kurd [Phrygian] (fit 1.0, shape confidence medium, name_allowed=True) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- candidate ghammaz: D (300c, 9% of phrase endings)
- flags: tonic/dominant split: B and E (a 4th/5th apart) score almost equally; the true tonic could be either | same notes also fit other tonics: E (1.00), C (1.00), D (1.00)  -> relative-mode ambiguity
- sections:
  - Section: verse: B medium / Kurd medium (fit 1.0)  [!] same notes also fit other tonics: C (1.00), E (1.00), D (1.00)  -> relative-mode ambiguity
  - Section: pre-chorus: B low / Kurd medium (fit 1.0)  [!] tonic/dominant split: B and E (a 4th/5th apart) score almost equally; the true tonic could be either
  - Section: chorus: B low / Kurd medium (fit 0.98)  [!] same notes also fit other tonics: E (0.98), G (0.98)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): B low / Kurd medium (fit 1.0)
- full report: `work/elissa-2002-aayshalak-09-la-trouh/report.md`
## 5. `elissa-2002-aayshalak-10-shou-el-hal` — Elissa — Elissa - 2002 Aayshalak — "شو الحل"
- file: `10. Shou El hal.mp3` | duration 255.376s | declared key Am | tempo 95.0 | voice Vocal
- parse: 100% of bars
- pitch classes: E 23%, D 20%, C 16%, F 15%, B 14%, A 8%
- tonic: E (low, margin 0.073) | cues: most-used note -> E; phrase endings -> E; tool key & chords* -> A (key) / A (commonest chord root); other voice -> D
- scale: Kurd [Phrygian] (fit 1.0, shape confidence medium, name_allowed=True) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- candidate ghammaz: B (700c, 40% of phrase endings)
- flags: tonic/dominant split: E and A (a 4th/5th apart) score almost equally; the true tonic could be either | same notes also fit other tonics: A (1.00), D (1.00)  -> relative-mode ambiguity
- sections:
  - Section: verse: E low / Kurd medium (fit 1.0)  [!] tonic/dominant split: E and A (a 4th/5th apart) score almost equally; the true tonic could be either
  - Section: chorus: B low / Kurd low (fit 0.751)  [!] tonic/dominant split: B and E (a 4th/5th apart) score almost equally; the true tonic could be either
- melody-only cross-check (chords removed): E low / Kurd medium (fit 1.0)
- full report: `work/elissa-2002-aayshalak-10-shou-el-hal/report.md`
## 6. `elissa-2004-ahla-donya-01-ergaa-lil-shou` — Elissa — Elissa - 2004 Ahla Donya — "ارجع للشوق"
- file: `01.Ergaa Lil Shou'.mp3` | duration 317.26s | declared key Fm | tempo 132.0 | voice Vocal
- parse: 100% of bars
- pitch classes: F 19%, F# 17%, Eb 17%, C# 14%, Ab 14%, Bb 10%
- tonic: F (high, margin 0.328) | cues: most-used note -> F; phrase endings -> F; tool key & chords* -> F (key) / F (commonest chord root); other voice -> F
- scale: Kurd [Phrygian] (fit 1.0, shape confidence medium, name_allowed=True) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- candidate ghammaz: Ab (300c, 33% of phrase endings)
- flags: same notes also fit other tonics: Ab (1.00), Bb (1.00), Eb (1.00)  -> relative-mode ambiguity
- sections:
  - Section: chorus: F high / Kurd medium (fit 1.0)  [!] same notes also fit other tonics: Ab (1.00), C# (1.00), Eb (1.00)  -> relative-mode ambiguity
  - Section: bridge: Bb low / Nahawand medium (fit 1.0)  [!] tonic/dominant split: Bb and F (a 4th/5th apart) score almost equally; the true tonic could be either
  - Section: verse: Bb low / Nahawand medium (fit 1.0)  [!] tonic/dominant split: Bb and F (a 4th/5th apart) score almost equally; the true tonic could be either
- melody-only cross-check (chords removed): F high / Kurd medium (fit 1.0)
- full report: `work/elissa-2004-ahla-donya-01-ergaa-lil-shou/report.md`
## 7. `elissa-2004-ahla-donya-02-ahla-donya` — Elissa — Elissa - 2004 Ahla Donya — "أحلى دنيا"
- file: `02.Ahla Donya.mp3` | duration 257.675s | declared key Fm | tempo 73.0 | voice Vocal
- parse: 100% of bars
- pitch classes: F 40%, Eb 30%, G 16%, C# 9%, C 4%, Ab 1%
- tonic: C (low, margin 0.282) | cues: most-used note -> F; phrase endings -> C; tool key & chords* -> F (key) / C (commonest chord root); other voice -> Ab
- scale: Kurd [Phrygian] (fit 0.96, shape confidence medium, name_allowed=True) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- candidate ghammaz: Eb (300c, 20% of phrase endings)
- flags: same notes also fit other tonics: F (0.96), Eb (0.96), C# (0.96)  -> relative-mode ambiguity
- sections:
  - Section: verse: F high / Nahawand low (fit 0.94)  [!] same notes also fit other tonics: C (0.94), G (0.94), Eb (0.94)  -> relative-mode ambiguity
  - Section: chorus: C low / Kurd medium (fit 0.96)  [!] same notes also fit other tonics: F (0.96), C# (0.96)  -> relative-mode ambiguity
  - Section: bridge: C low / Kurd medium (fit 0.96)  [!] same notes also fit other tonics: Eb (0.96), F (0.96), C# (0.96)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): C low / Kurd medium (fit 0.96)
- full report: `work/elissa-2004-ahla-donya-02-ahla-donya/report.md`
## 8. `elissa-2004-ahla-donya-03-kol-youm-beomre` — Elissa — Elissa - 2004 Ahla Donya — "كل يوم في عمري"
- file: `03.Kol Youm Beomre.mp3` | duration 323.321s | declared key Fm | tempo 105.0 | voice Vocal
- parse: 100% of bars
- pitch classes: F 28%, G 28%, Eb 14%, C# 12%, Ab 12%, C 3%
- tonic: G (low, margin 0.114) | cues: most-used note -> F; phrase endings -> G; tool key & chords* -> F (key) / C (commonest chord root); other voice -> C
- scale: Kurd [Phrygian] (fit 0.775, shape confidence low, name_allowed=False) | tied: Bayati, Kurd, Hijaz | 12-TET shadow of: Bayati
- flags: same notes also fit other tonics: Ab (0.97), F (0.97), C (0.97)  -> relative-mode ambiguity | no single scale explains this material (best fit 0.78); expect modulation, chromatic writing or quarter tones; do not name one maqam
- sections:
  - Section: chorus: G high / Kurd low (fit 0.806)  [!] same notes also fit other tonics: F (0.98), Ab (0.98), Eb (0.98)  -> relative-mode ambiguity
  - Section: verse: G low / Kurd low (fit 0.653)  [!] same notes also fit other tonics: Ab (0.88), F (0.88), Eb (0.88)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): G low / Kurd low (fit 0.775)
- full report: `work/elissa-2004-ahla-donya-03-kol-youm-beomre/report.md`
