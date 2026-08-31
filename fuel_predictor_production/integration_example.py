from predictor import FuelPredictor


# ------------------------------------------------------------
# Load production model
# ------------------------------------------------------------

predictor = FuelPredictor(
    "fuel_rf_model.joblib"
)


# ------------------------------------------------------------
# Example vessel/environment input
#
# IMPORTANT:
# Values must use the units specified in README.md.
# ------------------------------------------------------------

vessel_data = {
    "Ship_SpeedThroughWater": 5.5,
    "Environment_SeaFloorDepth": 100.0,
    "Weather_Temperature2M": 20.0,
    "Weather_WindSpeed10M": 5.0,
    "Weather_WaveHeight": 1.2,
    "Weather_WavePeriod": 6.0,
    "Weather_OceanCurrentVelocity": 0.5
}


# ------------------------------------------------------------
# Generate prediction
# ------------------------------------------------------------

fuel_consumption = predictor.predict(
    vessel_data
)


# ------------------------------------------------------------
# Display result
# ------------------------------------------------------------

print("=" * 60)
print("FUEL CONSUMPTION PREDICTION")
print("=" * 60)

print(f"Ship STW       : {vessel_data['Ship_SpeedThroughWater']} m/s")
print(
    f"Predicted fuel : "
    f"{fuel_consumption:.6f} kg/s"
)

print("=" * 60)
