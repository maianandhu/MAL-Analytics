# MAL-Analytics: Automated Web Scraping for Anime Intelligence[cite: 2]

**Author:** Anand Saundarya[cite: 2]

## Project Overview
This project leverages Python to bridge the gap between static web content and structured data analytics[cite: 2]. By targeting MyAnimeList, we've built a robust extraction engine that harvests real-time rankings, user scores, and series metadata for the top 200 titles globally[cite: 2]. The goal is to transform messy HTML into a clean, research-ready dataset for trend analysis and recommendation modeling[cite: 2].

## The Tech Stack
* **Python**[cite: 6]
* **Requests:** Handles the HTTP protocol to "fetch" raw HTML from the MAL servers with custom headers[cite: 2].
* **BeautifulSoup:** Parses the raw HTML document into a searchable tree for precise data pinpointing[cite: 2].
* **Pandas:** Acts as the "Accountant," converting raw lists into a structured CSV database format[cite: 2].
* **Time:** Manages rate-limiting to ensure the script behaves ethically and prevents IP bans[cite: 2].

## The Data Pipeline
This script functions as an automated data extraction pipeline consisting of four distinct stages[cite: 4]:

1. **Target URLs:** Calculating offsets for pagination across multiple pages (0, 50, 100, 150) to fetch all 200 anime[cite: 2, 4, 6].
2. **Raw HTML Download:** Executing GET requests with human-like spoofing[cite: 2, 4].
3. **Data Extraction:** Navigating the DOM to find specific CSS selectors (`<tr class='ranking-list'>`)[cite: 2, 4, 6].
4. **Clean Spreadsheet Export:** Cleaning raw strings, removing HTML noise, and saving to a final spreadsheet (`top_anime.csv`)[cite: 2, 4].

## Key Features
* **Browser Spoofing:** A custom User-Agent header mimics a Chrome browser to bypass bot-detection on MAL[cite: 6].
* **Rate Limiting:** By pausing for 2 seconds between every page request, we avoid triggering server alerts and ensure we don't disrupt the site's performance for other users[cite: 2, 6].
* **Robust Exception Handling (Fault Tolerance):** Nested try-except blocks ensure that if one anime has missing data, the script skips that row rather than crashing the entire process[cite: 2, 4, 6].
* **Network Resiliency:** 10-second timeouts prevent the program from hanging on slow connections[cite: 2].
* **Graceful Shutdown:** Catching `KeyboardInterrupt` allows a safe stop mid-scrape without losing already-collected data, handled via a `finally` block[cite: 2, 4, 6].
* **Data Sanitization / Wrangling:** Inline string parsing strips units (eps, members, commas) for clean numeric fields[cite: 4, 6].

## Data Insights Extracted
The resulting dataset (`top_anime.csv`) contains 200 rows and 7 data fields[cite: 6]. Initial insights reveal:
* **Top Score:** 9.26 (Sousou no Frieren)[cite: 6]
* **Average Score:** 8.66[cite: 6]
* **Most Common Type:** TV[cite: 6]
* **Most Popular:** Shingeki no Kyojin (4.38M members)[cite: 6]

## Setup and Execution
1. Clone the repository.
2. Ensure you have the required libraries installed (`pip install requests beautifulsoup4 pandas`).
3. Run `main.py`[cite: 1].
4. The script will automatically scrape the pages and generate a `top_anime.csv` file in the root directory[cite: 1, 4, 6].
