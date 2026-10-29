# Maqam review — batch-011 (8 songs)

Read `skills/maqam-analysis/SKILL.md` before deciding. Hard rules:
- 12-TET ABC cannot prove quarter tones. Quarter-tone maqamat (Rast, Bayati, Saba, Sikah, Huzam, Iraq, Awj Ara, Suznek, Jiharkah, Bastanikar) are status `possible`, never `consistent`.
- If the analyzer says `name_allowed=false`, a scale is not identified, parse <95%, or pitch classes are too few: use `maqam_status="withheld"`.
- Confidence can be lowered, never raised above the tool's evidence.
- A tonic/dominant split must name the other tonic in `tonic_alternatives`.
- Never import outside knowledge of the song. Evidence is the ABC only.

Fill the sibling template, then run:
```bash
python3 scripts/review.py record --batch work/review/batch-011.json \
  --labels work/review/batch-011.labels.json
```

## 1. `elissa-2012-as3ad-wa7da-03-moutafa2la` — Elissa — Elissa - 2012  As3ad Wa7da — "متفائلة"
- file: `03. Moutafa2La.mp3` | duration 326.034s | declared key G#m | tempo 62.0 | voice Vocal
- parse: 100% of bars
- pitch classes: E 20%, Ab 18%, Eb 15%, C# 15%, B 14%, Bb 11%
- tonic: Ab (high, margin 0.23) | cues: most-used note -> E; phrase endings -> Ab; tool key & chords* -> Ab (key) / Ab (commonest chord root); other voice -> Ab
- scale: Nahawand [natural minor / Aeolian] (fit 0.914, shape confidence low, name_allowed=True) | tied: Bayati, Nahawand | 12-TET shadow of: Bayati
- candidate ghammaz: C# (500c, 27% of phrase endings)
- flags: same notes also fit other tonics: C# (0.91), B (0.91), E (0.91)  -> relative-mode ambiguity
- sections:
  - Section: verse: C# low / Nikriz medium (fit 0.98)  [!] same notes also fit other tonics: Eb (0.98), Ab (0.98), E (0.98)  -> relative-mode ambiguity
  - Section: pre-chorus: B low / Ajam low (fit 0.841)  [!] same notes also fit other tonics: Ab (0.84), F# (0.84), E (0.84)  -> relative-mode ambiguity
  - Section: chorus: Ab high / Nahawand low (fit 0.904)  [!] same notes also fit other tonics: C# (0.90), E (0.90)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): Ab high / Nahawand low (fit 0.914)
- full report: `work/elissa-2012-as3ad-wa7da-03-moutafa2la/report.md`
## 2. `elissa-2012-as3ad-wa7da-04-faker` — Elissa — Elissa - 2012  As3ad Wa7da — "فاكر"
- file: `04. Faker.mp3` | duration 344.66s | declared key Em | tempo 88.0 | voice Vocal
- parse: 100% of bars
- pitch classes: E 19%, F# 19%, B 16%, G 14%, D 11%, A 11%
- tonic: E (low, margin 0.077) | cues: most-used note -> E; phrase endings -> B; tool key & chords* -> E (key) / A (commonest chord root); other voice -> B
- scale: Nahawand [natural minor / Aeolian] (fit 1.0, shape confidence medium, name_allowed=True) | tied: Bayati, Nahawand | 12-TET shadow of: Bayati
- candidate ghammaz: B (700c, 36% of phrase endings)
- flags: tonic/dominant split: E and B (a 4th/5th apart) score almost equally; the true tonic could be either | same notes also fit other tonics: B (1.00), C (1.00), G (1.00)  -> relative-mode ambiguity
- sections:
  - Section: verse: E low / Nahawand medium (fit 1.0)  [!] tonic/dominant split: E and B (a 4th/5th apart) score almost equally; the true tonic could be either
  - Section: chorus: C low / (no standard maqam) medium (fit 1.0)  [!] same notes also fit other tonics: B (1.00), D (1.00), E (1.00)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): E low / Nahawand medium (fit 1.0)
