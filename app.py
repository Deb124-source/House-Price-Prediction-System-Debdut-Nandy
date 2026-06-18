import streamlit as st
import pickle
import json
import numpy as np


# -------------------------
# Page Configuration
# -------------------------

st.set_page_config(
    page_title="Bangalore House Price Prediction",
    page_icon="🏠",
    layout="centered"
)


# -------------------------
# Load Model + Columns
# -------------------------

@st.cache_resource
def load_artifacts():

    with open(
        "model/bengaluru_house_prices_model.pickle",
        "rb"
    ) as file:
        model = pickle.load(file)


    with open(
        "model/columns.json",
        "r"
    ) as file:
        columns = json.load(file)["data_columns"]


    return model, columns



try:

    model, columns = load_artifacts()

except Exception as e:

    st.error("Model loading failed")
    st.write(e)
    st.stop()



# -------------------------
# Prediction Function
# -------------------------

def predict_price(location, sqft, bath, bhk):


    input_data = np.zeros(len(columns))


    # Find exact column positions

    if "total_sqft" in columns:
        sqft_index = columns.index("total_sqft")
        input_data[sqft_index] = sqft


    if "bath" in columns:
        bath_index = columns.index("bath")
        input_data[bath_index] = bath


    if "bhk" in columns:
        bhk_index = columns.index("bhk")
        input_data[bhk_index] = bhk



    # Location encoding

    if location in columns:

        location_index = columns.index(location)

        input_data[location_index] = 1



    prediction = model.predict(
        [input_data]
    )[0]


    return round(prediction,2)




# -------------------------
# UI Design
# -------------------------

st.title(
    "🏠 Bangalore House Price Prediction"
)


st.write(
    """
    Predict Bangalore house prices using a Machine Learning model.
    
    Enter house details below:
    """
)



st.divider()



# Location

locations = columns[3:]


location = st.selectbox(
    "Select Location",
    locations
)



# Square Feet

sqft = st.number_input(
    "Total Square Feet",
    min_value=300,
    max_value=10000,
    value=1000
)



# BHK

bhk = st.number_input(
    "Number of Bedrooms (BHK)",
    min_value=1,
    max_value=10,
    value=2
)



# Bathroom

bath = st.number_input(
    "Number of Bathrooms",
    min_value=1,
    max_value=10,
    value=2
)




# Prediction Button

if st.button(
    "Predict Price",
    use_container_width=True
):


    result = predict_price(
        location,
        sqft,
        bath,
        bhk
    )


    st.success(
        f"Estimated Price: ₹ {result} Lakhs"
    )


    st.info(
        "Prediction is based on historical Bangalore housing data."
    )




st.divider()


st.caption(
    "Machine Learning Model | Scikit-Learn | Streamlit Deployment"
)
