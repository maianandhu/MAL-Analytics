import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/137.0 Safari/537.36"
}

anime_data = []

try:

    for offset in [0, 50, 100, 150]:

        url = f"https://myanimelist.net/topanime.php?limit={offset}"

        print(f"Fetching page with offset {offset}...")

        try:
            response = requests.get(url, headers=headers, timeout=10)

            if response.status_code != 200:
                print(f"Failed to fetch page. Status Code: {response.status_code}")
                continue

            soup = BeautifulSoup(response.text, "html.parser")

            rows = soup.find_all("tr", class_="ranking-list")

            for row in rows:

                try:
                    rank_tag = row.find("td", class_="rank ac")
                    rank = rank_tag.find("span").text.strip()

                    title = row.find("h3").text.strip()

                    score_tag = row.find("span", class_="score-label")
                    score = score_tag.text.strip()

                    info_tag = row.find("div", class_="information")

                    lines = [x.strip() for x in info_tag.stripped_strings]

                    anime_type = lines[0].split("(")[0].strip()
                    episodes = (
                        lines[0]
                        .split("(")[1]
                        .replace("eps)", "")
                        .strip()
                    )

                    air_dates = lines[1]

                    members = (
                        lines[2]
                        .replace("members", "")
                        .replace(",", "")
                        .strip()
                    )

                    anime_data.append({
                        "Rank": rank,
                        "Title": title,
                        "Type": anime_type,
                        "Episodes": episodes,
                        "Air Dates": air_dates,
                        "Members": members,
                        "Score": score
                    })

                except Exception as e:
                    print(f"Error parsing anime row: {e}")

            time.sleep(2)

        except requests.exceptions.RequestException as e:
            print(f"Request Error: {e}")

except KeyboardInterrupt:
    print("\nScraping stopped by user.")

finally:

    try:
        df = pd.DataFrame(anime_data)

        df.to_csv("top_anime.csv", index=False)

        print(f"\nSaved {len(df)} records to top_200_anime.csv")

    except PermissionError:
        print(
            "Cannot save CSV. Close the file if it is open in Excel and try again."
        )

    except Exception as e:
        print(f"Error saving CSV: {e}")