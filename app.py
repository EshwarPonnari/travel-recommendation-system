import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Travel Decision Intelligence", layout="wide")

st.title("🌍 Travel Decision Intelligence Dashboard")
st.markdown("Built by **Eshwar Ponnari** | Inspired by real traveller workflows in global travel platforms")

# Sidebar Controls
st.sidebar.header("✈ Traveller Preferences")
budget = st.sidebar.slider("Budget ($)", 500, 1500, 800)
traveler_type = st.sidebar.selectbox(
    "Traveller Type",
    ["Budget Traveller", "Luxury Traveller", "Family Traveller"]
)

# Sample dataset
data = {
    "Destination": ["London", "Paris", "Dubai", "Singapore", "Rome"],
    "Price": [1200, 850, 900, 1300, 750],
    "Rating": [4.8, 4.6, 4.5, 4.7, 4.4],
    "Popularity_Index": [95, 88, 90, 92, 80]
}

df = pd.DataFrame(data)

# Filter by budget
df = df[df["Price"] <= budget]

if df.empty:
    st.warning("No destinations match your budget.")
    st.stop()

# Scoring Logic (Simulated Recommendation Engine)
def calculate_score(row):
    rating_weight = 0.4
    price_weight = 0.3
    popularity_weight = 0.3

    if traveler_type == "Luxury Traveller":
        rating_weight = 0.6
        price_weight = 0.1
    elif traveler_type == "Budget Traveller":
        rating_weight = 0.3
        price_weight = 0.5

    score = (
        (row["Rating"] * rating_weight) +
        ((1 / row["Price"]) * 1000 * price_weight) +
        (row["Popularity_Index"] / 100 * popularity_weight)
    )
    return round(score, 2)

df["Recommendation_Score"] = df.apply(calculate_score, axis=1)

# Simulated booking probability
df["Booking_Probability (%)"] = np.random.randint(60, 95, size=len(df))

df = df.sort_values("Recommendation_Score", ascending=False)

# Mark Best Value
df["Best_Value"] = df["Recommendation_Score"] == df["Recommendation_Score"].max()

# Layout
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📊 Ranked Recommendations")
    st.dataframe(df)

with col2:
    st.subheader("📈 Score Visualization")
    st.bar_chart(df.set_index("Destination")["Recommendation_Score"])

st.success("Recommendations ranked dynamically using multi-factor scoring logic.")

