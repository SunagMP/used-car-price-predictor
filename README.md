Used Car Price Predictor 🚗💰
==============================

Overview
--------
This project is a Machine Learning-based web application that predicts the resale price of used cars. The dataset was scraped from the Car24 website and includes various features such as car brand, model, registration year, fuel type, transmission type, distance driven, ownership type, and location.

Key Features
------------
✅ Scraped real-world data from Car24  
✅ Trained a regression model to predict car prices  
✅ Developed two interfaces:
   - **Streamlit Web App** (for interactive frontend UI)
   - **FastAPI Backend** with a `/predict` endpoint for API-based access  
✅ Deployed live using Render

Live Demo
---------
🌐 Streamlit App:  
https://used-car-price-predictor-wuhl.onrender.com/

Usage
-----
You can interact with the app in two ways:

1. **Streamlit Interface** (Recommended for end users)
   - Visit the live URL above.
   - Input details of the used car.
   - Get an instant price prediction.

2. **FastAPI Backend**
   - Access the prediction endpoint at `/predict`.
   - Example POST request:
     ```
     POST /predict
     Content-Type: application/json

     {
       "company": "Maruti",
       "car_model": "Swift",
       "registration_year": 2017,
       "fuel_type": "Petrol",
       "transmission_type": "Manual",
       "distance_driven": 48000,
       "ownership": "First Owner",
       "location": "Bangalore"
     }
     ```

Technology Stack
----------------
- Python
- Scikit-learn
- Pandas
- Streamlit
- FastAPI
- Render (for deployment)

Author
--------------------
Developed by Sunag M P  
Feel free to connect and contribute!
