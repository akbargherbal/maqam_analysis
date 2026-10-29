# Maqam review — batch-010 (8 songs)

Read `skills/maqam-analysis/SKILL.md` before deciding. Hard rules:
- 12-TET ABC cannot prove quarter tones. Quarter-tone maqamat (Rast, Bayati, Saba, Sikah, Huzam, Iraq, Awj Ara, Suznek, Jiharkah, Bastanikar) are status `possible`, never `consistent`.
- If the analyzer says `name_allowed=false`, a scale is not identified, parse <95%, or pitch classes are too few: use `maqam_status="withheld"`.
- Confidence can be lowered, never raised above the tool's evidence.
- A tonic/dominant split must name the other tonic in `tonic_alternatives`.
- Never import outside knowledge of the song. Evidence is the ABC only.

Fill the sibling template, then run:
```bash
python3 scripts/review.py record --batch work/review/batch-010.json \
  --labels work/review/batch-010.labels.json
```

## 1. `elissa-2009-tesada-a-bemeen-08-law-feye` — Elissa — Elissa - 2009 Tesada'a Bemeen — "لو فيي"
- file: `08.Law Feye.mp3` | duration 249.078s | declared key C#m | tempo 124.0 | voice Vocal
- parse: 100% of bars
- pitch classes: E 24%, Ab 21%, F# 18%, C# 13%, Eb 12%, B 6%
- tonic: Ab (low, margin 0.135) | cues: most-used note -> E; phrase endings -> Ab; tool key & chords* -> C# (key) / C# (commonest chord root); other voice -> Ab
- scale: Kurd [Phrygian] (fit 0.997, shape confidence medium, name_allowed=True) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- candidate ghammaz: E (800c, 20% of phrase endings)
- flags: same notes also fit other tonics: C# (1.00), E (1.00)  -> relative-mode ambiguity
- sections:
  - Section: chorus: Ab low / Kurd medium (fit 0.996)  [!] same notes also fit other tonics: E (1.00), C# (1.00)  -> relative-mode ambiguity
  - Section: verse: Ab low / Kurd medium (fit 1.0)  [!] tonic/dominant split: Ab and Eb (a 4th/5th apart) score almost equally; the true tonic could be either
- melody-only cross-check (chords removed): Ab low / Kurd medium (fit 0.997)
- full report: `work/elissa-2009-tesada-a-bemeen-08-law-feye/report.md`
## 2. `elissa-2009-tesada-a-bemeen-09-eftakart` — Elissa — Elissa - 2009 Tesada'a Bemeen — "افتكرت"
- file: `09.Eftakart.mp3` | duration 353.959s | declared key D#m | tempo 58.0 | voice Vocal
- parse: 100% of bars
- pitch classes: C# 23%, F 18%, F# 17%, Eb 13%, B 12%, Bb 10%
- tonic: B (low, margin 0.027) | cues: most-used note -> C#; phrase endings -> B; tool key & chords* -> Eb (key) / Bb (commonest chord root); other voice -> F#
- scale: (no standard maqam) [Lydian] (fit 1.0, shape confidence medium, name_allowed=True) | tied: (no standard maqam)
- candidate ghammaz: F (600c, 19% of phrase endings)
- flags: same notes also fit other tonics: Bb (1.00), Eb (1.00), C# (1.00)  -> relative-mode ambiguity
- sections:
  - Section: verse: B low / (no standard maqam) medium (fit 1.0)  [!] same notes also fit other tonics: C# (1.00), Bb (1.00), Eb (1.00)  -> relative-mode ambiguity
  - Section: chorus: B low / (no standard maqam) medium (fit 1.0)  [!] same notes also fit other tonics: C# (1.00), Bb (1.00)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): B low / (no standard maqam) medium (fit 1.0)
