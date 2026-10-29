# Maqam label export

Generated: 2026-10-29T08:25:13Z  |  run: `maqam-167-v1`

This is a **weak-label** dataset derived from SheetSage2 ABC transcriptions. It is not ground truth. Quarter-tone maqamat are marked `possible`, not stated as fact.

## Counts

| status | count |
|---|---:|
| labeled | 163 |
| pending | 0 |
| no ABC | 4 |
| missing transcript | 0 |
| needs human review | 163 |

## Maqam distribution

| maqam | count |
|---|---:|
| Kurd | 66 |
| Nahawand | 61 |
| (withheld) | 25 |
| Ajam | 4 |
| Rast | 4 |
| Hijaz | 2 |
| Nahawand (raised 7th) | 1 |

## Confidence

| overall confidence | count |
|---|---:|
| low | 134 |
| medium | 29 |

## Caveats

- Weak labels from SheetSage2 ABC scores. No ground truth exists for this corpus.
- ABC input is 12-TET, so quarter-tone maqamat can only be 'possible', never facts.
- Tonic confidence is a consistency measure between cues, not a probability.
- Four corpus tracks have no ABC and are exported with label_status=no_abc.
- Do not report accuracy without a blind re-review or human labels.

## Duplicate-title consistency

16 duplicate-title groups; 7 disagree. Disagreements are worth a human look.
- كرمالك: Kurd, Nahawand
- متى حبيبي متى: Kurd, Nahawand
- بياع القلوب: Kurd, Nahawand, Kurd
- يا حبيبي تعال: Nahawand, Kurd, Nahawand
- طاير يا هوى: Rast, Kurd
- اخدني معاك: Kurd, Kurd, (withheld), Kurd
- معقول: Nahawand, Rast
