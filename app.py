import streamlit as st
import pandas as pd
import pickle

with open('model.pkl', 'rb') as f:
    pipe = pickle.load(f)

tier1_company = ['MG', 'Skoda', 'KIA', 'Mahindra', 'Toyota']
tier2_company = ['Ford', 'Volkswagen', 'Nissan', 'Tata', 'Hyundai', 'Honda']
high_demand_cities = ['noida', 'new-delhi', 'new delhi', 'jaipur', 'vadodra', 'hyderabad', 'nagpur', 'pune', 'surat', 'coimbatore', 'ghaziabad', 'chennai', 'kochi', 'agra', 'patna', 'indore', 'nashik',]
less_demand_cities = ['rajkot', 'kolkata', 'mumbai', 'ahmedabad', 'bangalore']


st.title("Used car price predictor")

st.header("please provide the below information")

company = st.text_input('Company of the selling car : (Hyundai, Mahindra, Honda, Maruti, Renault, Skoda, Tata, Ford, Volkswagen, Datsun, Nissan, MG, Toyota, KIA)', value='Tata')
model_year = st.number_input('Provide the registration year of the car', value=2020)
fuel = st.selectbox('Provide the fuel that car runs on ', ['Petrol', 'Diesel', 'CNG', 'other'])
car_type = st.selectbox('Provide the tranferom type of the car ', ['Manual', 'Auto'])
distance = st.number_input("Distance travelled before selling in KM ", value=55000)
ownership = st.selectbox("Provide the ownership type of selling car ", ['1st owner', '2nd owner', '3 and above'])

availabe_loc = ['bangalore', 'mumbai', 'hyderabad', 'chennai', 'pune', 'new-delhi',
       'noida', 'jaipur', 'kochi', 'nashik', 'nagpur', 'indore', 'patna',
       'surat', 'coimbatore', 'ghaziabad', 'kolkata', 'ahmedabad',
       'rajkot', 'vadodra', 'agra']
location = st.selectbox("Provide the location of the car being sold", availabe_loc)

test_data = pd.DataFrame([{
    'company' : company,
    'model(year)' : model_year,
    'fuel' : fuel,
    'car type' : car_type,
    'distance' : distance,
    'ownership' : ownership,
    'location' : location
}])

def car_tier(comp):
    if comp in tier1_company:
        return 1
    elif comp in tier2_company:
        return 2
    return 3

def city_tier(location):
    if location in high_demand_cities:
        return 0
    elif location in less_demand_cities:
        return 1
    return 2

def ownership_handler(own):
    if own == '1st owner':
        return 1
    elif own == '2nd owner' :
        return 2
    return 3

test_data['ownership'] = test_data['ownership'].apply(ownership_handler)
test_data['car company tier'] = test_data['company'].str.lower().apply(car_tier)
test_data['demand frequency'] = test_data['location'].apply(city_tier)
test_data['KM per year'] = (test_data['distance'] / (2025-test_data['model(year)']))

if st.button("Predict price"):
    # st.write("The data provided : ", test_data)
    t_data = test_data[['model(year)', 'fuel', 'car type', 'ownership', 'car company tier',
       'demand frequency', 'KM per year']]
    t_prediction = pipe.predict(t_data)
    st.success(f"Predicted car price in RS : {round(t_prediction[0])} ")
    













    