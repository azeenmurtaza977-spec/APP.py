import streamlit as st
import time
from datetime import datetime
import pandas as pd

# Page setup
st.set_page_config(page_title="🌍 Live Population Tracker", layout="wide")

st.title("🌍 Live Population Tracker")
st.write("This app simulates global births, deaths, and population growth in real-time.")

# ---- Constants (based on UN/Worldometer estimates) ----
births_per_sec = 4.3     # ~4.3 births every second
deaths_per_sec = 1.8     # ~1.8 deaths every second
start_population = 8000000000  # Approx current world population

# Session state initialization
if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()
if "history" not in st.session_state:
    st.session_state.history = pd.DataFrame(columns=["Time", "Births", "Deaths", "Population"])

# Calculate elapsed time
elapsed = time.time() - st.session_state.start_time

# Live calculations
births = int(elapsed * births_per_sec)
deaths = int(elapsed * deaths_per_sec)
population = start_population + births - deaths

# Save history for plotting
st.session_state.history = pd.concat([
    st.session_state.history,
    pd.DataFrame({"Time": [datetime.now().strftime("%H:%M:%S")],
                  "Births": [births],
                  "Deaths": [deaths],
                  "Population": [population]})
], ignore_index=True).tail(50)  # keep last 50 points

# ---- Display metrics ----
col1, col2, col3 = st.columns(3)
col1.metric("👶 Births (since open)", f"{births:,}")
col2.metric("💀 Deaths (since open)", f"{deaths:,}")
col3.metric("🌍 Current Population", f"{population:,}")

# ---- Charts ----
st.subheader("📈 Real-time Trends (last few seconds)")

# Line chart for births & deaths
st.line_chart(st.session_state.history.set_index("Time")[["Births", "Deaths"]])

# Line chart for population growth
st.line_chart(st.session_state.history.set_index("Time")[["Population"]])

# ---- Monthly & yearly projections ----
st.subheader("📊 Monthly & Yearly Projections")

monthly_births = int(births_per_sec * 60 * 60 * 24 * 30)
monthly_deaths = int(deaths_per_sec * 60 * 60 * 24 * 30)
yearly_births = int(births_per_sec * 60 * 60 * 24 * 365)
yearly_deaths = int(deaths_per_sec * 60 * 60 * 24 * 365)

projection_df = pd.DataFrame({
    "Category": ["Monthly Births", "Monthly Deaths", "Yearly Births", "Yearly Deaths"],
    "Count": [monthly_births, monthly_deaths, yearly_births, yearly_deaths]
})

st.bar_chart(projection_df.set_index("Category"))

# Net insights
st.success(f"📌 Net growth per month: {monthly_births - monthly_deaths:,}")
st.success(f"📌 Net growth per year: {yearly_births - yearly_deaths:,}")
