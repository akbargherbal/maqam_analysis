# Maqam review — batch-012 (8 songs)

Read `skills/maqam-analysis/SKILL.md` before deciding. Hard rules:
- 12-TET ABC cannot prove quarter tones. Quarter-tone maqamat (Rast, Bayati, Saba, Sikah, Huzam, Iraq, Awj Ara, Suznek, Jiharkah, Bastanikar) are status `possible`, never `consistent`.
- If the analyzer says `name_allowed=false`, a scale is not identified, parse <95%, or pitch classes are too few: use `maqam_status="withheld"`.
- Confidence can be lowered, never raised above the tool's evidence.
- A tonic/dominant split must name the other tonic in `tonic_alternatives`.
- Never import outside knowledge of the song. Evidence is the ABC only.

Fill the sibling template, then run:
```bash
python3 scripts/review.py record --batch work/review/batch-012.json \
  --labels work/review/batch-012.labels.json
```

## 1. `fadl-shaker-01-walla-zaman-1998-01-meta-habibi` — Fadl Shaker — 01.Walla Zaman.1998 — "متى حبيبي متى"
- file: `01.Meta Habibi.mp3` | duration 280.007s | declared key Cm | tempo 94.0 | voice Vocal
- parse: 100% of bars
- pitch classes: Bb 24%, C 24%, D 21%, G 15%, Ab 14%, Eb 2%
- tonic: G (low, margin 0.312) | cues: most-used note -> Bb; phrase endings -> G; tool key & chords* -> C (key) / G (commonest chord root); other voice -> G
- scale: Kurd [Phrygian] (fit 0.98, shape confidence medium, name_allowed=True) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- candidate ghammaz: D (700c, 8% of phrase endings)
- flags: same notes also fit other tonics: C (0.98), Bb (0.98)  -> relative-mode ambiguity
- sections:
  - Section: verse: G low / Kurd medium (fit 0.96)  [!] same notes also fit other tonics: C (0.96), Bb (0.96)  -> relative-mode ambiguity
  - Section: chorus: G low / Kurd medium (fit 0.98)  [!] same notes also fit other tonics: C (0.98), Bb (0.98)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): G low / Kurd medium (fit 0.98)
- full report: `work/fadl-shaker-01-walla-zaman-1998-01-meta-habibi/report.md`
## 2. `fadl-shaker-01-walla-zaman-1998-04-kul-el-helween` — Fadl Shaker — 01.Walla Zaman.1998 — "كل الحلوين"
- file: `04.Kul El Helween.mp3` | duration 355.605s | declared key Gm | tempo 95.0 | voice Vocal
- parse: 100% of bars
- pitch classes: C 25%, Bb 18%, G 17%, D 16%, Eb 10%, Ab 7%
- tonic: G (high, margin 0.318) | cues: most-used note -> C; phrase endings -> G; tool key & chords* -> G (key) / G (commonest chord root); other voice -> G
- scale: Kurd [Phrygian] (fit 0.981, shape confidence medium, name_allowed=True) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- candidate ghammaz: C (500c, 10% of phrase endings)
- flags: same notes also fit other tonics: Bb (0.98), C (0.98), Ab (0.98)  -> relative-mode ambiguity
- sections:
  - Section: verse: G high / Kurd low (fit 0.912)  [!] same notes also fit other tonics: C (0.91), D (0.90), Bb (0.91)  -> relative-mode ambiguity
  - Section: chorus: G low / Kurd medium (fit 1.0)  [!] same notes also fit other tonics: Bb (1.00), Ab (1.00), C (1.00)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): G high / Kurd medium (fit 0.981)
