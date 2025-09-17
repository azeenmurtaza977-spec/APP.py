import streamlit as st
import requests
import pandas as pd
import datetime

st.set_page_config(page_title="🌍 Live Population Insights", layout="wide")

# Title
st.title("🌍 Live Population Insights Dashboard")

# Fetch population data from World Population API
@st.cache_data(ttl=60)  # refresh every 60 seconds
def get_population():
    url = "https://world-population.p.rapidapi.com/worldpopulation"
    headers = {
        "X-RapidAPI-Key": "YOUR_API_KEY",   # replace with your RapidAPI key
        "X-RapidAPI-Host": "world-population.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()["body"]
    else:
        return None

data = get_population()

if data:
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("🌍 Total World Population", f"{data['world_population']:,}")

    with col2:
        st.metric("👶 Births Today", f"{data['birth_today']:,}")

    with col3:
        st.metric("☠️ Deaths Today", f"{data['death_today']:,}")

    # Trend Data
    df = pd.DataFrame({
        "Metric": ["Population", "Births Today", "Deaths Today"],
        "Value": [data['world_population'], data['birth_today'], data['death_today']]
    })

    st.bar_chart(df.set_index("Metric"))

    # Update timestamp
    st.caption(f"Last updated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
else:
    st.error("Could not fetch population data. Check your API key or internet connection.")
