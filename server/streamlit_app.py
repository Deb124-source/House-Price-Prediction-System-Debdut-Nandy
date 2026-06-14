import streamlit as st
import requests
import json

st.set_page_config(page_title="House Price Prediction", page_icon="🏠", layout="centered")
st.title("🏠 House Price Prediction")

st.write("Enter details to estimate house price.")

# ---- Inputs ----
col1, col2, col3, col4 = st.columns(4)
with col1:
    total_sqft = st.number_input("Total sqft", min_value=0.0, step=1.0, value=1000.0)
with col2:
    bhk = st.number_input("BHK", min_value=1, step=1, value=2)
with col3:
    bath = st.number_input("Bath", min_value=1, step=1, value=2)

# Location list: try to fetch from Flask server, else fallback to a basic list.
server_url = st.text_input("Flask server URL", value="http://127.0.0.1:5000")
locations = ["Indira Nagar", "1st Phase JP Nagar"]

try:
    r = requests.get(f"{server_url}/get_location_names", timeout=3)
    r.raise_for_status()
    data = r.json()
    if isinstance(data, dict) and "locations" in data and isinstance(data["locations"], list) and len(data["locations"]) > 0:
        locations = data["locations"]
except Exception:
    # Keep fallback locations
    pass

with col4:
    location = st.selectbox("Location", options=locations)

# ---- Predict ----
if st.button("Predict price", type="primary"):
    try:
        resp = requests.post(
            f"{server_url}/predict_home_price",
            data={
                "total_sqft": float(total_sqft),
                "location": location,
                "bhk": int(bhk),
                "bath": int(bath),
            },
            timeout=10,
        )
        resp.raise_for_status()
        payload = resp.json()
        estimated_price = payload.get("estimated_price")

        if estimated_price is None:
            st.error(f"Unexpected response: {payload}")
        else:
            st.success(f"Estimated Price: ₹ {estimated_price} lakhs")

    except Exception as e:
        st.error(
            "Failed to call the Flask backend. "
            "Make sure the Flask server is running and the URL is correct.\n\n"
            f"Error: {e}"
        )

st.caption("Backend: Flask API in server/server.py")
