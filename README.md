# 🏁 F1 Pit Stop Predictor

A machine learning project that predicts the number of pit stops in a Formula 1 race based on race conditions, car data, and environmental parameters. This model is trained using a Linear Regression algorithm on historical F1 race data.

## 🚀 Project Overview

Pit stops play a crucial role in F1 race strategies. This project leverages machine learning to anticipate how many pit stops a driver might take, given race-specific and weather-related parameters.

### 📌 Year: 2023  
### 📌 Model: Linear Regression  
### 📌 Goal: Predict number of pit stops in a race  

---

## 📊 Features Used

- **Race Details:** Round, Lap, Laps, Stop
- **Driver & Team Info:** Driver ID, Constructor ID, Grid Position, Rank, Position Order
- **Performance:** Points, Milliseconds
- **Weather Conditions:**
  - Air Temperature (°C)
  - Track Temperature (°C)
  - Humidity (%)
  - Pressure (hPa)
  - Wind Speed (km/h)

---
## 📊 Features Used

The model is trained using the following input parameters:

- *Year*: Year of the race (e.g., 2023)
- *Round*: Round number in the season
- *Driver ID*: Unique identifier for the driver
- *Stop*: Number of pit stops (target for prediction)
- *Lap*: Current lap number
- *Milliseconds*: Time elapsed in milliseconds
- *Constructor ID*: Team/constructor identifier
- *Grid Position*: Starting grid position
- *Position Order*: Current race position
- *Points*: Points scored
- *Laps*: Total laps in the race
- *Rank*: Driver rank
- *Air Temperature (°C)*
- *Humidity (%)*
- *Pressure (hPa)*
- *Track Temperature (°C)*
- *Wind Speed (km/h)*

## 🔧 Model

We use the LinearRegression model from scikit-learn to train on the dataset and predict the Stop value.

### Requirements

- Python 3.8+
- scikit-learn
- pandas
- numpy
- matplotlib (optional, for visualizations)

### Installation


## 📥 Sample Input

```json
{
  "Year": 2023,
  "Round": 1,
  "Driver ID": 1,
  "Stop": 0,
  "Lap": 0,
  "Milliseconds": 1000,
  "Constructor ID": 1,
  "Grid Position": 1,
  "Position Order": 1,
  "Points": 0,
  "Laps": 50,
  "Rank": 1,
  "Air Temperature (°C)": 20.0,
  "Humidity (%)": 50.0,
  "Pressure (hPa)": 1013.25,
  "Track Temperature (°C)": 30.0,
  "Wind Speed (km/h)": 10.0
}

#