- full report: `work/elissa-2012-as3ad-wa7da-04-faker/report.md`
## 3. `elissa-2012-as3ad-wa7da-06-law-aoullak` — Elissa — Elissa - 2012  As3ad Wa7da — "لو اقولك"
- file: `06. Law Aoullak.mp3` | duration 228.833s | declared key Gm | tempo 125.0 | voice Vocal
- parse: 100% of bars
- pitch classes: G 27%, D 22%, Eb 20%, F 14%, A 11%, Bb 4%
- tonic: G (low, margin 0.114) | cues: most-used note -> G; phrase endings -> D; tool key & chords* -> G (key) / D (commonest chord root); other voice -> Eb
- scale: Nahawand [natural minor / Aeolian] (fit 1.0, shape confidence medium, name_allowed=True) | tied: Bayati, Nahawand | 12-TET shadow of: Bayati
- candidate ghammaz: F (1000c, 35% of phrase endings)
- flags: tonic/dominant split: G and D (a 4th/5th apart) score almost equally; the true tonic could be either | same notes also fit other tonics: D (1.00), F (1.00), Eb (1.00)  -> relative-mode ambiguity
- sections:
  - Section: verse: D low / Kurd medium (fit 1.0)  [!] same notes also fit other tonics: G (1.00), F (1.00), Eb (1.00)  -> relative-mode ambiguity
  - Section: chorus: G medium / Nahawand medium (fit 0.98)  [!] same notes also fit other tonics: D (0.98), F (0.98), Eb (0.98)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): G low / Nahawand medium (fit 1.0)
- full report: `work/elissa-2012-as3ad-wa7da-06-law-aoullak/report.md`
## 4. `elissa-2012-as3ad-wa7da-08-rohtelo` — Elissa — Elissa - 2012  As3ad Wa7da — "روحتله"
- file: `08. Rohtelo.mp3` | duration 245.473s | declared key Bbm | tempo 88.0 | voice Vocal
- parse: 100% of bars
- pitch classes: F 22%, C 19%, Bb 18%, C# 15%, F# 12%, Eb 10%
- tonic: Bb (low, margin 0.111) | cues: most-used note -> F; phrase endings -> F; tool key & chords* -> Bb (key) / Bb (commonest chord root); other voice -> Bb
- scale: Nahawand (raised 7th) [harmonic minor] (fit 0.978, shape confidence medium, name_allowed=True) | tied: Nahawand (raised 7th)
- candidate ghammaz: F (700c, 50% of phrase endings)
- flags: tonic/dominant split: Bb and F (a 4th/5th apart) score almost equally; the true tonic could be either | same notes also fit other tonics: F (0.98)  -> relative-mode ambiguity
- sections:
  - Section: verse: Bb low / Nahawand (raised 7th) medium (fit 0.99)  [!] same notes also fit other tonics: F (0.99), Eb (0.99)  -> relative-mode ambiguity
  - Section: chorus: Bb low / Nahawand medium (fit 0.986)  [!] tonic/dominant split: Bb and F (a 4th/5th apart) score almost equally; the true tonic could be either
- melody-only cross-check (chords removed): Bb low / Nahawand (raised 7th) medium (fit 0.978)
- full report: `work/elissa-2012-as3ad-wa7da-08-rohtelo/report.md`
## 5. `elissa-2012-as3ad-wa7da-09-eghmerni` — Elissa — Elissa - 2012  As3ad Wa7da — "اغمرني"
- file: `09. Eghmerni.mp3` | duration 310.7s | declared key C#m | tempo 105.0 | voice Vocal
- parse: 100% of bars
- pitch classes: E 23%, F# 19%, Ab 16%, Eb 14%, A 13%, B 10%
- tonic: Ab (low, margin 0.021) | cues: most-used note -> E; phrase endings -> Ab; tool key & chords* -> C# (key) / C# (commonest chord root); other voice -> Eb
- scale: Kurd [Phrygian] (fit 1.0, shape confidence medium, name_allowed=True) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- candidate ghammaz: E (800c, 38% of phrase endings)
- flags: tonic/dominant split: Ab and C# (a 4th/5th apart) score almost equally; the true tonic could be either | same notes also fit other tonics: C# (1.00), E (1.00), F# (1.00)  -> relative-mode ambiguity
- sections:
  - Section: intro: E low / Ajam medium (fit 0.98)  [!] same notes also fit other tonics: Ab (0.98), F# (0.98), B (0.98)  -> relative-mode ambiguity
  - Section: verse: Ab low / Kurd medium (fit 1.0)  [!] same notes also fit other tonics: C# (1.00), B (1.00)  -> relative-mode ambiguity
  - Section: chorus: Ab medium / Kurd medium (fit 1.0)  [!] same notes also fit other tonics: C# (1.00), A (1.00), F# (1.00)  -> relative-mode ambiguity
  - Section: interlude: E low / Ajam medium (fit 0.98)  [!] same notes also fit other tonics: Ab (0.98), B (0.98), F# (0.98)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): Ab low / Kurd medium (fit 1.0)
