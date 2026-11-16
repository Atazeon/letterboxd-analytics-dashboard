# Letterboxd Analytics Dashboard

A Streamlit dashboard for exploring a Letterboxd diary. It shows movie counts, average ratings, hours watched, the ten most common genres, a rating distribution, and the five most recent entries rated five stars.

`api_test.py` reads a Letterboxd export and uses TMDB to add runtimes, genres, poster URLs, TMDB ratings, and original languages. `dashboard.py` reads the resulting CSV.

## Run locally

Use Python 3.11, the version configured for the development container.

```bash
git clone https://github.com/Atazeon/letterboxd-analytics-dashboard.git
cd letterboxd-analytics-dashboard
python -m venv .venv
source .venv/bin/activate
pip install pandas streamlit tmdbv3api python-dotenv
streamlit run dashboard.py
```

On Windows, activate the environment with `.venv\Scripts\activate`.

The repository includes `final_enriched_diary.csv`, so you can run the dashboard without an API key. Run commands from the repository root so the scripts can find the CSV files.

## Use your own diary

1. Export your data from Letterboxd and replace `diary.csv` with your export's diary file.
2. Create a `.env` file in the repository root with your TMDB API key:

   ```dotenv
   TMDB_API_KEY=your_api_key_here
   ```

3. Fetch the movie metadata:

   ```bash
   python api_test.py
   ```

4. Start the dashboard:

   ```bash
   streamlit run dashboard.py
   ```

The script overwrites `final_enriched_diary.csv`. It searches TMDB by title, picks the first result released within one year of the diary's release year, and falls back to the first search result if none match. Some entries may need manual correction.

Each successful lookup is followed by a three-second pause. Connection errors containing `10054` or `forcibly closed` are retried up to ten attempts with a fixed five-second delay. Other errors skip the entry.

The dashboard excludes entries without poster URLs, including from its summary statistics. Counts represent diary entries, so rewatches count separately.
