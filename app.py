import streamlit as st
import pandas as pd
import numpy as np
import joblib
import json


# -----------------------------
# Page Config
# -----------------------------

st.set_page_config(
    page_title="HousePrice AI",
    page_icon="🏠",
    layout="centered"
)


# -----------------------------
# Load Assets
# -----------------------------

model = joblib.load("house_price_model.pkl")

with open("columns.json", "r") as f:
    data_columns = json.load(f)["data_columns"]


locations = sorted(data_columns[3:])


# -----------------------------
# Prediction Function
# -----------------------------

def predict_price(location, sqft, bath, bhk):

    x = np.zeros(len(data_columns))

    x[0] = sqft
    x[1] = bath
    x[2] = bhk

    if location.lower() in data_columns:
        loc_index = data_columns.index(location.lower())
        x[loc_index] = 1

    prediction = model.predict([x])[0]

    return round(prediction, 2)


# -----------------------------
# UI
# -----------------------------

st.title("🏠 HousePrice AI")
st.subheader("AI Powered House Price Prediction")

st.write(
    "Enter property details below to estimate the house price."
)

location = st.selectbox(
    "📍 Location",
    locations
)

col1, col2 = st.columns(2)

with col1:
    sqft = st.number_input(
        "📐 Total Sqft",
        min_value=100,
        value=1200
    )

with col2:
    bath = st.number_input(
        "🛁 Bathrooms",
        min_value=1,
        value=2
    )

col3, col4 = st.columns(2)

with col3:
    bhk = st.number_input(
        "🏡 BHK",
        min_value=1,
        value=2
    )

with col4:
    st.empty()


if st.button("🔮 Predict Price"):

    price = predict_price(
        location,
        sqft,
        bath,
        bhk
    )

    st.success(
        f"Estimated House Price: ₹ {price:.2f} Lakhs"
    )
