from flask import Flask, request, jsonify
from flask_cors import CORS
CORS(app)
import util
util.load_saved_artifacts()

app = Flask(__name__)

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqft = request.form['total_sqft']
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])   # FIXED space issue

    response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft, bhk, bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    print("Starting Python Flask Server For House Price Prediction...")
    util.load_saved_artifacts()
    app.run(debug=True)
