# 🏠 House Price Prediction Web App

A full-stack Machine Learning web application that predicts house prices based on user inputs like location, square footage, BHK, and number of bathrooms. Built with a powerful combination of Python (Flask) for backend and a clean HTML/CSS/JavaScript frontend.<br><br>


## 🚀 Project Overview

This project demonstrates how a machine learning model can be deployed as a real-world web application. Instead of just training a model in a notebook, this system allows users to interact with it through a simple and intuitive UI.<br><br>


### Users can:
1. Enter property details
2. Select location
3. Get instant price predictions<br><br>

   
## 🧠 Machine Learning Model
Algorithm Used: Linear Regression
Dataset: Real estate housing dataset<br><br>


### Preprocessing:
Handling missing values
One-hot encoding for locations
Feature scaling (if applied)
Model Serialization: pickle<br><br>


## 🛠️ Tech Stack
Python<br>
Flask<br>
NumPy<br>
Scikit-Learn<br>
Pickle<br>
HTML<br>
CSS<br>
JavaScript<br>
VS Code<br>
Jupyter Notebook / Google Colab<br><br>


## 📂 Project Structure
![Structure](image.png)
<br><br>

## ⚙️ Features

✅ Predict house prices instantly<br>
✅ Clean and responsive UI<br>
✅ Dynamic location dropdown<br>
✅ REST API integration<br>
✅ Lightweight and fast<br><br>


## 🔌 How It Works
User enters:
Location<br>
Square feet<br>
BHK<br>
Bathrooms<br>
Frontend sends data to Flask API<br>
Backend processes input using trained model<br>
Predicted price is returned and displayed<br><br>

## 🧪 Sample Inputs for Demo
You can use these while showcasing your project:
<br>

Location	         Sqft	   BHK	  Bath   Expected Output<br>
Whitefield	      1200	    2     	2    	Moderate price<br>
Indiranagar	      2000   	 3	      3	   High price<br>
Electronic City 	900	    2	      1	   Lower price<br>
Yelahanka         1500	    3	      2   	Mid-high<br>
Hebbal	         1800	    3	      3	   Premium<br>
<br><br>

## ▶️ Running the Project
1. Clone the Repository:
git clone https://github.com/your-username/house-price-prediction.git

cd house-price-prediction

3. Install Dependencies:
pip install flask numpy
4. Run the Server:
python server/server.py
5. Open Frontend:
Simply open app.html in your browser
<br><br>

## 🌐 API Endpoint
POST /predict_home_price<br>
Parameters:
location<br>
total_sqft<br>
bhk<br>
bath<br>
<br><br>

## 🎯 Future Improvements
📊 Add advanced ML models (Random Forest, XGBoost)<br>
🌍 Deploy on cloud (AWS / Render / Vercel)<br>
📱 Make mobile responsive UI<br>
📈 Add price trend visualization<br>
🔐 User authentication system<br>
<br><br>

## 📸 Screenshot of the project
![App UI](demo_prediction.png)
<br><br>

## 🙌 Acknowledgements
Dataset inspiration from real estate listings<br>
Flask documentation<br>
<br><br>

## 📌 Conclusion
This project bridges the gap between Machine Learning and Web Development, making models usable in real-world scenarios. It’s a strong portfolio project showcasing both data science and full-stack skills.
