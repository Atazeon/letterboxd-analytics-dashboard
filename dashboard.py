import streamlit as st
import pandas as pd

st.set_page_config(page_title="My Letterboxd Dashboard", layout="wide")
st.title("My Letterboxd Diary Analytics")

@st.cache_data
def load_data():
    df = pd.read_csv("final_enriched_diary.csv").dropna(subset=['Poster_URL'])
    if "Watched Date" in df.columns:
        df = df.sort_values(by="Watched Date", ascending=False)
    return df

df = load_data()

st.markdown("### Quick Stats")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Movies", len(df))
col2.metric("Average Rating", f"{round(df['Rating'].mean(), 2)} / 5.0")
col3.metric("Total Hours", round(df['Runtime'].sum() / 60, 1))
col4.metric("Perfect 5-Stars", len(df[df['Rating'] == 5.0]))

st.divider()

st.markdown("### Watching Habits")
chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    st.markdown("**Your Top 10 Genres**")

    genre_counts = df['Genres'].dropna().str.split(', ').explode().value_counts().head(10)
    st.bar_chart(genre_counts)

with chart_col2:
    st.markdown("**Your Rating Distribution**")

    rating_counts = df['Rating'].value_counts().sort_index()
    st.bar_chart(rating_counts)

st.divider()

st.markdown("### 5-Star Hall of Fame")
perfect_scores = df[df['Rating'] == 5.0].head(5)
cols = st.columns(5)

for col, (_, row) in zip(cols, perfect_scores.iterrows()):
    col.image(row['Poster_URL'], caption=f"{row['Name']} ({row['Year']})")
