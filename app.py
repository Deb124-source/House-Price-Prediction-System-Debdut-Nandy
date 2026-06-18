import streamlit as st
import pickle
import json
import numpy as np


# -------------------------
# Load Model
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


model, columns = load_artifacts()



# -------------------------
# Prediction Logic
# -------------------------

def predict_price(location, sqft, bath, bhk):

    input_data = np.zeros(len(columns))


    # first 3 columns
    input_data[0] = sqft
    input_data[1] = bath
    input_data[2] = bhk


    if location in columns:

        loc_index = columns.index(location)

        input_data[loc_index] = 1


    prediction = model.predict([input_data])[0]


    return round(prediction,2)



# -------------------------
# Streamlit UI
# -------------------------


st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠"
)



st.title("🏠 Bangalore House Price Prediction")

st.write(
    "Predict Bangalore house prices using Machine Learning"
)



locations = columns[3:]


location = st.selectbox(
    "Select Location",
    locations
)



sqft = st.number_input(
    "Total Square Feet",
    min_value=300,
    value=1000
)



bhk = st.number_input(
    "Number of Bedrooms",
    min_value=1,
    max_value=10,
    value=2
)



bath = st.number_input(
    "Number of Bathrooms",
    min_value=1,
    max_value=10,
    value=2
)



if st.button("Predict Price"):


    result = predict_price(
        location,
        sqft,
        bath,
        bhk
    )


    st.success(
        f"Estimated Price: ₹ {result} Lakhs"
    )



st.markdown("---")

st.caption(
    "Machine Learning Model | Streamlit Deployment"
)
