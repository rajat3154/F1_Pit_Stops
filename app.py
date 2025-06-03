import streamlit as st
import pickle
import pandas as pd
import math

# Load trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("Pit Stop Prediction")

st.subheader("Enter Race and Weather Details")

# Manual input fields
driverId = st.number_input('Driver ID', value=843.0)
constructorId = st.number_input('Constructor ID', value=5.0)
grid = st.number_input('Grid Position', value=16.0)
positionOrder = st.number_input('Final Position Order', value=15.0)
laps = st.number_input('Number of Laps', value=57.0)
AirTemp = st.number_input('Air Temperature (°C)', value=24.0)
Humidity = st.number_input('Humidity (%)', value=36.3)
Pressure = st.number_input('Pressure (hPa)', value=997.1)
Rainfall = st.checkbox('Rainfall Present?', value=False)
TrackTemp = st.number_input('Track Temperature (°C)', value=38.6)

# Prepare input for model prediction
input_data = pd.DataFrame({
    'driverId': [driverId],
    'constructorId': [constructorId],
    'grid': [grid],
    'positionOrder': [positionOrder],
    'laps': [laps],
    'AirTemp': [AirTemp],
    'Humidity': [Humidity],
    'Pressure': [Pressure],
    'Rainfall': [int(Rainfall)],
    'TrackTemp': [TrackTemp]
})

# Predict button
if st.button('Predict Number of Pit Stops'):
    prediction = model.predict(input_data)
    pred_value = prediction[0]
    decimal_part = pred_value - int(pred_value)

    # Apply your custom rule
    if decimal_part >= 0.70:
        predicted_pitstops = math.ceil(pred_value)
    else:
        predicted_pitstops = int(pred_value)

    st.success(f'Predicted Number of Pit Stops: {predicted_pitstops}')
#     st.info(f'(Raw model output: {pred_value:.2f})')

