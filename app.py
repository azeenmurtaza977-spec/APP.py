import streamlit as st
import time
from datetime import datetime

# Config
st.set_page_config(page_title="🌍 Live Population Tracker", layout="wide")

st.title("🌍 Global Population Insights")
st.write("📊 A live demo tracker for births, deaths, and net population growth.")

# Constants (approx from UN / Worldometer)
POPULATION_2025 = 8_100_000_000
BIRTHS_PER_YEAR = 140_000_000
DEATHS_PER_YEAR = 60_000_000
SECONDS_PER_YEAR = 365 * 24 * 60 * 60

# Per second rates
births_per_sec = BIRTHS_PER_YEAR / SECONDS_PER_YEAR
deaths_per_sec = DEATHS_PER_YEAR / SECONDS_PER_YEAR
growth_per_sec = births_per_sec - deaths_per_sec

# Reference start time
if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()

# Elapsed time since app started
elapsed = time.time() - st.session_state.start_time

# Calculations
current_population = int(POPULATION_2025 + (elapsed * growth_per_sec))
births_so_far = int(elapsed * births_per_sec)
deaths_so_far = int(elapsed * deaths_per_sec)

# Layout
col1, col2, col3 = st.columns(3)
col1.metric("🌍 Current Population", f"{current_population:,}")
col2.metric("👶 Births since start", f"{births_so_far:,}")
col3.metric("⚰️ Deaths since start", f"{deaths_so_far:,}")

st.subheader("📅 Yearly / Monthly Estimates")
st.write(f"👶 Births per year: {BIRTHS_PER_YEAR:,}")
st.write(f"⚰️ Deaths per year: {DEATHS_PER_YEAR:,}")
st.write(f"📈 Net growth per year: {BIRTHS_PER_YEAR - DEATHS_PER_YEAR:,}")
st.write(f"👶 Births per month: {BIRTHS_PER_YEAR // 12:,}")
st.write(f"⚰️ Deaths per month: {DEATHS_PER_YEAR // 12:,}")

st.info("ℹ️ Data based on UN & Worldometer global estimates (demo version).")

