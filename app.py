import streamlit as st
import pickle
import pandas as pd

# # Load model
# with open("model.pkl", "rb") as f:
#     model = pickle.load(f)
import joblib

model = joblib.load("model.pkl")

st.title("🏠 California House Price Prediction")

st.write("Enter house details below:")

# Numeric inputs
longitude = st.number_input("Longitude", value=-122.23)
latitude = st.number_input("Latitude", value=37.88)
housing_median_age = st.number_input("Housing Median Age", value=20.0)
total_rooms = st.number_input("Total Rooms", value=1000.0)
total_bedrooms = st.number_input("Total Bedrooms", value=200.0)
population = st.number_input("Population", value=500.0)
households = st.number_input("Households", value=200.0)
median_income = st.number_input("Median Income", value=3.0)

# Categorical input
ocean_proximity = st.selectbox(
    "Ocean Proximity",
    ["<1H OCEAN", "INLAND", "ISLAND", "NEAR OCEAN", "NEAR BAY"]
)

# Predict
if st.button("Predict Price"):
    input_data = pd.DataFrame([{
        "longitude": longitude,
        "latitude": latitude,
        "housing_median_age": housing_median_age,
        "total_rooms": total_rooms,
        "total_bedrooms": total_bedrooms,
        "population": population,
        "households": households,
        "median_income": median_income,
        "ocean_proximity": ocean_proximity
    }])

    prediction = model.predict(input_data)

    st.success(f"Predicted House Price: ${prediction[0]:,.2f}")