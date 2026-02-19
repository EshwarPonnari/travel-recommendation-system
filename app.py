import streamlit as st
import pandas as pd

st.title("Smart Travel Recommendation System")

data = {
    "Destination": ["London", "Paris", "Dubai", "Singapore", "Rome"],
    "Price": [800, 650, 700, 900, 600],
    "Rating": [4.8, 4.6, 4.5, 4.7, 4.4]
}

df = pd.DataFrame(data)

budget = st.slider("Select your budget ($)", 500, 1000, 700)

traveler_type = st.selectbox(
    "Traveller Type",
    ["Budget Traveller", "Luxury Traveller", "Family Traveller"]
)

filtered = df[df["Price"] <= budget]

if traveler_type == "Luxury Traveller":
    filtered = filtered.sort_values("Rating", ascending=False)

st.subheader("Recommended Destinations")
st.write(filtered)
