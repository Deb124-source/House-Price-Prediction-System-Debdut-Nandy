import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None


def get_location_names():
    return __locations


def get_estimated_price(location, total_sqft, bhk, bath):
    try:
        # Find index in full data columns (IMPORTANT FIX)
        loc_index = __data_columns.index(location.strip().lower())
    except:
        loc_index = -1

    # Create input array
    x = np.zeros(len(__data_columns))

    x[0] = float(total_sqft)
    x[1] = float(bath)
    x[2] = float(bhk)

    # Set location encoding
    if loc_index >= 0:
        x[loc_index] = 1

    # Predict price
    price = round(__model.predict([x])[0], 2)

    # Debug log (helps during testing)
    print(f"Debug: loc={location}, idx={loc_index}, sqft={total_sqft}, bhk={bhk}, bath={bath}, price={price}")

    return price


def load_saved_artifacts():
    print("Loading saved artifacts...start")

    global __data_columns
    global __locations
    global __model

    # Load column names
    with open("server/artifacts/columns.json", 'r') as f:
        __data_columns = json.load(f)["data_columns"]
        __locations = __data_columns[3:]
        print("Data columns loaded...done")

    # Load trained model
    with open("server/artifacts/bengaluru_house_prices_model.pickle", 'rb') as f:
        __model = pickle.load(f)
        print("Model loaded successfully.")


if __name__ == '__main__':
    load_saved_artifacts()

    print(get_location_names())

    # Test predictions
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('1st Phase JP Nagar', 2000, 3, 3))
    print(get_estimated_price('Indira Nagar', 1500, 3, 2))