- full report: `work/fadl-shaker-01-walla-zaman-1998-04-kul-el-helween/report.md`
## 3. `fadl-shaker-01-walla-zaman-1998-05-walla-zaman` — Fadl Shaker — 01.Walla Zaman.1998 — "والله زمان"
- file: `05.Walla Zaman.mp3` | duration 320.705s | declared key Am | tempo 95.0 | voice Vocal
- parse: 100% of bars
- pitch classes: C 26%, A 22%, Bb 21%, D 21%, B 4%, G 4%
- tonic: A (low, margin 0.405) | cues: most-used note -> C; phrase endings -> A; tool key & chords* -> A (key) / A (commonest chord root); other voice -> C
- scale: Kurd [Phrygian] (fit 0.895, shape confidence low, name_allowed=False) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- flags: same notes also fit other tonics: D (0.89), C (0.89), G (0.89)  -> relative-mode ambiguity | no single scale explains this material (best fit 0.89); expect modulation, chromatic writing or quarter tones; do not name one maqam
- sections:
  - Section: chorus: A low / Kurd low (fit 0.854)  [!] same notes also fit other tonics: D (0.85), C (0.85), Bb (0.85)  -> relative-mode ambiguity
  - Section: verse: A high / Kurd medium (fit 0.98)  [!] same notes also fit other tonics: G (0.98), C (0.98), D (0.98)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): A low / Kurd low (fit 0.895)
- full report: `work/fadl-shaker-01-walla-zaman-1998-05-walla-zaman/report.md`
## 4. `fadl-shaker-02-bayya-a-el-qeloub-1999-01-esheqtak` — Fadl Shaker — 02.Bayya'a El Qeloub.1999 — "عشقتك"
- file: `01.Esheqtak.mp3` | duration 312.581s | declared key Gm | tempo 150.0 | voice Vocal
- parse: 100% of bars
- pitch classes: Bb 20%, A 20%, D 18%, G 18%, C 17%, B 3%
- tonic: G (high, margin 0.321) | cues: most-used note -> Bb; phrase endings -> G; tool key & chords* -> G (key) / G (commonest chord root); other voice -> G
- scale: Nahawand (raised 7th) [harmonic minor] (fit 0.878, shape confidence low, name_allowed=False) | tied: Nahawand (raised 7th)
- candidate ghammaz: D (700c, 20% of phrase endings)
- flags: same notes also fit other tonics: D (0.88), A (0.85), C (0.88)  -> relative-mode ambiguity | no single scale explains this material (best fit 0.88); expect modulation, chromatic writing or quarter tones; do not name one maqam
- sections:
  - Section: verse: G low / Nahawand (raised 7th) medium (fit 0.969)  [!] tonic/dominant split: G and D (a 4th/5th apart) score almost equally; the true tonic could be either
  - Section: chorus: G medium / Nahawand (raised 7th) low (fit 0.857)  [!] same notes also fit other tonics: D (0.86), A (0.84), C (0.86)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): G high / Nahawand (raised 7th) low (fit 0.878)
- full report: `work/fadl-shaker-02-bayya-a-el-qeloub-1999-01-esheqtak/report.md`
## 5. `fadl-shaker-02-bayya-a-el-qeloub-1999-02-bayya-a-el-qeloub` — Fadl Shaker — 02.Bayya'a El Qeloub.1999 — "بياع القلوب"
- file: `02.Bayya'a El Qeloub.mp3` | duration 284.212s | declared key Gm | tempo 86.0 | voice Vocal
- parse: 100% of bars
- pitch classes: Bb 34%, C 21%, Ab 15%, G 14%, D 12%, Eb 2%
- tonic: G (high, margin 0.434) | cues: most-used note -> Bb; phrase endings -> G; tool key & chords* -> G (key) / G (commonest chord root); other voice -> G
- scale: Kurd [Phrygian] (fit 0.95, shape confidence medium, name_allowed=True) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- candidate ghammaz: Bb (300c, 7% of phrase endings)
- flags: same notes also fit other tonics: C (0.95), Bb (0.95)  -> relative-mode ambiguity
- sections:
  - Section: verse: G low / Kurd medium (fit 0.958)  [!] same notes also fit other tonics: C (0.96), Bb (0.96)  -> relative-mode ambiguity
  - Section: chorus: G low / Kurd medium (fit 0.961)  [!] same notes also fit other tonics: C (0.96), Bb (0.96)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): G high / Kurd medium (fit 0.95)
