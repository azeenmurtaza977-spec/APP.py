import streamlit as st

# Page config
st.set_page_config(page_title="📊 Population Insights Demo", layout="wide")

# Title
st.title("🌍 Population Insights (Sample App)")

# Sidebar
st.sidebar.header("⚙️ Options")
option = st.sidebar.selectbox("Select a view:", ["Overview", "Trends", "About"])

# Main Area
if option == "Overview":
    st.subheader("📈 Population Overview")
    st.metric("World Population", "8 Billion")
    st.metric("Births per Year", "140 Million")
    st.metric("Deaths per Year", "60 Million")

elif option == "Trends":
    st.subheader("📊 Trends (Sample Data)")
    st.line_chart({"Population (B)": [1, 2, 3, 4, 5, 6, 7, 8]})

elif option == "About":
    st.subheader("ℹ️ About This App")
    st.write("""
        This is a **demo app template** created with Streamlit.  
        - Sidebar to switch views  
        - Metrics and charts for insights  
        - Fully customizable for your own data  
    """)




    
