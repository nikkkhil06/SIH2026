# Fuel Consumption Predictor

## 1. Overview

This package contains the production-ready Random Forest model for predicting vessel momentary fuel consumption.

Target: `Consumer_Total_MomentaryFuel`

Output unit: `kg/s`

The predictor accepts seven vessel/environmental input features and returns predicted momentary fuel consumption.

## 2. Model

Model type: `RandomForestRegressor`

- Number of trees: 200
- Maximum depth: 20
- Minimum samples per leaf: 5
- Random state: 42
- Training samples: 82,395
- Test samples: 20,599

## 3. Input Features

| Feature | Unit |
|---|---|
| Ship_SpeedThroughWater | m/s |
| Environment_SeaFloorDepth | m |
| Weather_Temperature2M | °C |
| Weather_WindSpeed10M | m/s |
| Weather_WaveHeight | m |
| Weather_WavePeriod | s |
| Weather_OceanCurrentVelocity | m/s |

**Important:** Feature names and feature order are part of the production model contract.

### SOG vs STW

The model was trained using `Ship_SpeedThroughWater` (STW).

It was not trained using `Ship_SpeedOverGround` (SOG).

AIS SOG must therefore not be directly substituted for STW without an appropriate transformation or modeling decision.

## 4. Output

The predictor returns `Consumer_Total_MomentaryFuel` in `kg/s`.

## 5. Model Performance

Evaluation was performed on 20,599 held-out test observations.

| Metric | Value |
|---|---:|
| MAE | 0.049754 kg/s |
| RMSE | 0.068637 kg/s |
| R² | 0.981724 |

These metrics represent performance on the held-out dataset and are not a guarantee of identical performance on future real-world data.

## 6. Package Structure

```text
fuel_predictor_production/
├── fuel_rf_model.joblib
├── metadata.json
├── predictor.py
├── requirements.txt
└── README.md
```

## 7. Files

- `fuel_rf_model.joblib` — serialized trained Random Forest model
- `metadata.json` — model metadata, features, units, parameters and metrics
- `predictor.py` — production inference interface
- `requirements.txt` — pinned Python dependencies
- `README.md` — usage and integration documentation

## 8. Environment

Python version: `3.11.4`

Required packages:

```text
numpy==1.26.4
pandas==2.3.3
scikit-learn==1.9.0
joblib==1.5.3
```

## 9. Installation

Create or activate a Python 3.11 environment and run:

```bash
pip install -r requirements.txt
```

## 10. Single Prediction

```python
from predictor import FuelPredictor

predictor = FuelPredictor(
    'fuel_rf_model.joblib'
)

data = {
    'Ship_SpeedThroughWater': 5.5,
    'Environment_SeaFloorDepth': 100.0,
    'Weather_Temperature2M': 20.0,
    'Weather_WindSpeed10M': 5.0,
    'Weather_WaveHeight': 1.2,
    'Weather_WavePeriod': 6.0,
    'Weather_OceanCurrentVelocity': 0.5
}

fuel = predictor.predict(data)

print(f'Predicted fuel consumption: {fuel:.6f} kg/s')
```

Expected result for this test input:

`0.581898 kg/s`

## 11. Batch Prediction

```python
import pandas as pd
from predictor import FuelPredictor

predictor = FuelPredictor(
    'fuel_rf_model.joblib'
)

predictions = predictor.predict_batch(dataframe)
```

The result is a pandas Series containing predicted fuel consumption in kg/s.

## 12. Input Validation

The production predictor validates:

- missing features
- unexpected features
- missing/NaN values
- incorrect input type
- non-numeric values
- model feature compatibility

Invalid input raises an appropriate exception instead of silently producing a prediction.

## 13. Verification Completed

- Feature contract verified
- Held-out test validation completed
- Negative prediction check completed
- NaN prediction check completed
- Infinite prediction check completed
- Saved model successfully reloaded
- Reloaded model produced identical predictions
- Single-row production prediction verified
- Batch prediction verified on 20,599 observations
- Batch predictions matched the original model exactly

Maximum prediction difference after reloading:

`0.000000000000`

## 14. Limitations

1. The model expects STW, not AIS SOG.
2. Input units must match the documented units.
3. Predictions outside the training-data distribution may be unreliable.
4. Reported metrics come from the held-out test dataset.
5. Production deployment should monitor input distribution drift.
6. Retraining/versioning should be considered when operational data changes significantly.

## 15. Version

Model version: `1.0.0`

Model name: `fuel_consumption_random_forest`

Target: `Consumer_Total_MomentaryFuel`