- full report: `work/elissa-2009-tesada-a-bemeen-09-eftakart/report.md`
## 3. `elissa-2009-tesada-a-bemeen-10-w-byestehi` — Elissa — Elissa - 2009 Tesada'a Bemeen — "وبيستحي"
- file: `10.W Byestehi.mp3` | duration 258.22s | declared key Bbm | tempo 67.0 | voice Vocal
- parse: 100% of bars
- pitch classes: Ab 23%, F# 22%, Bb 16%, F 15%, C 14%, C# 6%
- tonic: F (low, margin 0.097) | cues: most-used note -> Ab; phrase endings -> F; tool key & chords* -> Bb (key) / F# (commonest chord root); other voice -> F
- scale: Kurd [Phrygian] (fit 1.0, shape confidence medium, name_allowed=True) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- candidate ghammaz: Ab (300c, 15% of phrase endings)
- flags: tonic/dominant split: F and Bb (a 4th/5th apart) score almost equally; the true tonic could be either | same notes also fit other tonics: Bb (1.00), F# (1.00), Ab (1.00)  -> relative-mode ambiguity
- sections:
  - Section: verse: Bb low / Nahawand medium (fit 1.0)  [!] tonic/dominant split: Bb and F (a 4th/5th apart) score almost equally; the true tonic could be either
  - Section: chorus: F low / Kurd medium (fit 0.98)  [!] tonic/dominant split: F and Bb (a 4th/5th apart) score almost equally; the true tonic could be either
- melody-only cross-check (chords removed): F low / Kurd medium (fit 1.0)
- full report: `work/elissa-2009-tesada-a-bemeen-10-w-byestehi/report.md`
## 4. `elissa-2009-tesada-a-bemeen-11-ma-ta-rafchi-lei` — Elissa — Elissa - 2009 Tesada'a Bemeen — "ما تعرفش ليه"
- file: `11.Ma Ta'rafchi Lei.mp3` | duration 286.955s | declared key Am | tempo 67.0 | voice Vocal
- parse: 100% of bars
- pitch classes: E 26%, F 24%, G 17%, D 11%, A 11%, B 7%
- tonic: E (high, margin 0.129) | cues: most-used note -> E; phrase endings -> E; tool key & chords* -> A (key) / A (commonest chord root); other voice -> E
- scale: Kurd [Phrygian] (fit 1.0, shape confidence medium, name_allowed=True) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- candidate ghammaz: G (300c, 30% of phrase endings)
- flags: same notes also fit other tonics: A (1.00), D (1.00), G (1.00)  -> relative-mode ambiguity
- sections:
  - Section: verse: D low / (no standard maqam) medium (fit 1.0)  [!] same notes also fit other tonics: A (1.00), E (1.00), G (1.00)  -> relative-mode ambiguity
  - Section: chorus: E medium / Kurd medium (fit 0.98)  [!] same notes also fit other tonics: A (0.98), G (0.98), D (0.98)  -> relative-mode ambiguity
  - Section: bridge: E low / Kurd medium (fit 0.98)  [!] same notes also fit other tonics: A (0.98), F (0.98), D (0.98)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): E high / Kurd medium (fit 1.0)
- full report: `work/elissa-2009-tesada-a-bemeen-11-ma-ta-rafchi-lei/report.md`
## 5. `elissa-2009-tesada-a-bemeen-12-aisha-welsalam` — Elissa — Elissa - 2009 Tesada'a Bemeen — "عيشه والسلام"
- file: `12.Aisha Welsalam.mp3` | duration 347.585s | declared key Dm | tempo 121.0 | voice Vocal
- parse: 100% of bars
- pitch classes: F 23%, G 16%, E 15%, D 14%, C 13%, A 11%
- tonic: G (low, margin 0.001) | cues: most-used note -> F; phrase endings -> E; tool key & chords* -> D (key) / A (commonest chord root); other voice -> E
- scale: (no standard maqam) [Dorian] (fit 0.999, shape confidence medium, name_allowed=True) | tied: Rast, (no standard maqam) | 12-TET shadow of: Rast
- candidate ghammaz: E (900c, 15% of phrase endings)
- flags: tonic/dominant split: G and D (a 4th/5th apart) score almost equally; the true tonic could be either | same notes also fit other tonics: D (1.00), F (1.00)  -> relative-mode ambiguity
- sections:
  - Section: verse: F low / Ajam medium (fit 0.997)  [!] same notes also fit other tonics: G (1.00), D (1.00), A (1.00)  -> relative-mode ambiguity
  - Section: chorus: E low / Kurd low (fit 0.857)  [!] same notes also fit other tonics: C (1.00), D (1.00), Bb (1.00)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): F low / Ajam medium (fit 0.999)