- full report: `work/elissa-2012-as3ad-wa7da-09-eghmerni/report.md`
## 6. `elissa-2012-as3ad-wa7da-11-alouli-el-eid` — Elissa — Elissa - 2012  As3ad Wa7da — "قالولي العيد"
- file: `11. Alouli El Eid.mp3` | duration 295.602s | declared key Cm | tempo 103.0 | voice Vocal
- parse: 100% of bars
- pitch classes: G 23%, Bb 17%, D 15%, F 13%, Ab 12%, C 12%
- tonic: G (high, margin 0.36) | cues: most-used note -> G; phrase endings -> G; tool key & chords* -> C (key) / G (commonest chord root); other voice -> G
- scale: Kurd [Phrygian] (fit 1.0, shape confidence medium, name_allowed=True) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- flags: same notes also fit other tonics: C (1.00), F (1.00), Bb (1.00)  -> relative-mode ambiguity
- sections:
  - Section: verse: G low / Kurd medium (fit 1.0)  [!] same notes also fit other tonics: Bb (1.00), C (1.00), Ab (1.00)  -> relative-mode ambiguity
  - Section: chorus: G medium / Kurd medium (fit 1.0)  [!] same notes also fit other tonics: C (1.00), Eb (1.00), F (1.00)  -> relative-mode ambiguity
  - Section: bridge: G low / Kurd medium (fit 1.0)  [!] tonic/dominant split: G and C (a 4th/5th apart) score almost equally; the true tonic could be either
- melody-only cross-check (chords removed): G high / Kurd medium (fit 1.0)
- full report: `work/elissa-2012-as3ad-wa7da-11-alouli-el-eid/report.md`
## 7. `elissa-2012-as3ad-wa7da-12-albi-hasis-fik` — Elissa — Elissa - 2012  As3ad Wa7da — "قلبي حاسس فيك"
- file: `12. Albi Hasis Fik.mp3` | duration 305.842s | declared key D#m | tempo 132.0 | voice Vocal
- parse: 100% of bars
- pitch classes: F 29%, Eb 28%, F# 20%, C# 7%, Ab 6%, B 6%
- tonic: Bb (low, margin 0.167) | cues: most-used note -> F; phrase endings -> Bb; tool key & chords* -> Eb (key) / B (commonest chord root); other voice -> Eb
- scale: Kurd [Phrygian] (fit 0.983, shape confidence medium, name_allowed=True) | tied: Bayati, Kurd | 12-TET shadow of: Bayati
- candidate ghammaz: F (700c, 33% of phrase endings)
- flags: same notes also fit other tonics: Eb (0.98), F# (0.98)  -> relative-mode ambiguity
- sections:
  - Section: verse: F medium / Kurd low (fit 0.83)  [!] same notes also fit other tonics: F# (0.96), Eb (0.96), B (0.96)  -> relative-mode ambiguity
  - Section: chorus: Bb low / Kurd low (fit 0.915)  [!] same notes also fit other tonics: Eb (0.92), C# (0.92), B (0.92)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): Bb low / Kurd medium (fit 0.983)
- full report: `work/elissa-2012-as3ad-wa7da-12-albi-hasis-fik/report.md`
## 8. `elissa-2012-as3ad-wa7da-13-sa3at` — Elissa — Elissa - 2012  As3ad Wa7da — "ساعات"
- file: `13. Sa3at.mp3` | duration 305.319s | declared key F#m | tempo 76.0 | voice Vocal
- parse: 100% of bars
- pitch classes: F# 33%, E 18%, D 18%, Ab 15%, C# 8%, A 6%
- tonic: F# (low, margin 0.039) | cues: most-used note -> F#; phrase endings -> D; tool key & chords* -> F# (key) / C# (commonest chord root); other voice -> C#
- scale: Nahawand [natural minor / Aeolian] (fit 0.978, shape confidence medium, name_allowed=True) | tied: Bayati, Nahawand | 12-TET shadow of: Bayati
- candidate ghammaz: E (1000c, 32% of phrase endings)
- flags: same notes also fit other tonics: D (0.98), C# (0.98), E (0.98)  -> relative-mode ambiguity
- sections:
  - Section: verse: C# low / Kurd medium (fit 0.953)  [!] tonic/dominant split: C# and F# (a 4th/5th apart) score almost equally; the true tonic could be either
  - Section: chorus: F# low / Nahawand medium (fit 0.98)  [!] same notes also fit other tonics: E (0.98), D (0.98), C# (0.98)  -> relative-mode ambiguity
- melody-only cross-check (chords removed): F# low / Nahawand medium (fit 0.978)
- full report: `work/elissa-2012-as3ad-wa7da-13-sa3at/report.md`
