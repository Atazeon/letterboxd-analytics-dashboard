import os
from dotenv import load_dotenv
from tmdbv3api import TMDb, Movie
import pandas as pd
import time

load_dotenv()

tmdb = TMDb()
tmdb.api_key = os.getenv("TMDB_API_KEY")
movie_tool = Movie()

print("Loading Letterboxd diary...")
df = pd.read_csv("diary.csv")

df["Name"] = df["Name"].astype(str).str.strip()
df["Year"] = df["Year"].astype(str).str.replace(".0", "", regex=False).str.strip()

df[["Runtime", "Genres", "Poster_URL", "TMDB_Rating", "Language"]] = None

print(f"Starting API enrichment for {len(df)} movies...\n")

for index, row in df.iterrows():
    title, year = row["Name"], row["Year"]
    print(f"Searching: {title} ({year})...", end=" ", flush=True)

    for attempt in range(10):
        try:
            search_results = movie_tool.search(title)

            if not search_results:
                print("No results found.")
                break

            best_match = next(
                (res for res in search_results if hasattr(res, 'release_date') and res.release_date and abs(int(res.release_date[:4]) - int(year)) <= 1),
                search_results[0]
            )

            details = movie_tool.details(best_match.id)

            df.at[index, "Runtime"] = getattr(details, 'runtime', None)

            if getattr(details, 'genres', None):
                df.at[index, "Genres"] = ", ".join([g['name'] for g in details.genres])

            if getattr(details, 'poster_path', None):
                df.at[index, "Poster_URL"] = f"https://image.tmdb.org/t/p/w500{details.poster_path}"

            df.at[index, "TMDB_Rating"] = getattr(details, 'vote_average', None)
            df.at[index, "Language"] = getattr(details, 'original_language', None)

            print("Found.")
            time.sleep(3)
            break

        except Exception as e:
            if "10054" in str(e) or "forcibly closed" in str(e):
                time.sleep(5)
            else:
                print(f"Error: {e}")
                break
    else:

        print("Failed: Connection dropped.")

df.to_csv("final_enriched_diary.csv", index=False)
print("\nSaved to final_enriched_diary.csv")
