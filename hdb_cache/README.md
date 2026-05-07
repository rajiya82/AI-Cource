# HDB Cache Directory

This folder contains cached HDB resale price data downloaded from data.gov.sg.

## Contents

- **BISHAN.json** - Bishan HDB resale records (July 2022 - present)
- **TAMPINES.json** - Tampines HDB resale records (July 2022 - present)

## Auto-Management

The `fetch_town()` function automatically:
1. Checks if data is already cached
2. Downloads from data.gov.sg on first run (20-40 seconds)
3. Saves as JSON for instant future access
4. Can be refreshed by deleting the cache file and re-running

## Manual Cache Management

To refresh cached data:

```python
# Option 1: Delete specific town cache
import os
os.remove('hdb_cache/BISHAN.json')

# Option 2: Re-run fetch_town() - it will re-download
data = fetch_town('BISHAN')

# Option 3: Delete entire cache folder and re-run
# (notebook will recreate it on next fetch_town() call)
```

## Cache File Format

Each JSON file contains:
```json
{
  "town": "BISHAN",
  "start_date": "2022-07",
  "cached_at": "2026-05-06 14:30",
  "records": [
    {
      "month": "2026-04",
      "town": "BISHAN",
      "flat_type": "4 ROOM",
      "flat_model": "New Generation",
      "lease_commence_date": 1999,
      "floor_area_sqm": 93,
      "resale_price": 620000,
      "storey_range": "01 TO 03"
    },
    ...
  ]
}
```

---
Generated: May 6, 2026