- full report: `work/fadl-shaker-02-bayya-a-el-qeloub-1999-02-bayya-a-el-qeloub/report.md`
## 6. `fadl-shaker-02-bayya-a-el-qeloub-1999-03-eyouno-el-soud` — Fadl Shaker — 02.Bayya'a El Qeloub.1999 — "عيونه سود"
- file: `03.Eyouno El Soud.mp3` | duration 313.287s | declared key Cm | tempo 94.0 | voice Vocal
- parse: 100% of bars
- pitch classes: Bb 30%, C 30%, Ab 14%, D 12%, G 10%, Eb 3%
- tonic: G (low, margin 0.106) | cues: most-used note -> Bb; phrase endings -> G; tool key & chords* -> C (key) / G (commonest chord root); other voice -> G
- scale: Kurd [Phrygian] (fit 0.98, shape confidence medium, name_allowed=True) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- candidate ghammaz: Bb (300c, 43% of phrase endings)
- flags: tonic/dominant split: G and C (a 4th/5th apart) score almost equally; the true tonic could be either | same notes also fit other tonics: C (0.98), Bb (0.98), Ab (0.98)  -> relative-mode ambiguity
- sections:
  - Section: verse: G low / Kurd medium (fit 0.98)  [!] tonic/dominant split: G and C (a 4th/5th apart) score almost equally; the true tonic could be either
  - Section: chorus: G low / Kurd medium (fit 0.96)  [!] same notes also fit other tonics: C (0.96), Ab (0.96), Bb (0.96)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): G low / Kurd medium (fit 0.98)
- full report: `work/fadl-shaker-02-bayya-a-el-qeloub-1999-03-eyouno-el-soud/report.md`
## 7. `fadl-shaker-02-bayya-a-el-qeloub-1999-05-ewa-a-tesada-ny` — Fadl Shaker — 02.Bayya'a El Qeloub.1999 — "اوعى تصدقني"
- file: `05.Ewa'a Tesada'ny.mp3` | duration 285.283s | declared key C#m | tempo 90.0 | voice Vocal
- parse: 100% of bars
- pitch classes: C# 20%, A 20%, F# 17%, B 16%, Ab 12%, E 11%
- tonic: C# (high, margin 0.156) | cues: most-used note -> C#; phrase endings -> C#; tool key & chords* -> C# (key) / C# (commonest chord root); other voice -> Ab
- scale: Nahawand [natural minor / Aeolian] (fit 0.955, shape confidence medium, name_allowed=True) | tied: Bayati, Nahawand | 12-TET shadow of: Bayati
- candidate ghammaz: E (300c, 28% of phrase endings)
- flags: same notes also fit other tonics: Ab (0.96), F# (0.96), A (0.96)  -> relative-mode ambiguity
- sections:
  - Section: verse: C# low / Nahawand medium (fit 0.97)  [!] tonic/dominant split: C# and F# (a 4th/5th apart) score almost equally; the true tonic could be either
  - Section: chorus: C# high / Nahawand low (fit 0.946)  [!] same notes also fit other tonics: Ab (0.95), A (0.95), E (0.95)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): C# high / Nahawand medium (fit 0.955)
- full report: `work/fadl-shaker-02-bayya-a-el-qeloub-1999-05-ewa-a-tesada-ny/report.md`
## 8. `fadl-shaker-02-bayya-a-el-qeloub-1999-06-awel-hob` — Fadl Shaker — 02.Bayya'a El Qeloub.1999 — "اول حب"
- file: `06.Awel Hob.mp3` | duration 343.771s | declared key Gm | tempo 92.0 | voice Vocal
- parse: 100% of bars
- pitch classes: Bb 31%, C 28%, Ab 16%, D 13%, G 8%, F 2%
- tonic: G (high, margin 0.189) | cues: most-used note -> Bb; phrase endings -> G; tool key & chords* -> G (key) / G (commonest chord root); other voice -> G
- scale: Kurd [Phrygian] (fit 0.965, shape confidence medium, name_allowed=True) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- candidate ghammaz: Bb (300c, 33% of phrase endings)
- flags: same notes also fit other tonics: C (0.96), Bb (0.96)  -> relative-mode ambiguity
- sections:
  - Section: chorus: G high / Kurd medium (fit 0.965)  [!] same notes also fit other tonics: C (0.97), Bb (0.97)  -> relative-mode ambiguity
  - Section: verse: C low / Nahawand low (fit 0.944)  [!] tonic/dominant split: C and G (a 4th/5th apart) score almost equally; the true tonic could be either
- melody-only cross-check (chords removed): G high / Kurd medium (fit 0.965)
- full report: `work/fadl-shaker-02-bayya-a-el-qeloub-1999-06-awel-hob/report.md`