- full report: `work/elissa-2009-tesada-a-bemeen-12-aisha-welsalam/report.md`
## 6. `elissa-2009-tesada-a-bemeen-13-masdoma` — Elissa — Elissa - 2009 Tesada'a Bemeen — "مصدومة"
- file: `13.Masdoma.mp3` | duration 263.079s | declared key Fm | tempo 84.0 | voice Vocal
- parse: 100% of bars
- pitch classes: F 30%, G 18%, Eb 16%, C# 12%, C 12%, Ab 6%
- tonic: C (low, margin 0.052) | cues: most-used note -> F; phrase endings -> C; tool key & chords* -> F (key) / Bb (commonest chord root); other voice -> C
- scale: Kurd [Phrygian] (fit 0.988, shape confidence medium, name_allowed=True) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- candidate ghammaz: Eb (300c, 10% of phrase endings)
- flags: tonic/dominant split: C and F (a 4th/5th apart) score almost equally; the true tonic could be either | same notes also fit other tonics: F (0.99), Bb (0.99), C# (0.99)  -> relative-mode ambiguity
- sections:
  - Section: verse: C low / Kurd medium (fit 1.0)  [!] same notes also fit other tonics: F (1.00), C# (1.00), Eb (1.00)  -> relative-mode ambiguity
  - Section: chorus: C low / Kurd medium (fit 0.97)  [!] same notes also fit other tonics: Bb (0.97), F (0.97), Eb (0.97)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): C low / Kurd medium (fit 0.988)
- full report: `work/elissa-2009-tesada-a-bemeen-13-masdoma/report.md`
## 7. `elissa-2012-as3ad-wa7da-01-fi-ouyounak` — Elissa — Elissa - 2012  As3ad Wa7da — "في عيــونك"
- file: `01. Fi Ouyounak.mp3` | duration 272.274s | declared key Em | tempo 73.0 | voice Vocal
- parse: 100% of bars
- pitch classes: E 29%, B 19%, D 15%, F# 14%, C 9%, A 8%
- tonic: B (low, margin 0.211) | cues: most-used note -> E; phrase endings -> B; tool key & chords* -> E (key) / E (commonest chord root); other voice -> E
- scale: Kurd [Phrygian] (fit 1.0, shape confidence medium, name_allowed=True) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- flags: same notes also fit other tonics: E (1.00), D (1.00), A (1.00)  -> relative-mode ambiguity
- sections:
  - Section: verse: B low / Kurd medium (fit 1.0)  [!] same notes also fit other tonics: E (1.00), A (1.00)  -> relative-mode ambiguity
  - Section: chorus: B low / Kurd medium (fit 1.0)  [!] same notes also fit other tonics: E (1.00), A (1.00), D (1.00)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): B low / Kurd medium (fit 1.0)
- full report: `work/elissa-2012-as3ad-wa7da-01-fi-ouyounak/report.md`
## 8. `elissa-2012-as3ad-wa7da-02-as3ad-wa7da` — Elissa — Elissa - 2012  As3ad Wa7da — "أسعد واحدة"
- file: `02. As3ad Wa7da.mp3` | duration 276.01s | declared key Dm | tempo 126.0 | voice Vocal
- parse: 100% of bars
- pitch classes: F 18%, E 18%, Bb 17%, G 14%, A 14%, D 10%
- tonic: A (low, margin 0.284) | cues: most-used note -> F; phrase endings -> A; tool key & chords* -> D (key) / A (commonest chord root); other voice -> A
- scale: Kurd [Phrygian] (fit 1.0, shape confidence medium, name_allowed=True) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- flags: same notes also fit other tonics: D (1.00), G (1.00), Bb (1.00)  -> relative-mode ambiguity
- sections:
  - Section: verse: A low / Kurd medium (fit 1.0)  [!] same notes also fit other tonics: G (1.00), D (1.00), Bb (1.00)  -> relative-mode ambiguity
  - Section: chorus: A low / Kurd medium (fit 1.0)  [!] same notes also fit other tonics: D (1.00), Bb (1.00), C (1.00)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): A low / Kurd medium (fit 1.0)
- full report: `work/elissa-2012-as3ad-wa7da-02-as3ad-wa7da/report.md`
