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
git clone [https://github.com/YOUR_USERNAME/letterboxd-analytics-dashboard.git](https://github.com/YOUR_USERNAME/letterboxd-analytics-dashboard.git)
cd letterboxd-analytics-dashboard
