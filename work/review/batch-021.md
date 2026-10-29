# Maqam review — batch-021 (3 songs)

Read `skills/maqam-analysis/SKILL.md` before deciding. Hard rules:
- 12-TET ABC cannot prove quarter tones. Quarter-tone maqamat (Rast, Bayati, Saba, Sikah, Huzam, Iraq, Awj Ara, Suznek, Jiharkah, Bastanikar) are status `possible`, never `consistent`.
- If the analyzer says `name_allowed=false`, a scale is not identified, parse <95%, or pitch classes are too few: use `maqam_status="withheld"`.
- Confidence can be lowered, never raised above the tool's evidence.
- A tonic/dominant split must name the other tonic in `tonic_alternatives`.
- Never import outside knowledge of the song. Evidence is the ABC only.

Fill the sibling template, then run:
```bash
python3 scripts/review.py record --batch work/review/batch-021.json \
  --labels work/review/batch-021.labels.json
```

## 1. `fadl-shaker-15-the-best-of-al-rawae3-2010-14-ahawel` — Fadl Shaker — 15.The Best Of (Al Rawae3).2010 — "احاول"
- file: `14.Ahawel.mp3` | duration 338.184s | declared key Em | tempo 113.0 | voice Vocal
- parse: 100% of bars
- pitch classes: G 31%, F# 23%, E 22%, D 12%, B 4%, A 4%
- tonic: G (low, margin 0.085) | cues: most-used note -> G; phrase endings -> B; tool key & chords* -> E (key) / B (commonest chord root); other voice -> B
- scale: Ajam [major / Ionian] (fit 0.994, shape confidence medium, name_allowed=True) | tied: Rast, Ajam | 12-TET shadow of: Rast
- candidate ghammaz: E (900c, 24% of phrase endings)
- flags: same notes also fit other tonics: E (0.99), B (0.99), D (0.99)  -> relative-mode ambiguity
- sections:
  - Section: verse: G low / Ajam medium (fit 0.993)  [!] same notes also fit other tonics: B (0.99), E (0.99), D (0.99)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): G low / Ajam medium (fit 0.994)
- full report: `work/fadl-shaker-15-the-best-of-al-rawae3-2010-14-ahawel/report.md`
## 2. `fadl-shaker-15-the-best-of-al-rawae3-2010-15-ya-habibi-ta-ala` — Fadl Shaker — 15.The Best Of (Al Rawae3).2010 — "يا حبيبي تعال"
- file: `15.Ya Habibi Ta'ala.mp3` | duration 260.836s | declared key Am | tempo 127.0 | voice Vocal
- parse: 100% of bars
- pitch classes: C 22%, A 17%, B 17%, D 17%, E 12%, F 7%
- tonic: A (high, margin 0.176) | cues: most-used note -> C; phrase endings -> A; tool key & chords* -> A (key) / A (commonest chord root); other voice -> A
- scale: Nahawand [natural minor / Aeolian] (fit 1.0, shape confidence medium, name_allowed=True) | tied: Bayati, Nahawand | 12-TET shadow of: Bayati
- candidate ghammaz: E (700c, 27% of phrase endings)
- flags: same notes also fit other tonics: D (1.00), E (1.00), G (1.00)  -> relative-mode ambiguity
- sections:
  - Section: verse: A low / Nahawand medium (fit 1.0)  [!] same notes also fit other tonics: D (1.00), G (1.00), E (1.00)  -> relative-mode ambiguity
  - Section: chorus: A high / Nahawand medium (fit 1.0)  [!] same notes also fit other tonics: D (1.00), E (1.00), C (1.00)  -> relative-mode ambiguity
  - Section: bridge: E low / Kurd medium (fit 0.98)  [!] tonic/dominant split: E and A (a 4th/5th apart) score almost equally; the true tonic could be either
- melody-only cross-check (chords removed): A high / Nahawand medium (fit 1.0)
- full report: `work/fadl-shaker-15-the-best-of-al-rawae3-2010-15-ya-habibi-ta-ala/report.md`
## 3. `fadl-shaker-15-the-best-of-al-rawae3-2010-16-baya-el-oulob` — Fadl Shaker — 15.The Best Of (Al Rawae3).2010 — "بياع القلوب"
- file: `16.Baya' El Oulob.mp3` | duration 284.607s | declared key Gm | tempo 86.0 | voice Vocal
- parse: 100% of bars
- pitch classes: Bb 34%, C 22%, Ab 14%, G 14%, D 11%, F 3%
- tonic: G (high, margin 0.412) | cues: most-used note -> Bb; phrase endings -> G; tool key & chords* -> G (key) / G (commonest chord root); other voice -> G
- scale: Kurd [Phrygian] (fit 0.967, shape confidence medium, name_allowed=True) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- candidate ghammaz: Bb (300c, 12% of phrase endings)
- flags: same notes also fit other tonics: C (0.97), Bb (0.97), F (0.97)  -> relative-mode ambiguity
- sections:
  - Section: verse: G low / Kurd medium (fit 0.96)  [!] same notes also fit other tonics: C (0.96), Bb (0.96), Ab (0.96)  -> relative-mode ambiguity
  - Section: chorus: G high / Kurd low (fit 0.899)  [!] same notes also fit other tonics: Bb (0.90), C (0.90), Ab (0.90)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): G high / Kurd medium (fit 0.967)
- full report: `work/fadl-shaker-15-the-best-of-al-rawae3-2010-16-baya-el-oulob/report.md`
