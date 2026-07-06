# MAL-Analytics 🎬

**Automated Insights via Web Scraping** — a Python pipeline that scrapes MyAnimeList's Top Anime rankings and turns them into a clean, analysis-ready CSV.

## Overview

This project bridges static web content and structured data analytics. It targets [MyAnimeList](https://myanimelist.net/topanime.php) and harvests rankings, user scores, and series metadata for the top 200 titles, transforming messy HTML into a research-ready dataset for trend analysis and recommendation modeling.

## Tech Stack

| Library | Role |
|---|---|
| `requests` | Fetches raw HTML from MAL servers with spoofed browser headers |
| `BeautifulSoup` (bs4) | Parses HTML into a navigable DOM tree for precise data extraction |
| `pandas` | Converts scraped records into a structured DataFrame and exports to CSV |
| `time` | Rate-limits requests to avoid hammering the server |

## Pipeline

1. **Targeting** — Calculate pagination offsets (`0, 50, 100, 150`) to cover the top 200 anime.
2. **Downloading** — Send GET requests with a spoofed `User-Agent` header and a 10s timeout.
3. **Parsing** — Isolate each `<tr class="ranking-list">` row, then drill into `<h3>`, `<span class="score-label">`, and the `information` div for metadata.
4. **Sanitizing** — Strip whitespace, split combined fields (e.g. `"TV (64 eps)"` → `"TV"` / `"64"`), and remove label noise (e.g. `"3,210,123 members"` → `3210123`).
5. **Exporting** — Serialize the collected records into `top_anime.csv` via `pandas`.

## Data Fields

| Column | Description |
|---|---|
| Rank | MAL ranking position |
| Title | Anime title |
| Type | TV, Movie, OVA, ONA, etc. |
| Episodes | Episode count (`?` if still airing/unknown) |
| Air Dates | Broadcast date range |
| Members | Number of MAL members who added the title |
| Score | Average user rating |

## Robustness Features

- **Fault tolerance** — nested `try/except` blocks skip a row with missing data instead of crashing the whole run.
- **Network resiliency** — a 10-second timeout prevents hangs on slow connections.
- **Graceful shutdown** — a `finally` block saves whatever has been scraped so far, even on `KeyboardInterrupt`.
- **Request throttling** — a 2-second pause between page requests to stay a good web citizen.

## Setup

```bash
pip install -r requirements.txt
python main.py
```

Output is saved to `top_anime.csv` in the project root.

## Requirements

- Python 3.9+
- See `requirements.txt` for package versions

## Notes / Known Limitations

- Relies on MAL's current HTML structure (CSS classes like `ranking-list`, `information`). If MAL redesigns the page, the selectors will need updating.
- No `?` (unknown episode count) handling beyond passing the raw string through — treat that column as a string, not always an int, in downstream analysis.
- Scraping is for personal/educational analytics use; review MyAnimeList's [Terms of Service](https://myanimelist.net/about/terms_of_use) and `robots.txt` before scaling up request volume.

## License

Add a license of your choice (e.g. MIT) if you plan to make this repo public.
