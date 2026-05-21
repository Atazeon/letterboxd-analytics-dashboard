# Letterboxd Data Analytics Pipeline & Dashboard

An end-to-end data engineering and visualization project that transforms a static Letterboxd diary export into a fully enriched, interactive analytics dashboard. 

## Overview
This project takes a raw `diary.csv` export from Letterboxd, runs it through a custom Python data pipeline to fetch missing metadata (posters, runtime, genres, public ratings) via the TMDB API, and serves the enriched dataset to a live Streamlit web application.

### Key Features
* **Automated Data Enrichment:** Uses the `tmdbv3api` to dynamically pull high-resolution movie posters, runtimes, and genre classifications.
* **Smart Fuzzy Matching:** Implements a custom matching algorithm to account for release-year discrepancies (e.g., festival premiere vs. theatrical release) between the Letterboxd and TMDB databases.
* **Network Fault Tolerance:** Built with robust retry logic and exponential backoff to handle server-side rate limits and connection drops (`Error 10054`) from enterprise security firewalls (Cloudflare).
* **Interactive Visualization:** A responsive frontend built with Streamlit that visualizes viewing habits, genre distributions, and a 5-Star "Hall of Fame."

## Tech Stack
* **Language:** Python 3
* **Data Manipulation:** Pandas
* **API Integration:** tmdbv3api, REST APIs
* **Frontend/Deployment:** Streamlit, Streamlit Community Cloud
* **Environment Management:** python-dotenv

## Local Setup & Installation

If you want to run this pipeline locally with your own Letterboxd data, follow these steps:

**1. Clone the repository**
```bash
git clone [https://github.com/atazeon/letterboxd-analytics-dashboard.git](https://github.com/atazeon/letterboxd-analytics-dashboard.git)
cd letterboxd-analytics-dashboard
```

**2. Install dependencies**
`pip install pandas streamlit tmdbv3api python-dotenv`

**3. Setup your environment variables**
Create a `.env` file in the root directory and add your TMDB API key:
`TMDB_API_KEY="your_api_key_here"`

**4. Add your data**
Export your data from Letterboxd and place the `diary.csv` file into the root folder. 

**5. Run the data pipeline**
This script will clean your data, ping the TMDB API, and generate a `final_enriched_diary.csv` file. 
`python api_test.py`

**6. Launch the dashboard**
`streamlit run dashboard.py`
