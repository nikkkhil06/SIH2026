from app.schemas.prediction import PredictionRequest
from app.ML.fuel_predictor.predictor import FuelPredictor


MODEL_PATH = "app/ML/fuel_predictor/fuel_rf_model.joblib"

predictor = FuelPredictor(MODEL_PATH)


def predict_fuel(data: PredictionRequest):

    model_input = {
        "Ship_SpeedThroughWater": data.ship_speed_through_water,
        "Environment_SeaFloorDepth": data.sea_floor_depth,
        "Weather_Temperature2M": data.air_temperature,
        "Weather_WindSpeed10M": data.wind_speed,
        "Weather_WaveHeight": data.wave_height,
        "Weather_WavePeriod": data.wave_period,
        "Weather_OceanCurrentVelocity": data.ocean_current_velocity,
    }

    predicted_fuel = predictor.predict(model_input)

    return {
        "predicted_fuel": predicted_fuel,
        "fuel_unit": "kg/s",
    }