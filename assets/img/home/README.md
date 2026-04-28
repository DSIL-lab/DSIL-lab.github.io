# Home Slider Images

Images placed in this folder are automatically included in the home page slider.  
They are sorted by **filename in descending order**, so the most recent image appears first.

---

## Naming Convention

```
YY-SEASON_description.jpg
```

| Part | Format | Description |
|---|---|---|
| `YY` | 2-digit year | e.g. `26` for 2026 |
| `SEASON` | `spring` / `summer` / `fall` / `winter` | season name in lowercase English |
| `description` | lowercase English, hyphens for spaces | brief label |
| `.jpg` | lowercase extension | required |

### Examples

| Filename | Meaning |
|---|---|
| `26-spring_spring-outing.jpg` | Spring 2026 outing |
| `25-winter_year-end-party.jpg` | Winter 2025 year-end party |
| `25-fall_ganwolche.jpg` | Fall 2025 Ganwolche hike |
| `25-summer_summer-mt.jpg` | Summer 2025 MT |

---

## Image Requirements

| Item | Requirement |
|---|---|
| **Orientation** | Landscape only |
| **Aspect ratio** | 4 : 3 (e.g. 1200 × 900 px) |
| **File extension** | `.jpg` (lowercase) |
| **Filename characters** | ASCII only — no Korean, spaces, or special characters |

---

## How the Auto-Sort Works

The slider reads all images in this folder and sorts them by **year → season** (most recent first) at page load using JavaScript.

Season order used for sorting: `spring=1 < summer=2 < fall=3 < winter=4`

So `25-winter` ranks higher than `25-fall`, and any `26-...` ranks above any `25-...`.

**Sort check:**  
`26-spring` > `25-winter` > `25-fall` > `25-summer` > `25-spring` ✓

Images whose filenames do not match the `YY-SEASON_...` pattern will appear **last** in the slider.
