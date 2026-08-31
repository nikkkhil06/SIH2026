import sys
from pathlib import Path

import numpy as np
import pandas as pd


# ------------------------------------------------------------
# Resolve production directory
# ------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

MODEL_PATH = BASE_DIR / "fuel_rf_model.joblib"

sys.path.insert(0, str(BASE_DIR))

from predictor import FuelPredictor


# ------------------------------------------------------------
# Test data
# ------------------------------------------------------------

SAMPLE_INPUT = {
    "Ship_SpeedThroughWater": 5.5,
    "Environment_SeaFloorDepth": 100.0,
    "Weather_Temperature2M": 20.0,
    "Weather_WindSpeed10M": 5.0,
    "Weather_WaveHeight": 1.2,
    "Weather_WavePeriod": 6.0,
    "Weather_OceanCurrentVelocity": 0.5
}


# ------------------------------------------------------------
# Test 1 — Model loading
# ------------------------------------------------------------

def test_model_loading():

    assert MODEL_PATH.exists(), (
        f"Model not found: {MODEL_PATH}"
    )

    predictor = FuelPredictor(str(MODEL_PATH))

    assert predictor.model is not None

    print("PASS: Model loading")


# ------------------------------------------------------------
# Test 2 — Feature contract
# ------------------------------------------------------------

def test_feature_contract():

    predictor = FuelPredictor(str(MODEL_PATH))

    expected_features = [
        "Ship_SpeedThroughWater",
        "Environment_SeaFloorDepth",
        "Weather_Temperature2M",
        "Weather_WindSpeed10M",
        "Weather_WaveHeight",
        "Weather_WavePeriod",
        "Weather_OceanCurrentVelocity"
    ]

    assert predictor.FEATURES == expected_features

    assert list(
        predictor.model.feature_names_in_
    ) == expected_features

    print("PASS: Feature contract")


# ------------------------------------------------------------
# Test 3 — Single prediction
# ------------------------------------------------------------

def test_single_prediction():

    predictor = FuelPredictor(str(MODEL_PATH))

    result = predictor.predict(SAMPLE_INPUT)

    assert isinstance(result, float)
    assert np.isfinite(result)
    assert result >= 0

    # Known prediction for this test input
    expected = 0.581898

    assert np.isclose(
        result,
        expected,
        rtol=1e-5,
        atol=1e-6
    )

    print("PASS: Single prediction")


# ------------------------------------------------------------
# Test 4 — Missing feature
# ------------------------------------------------------------

def test_missing_feature():

    predictor = FuelPredictor(str(MODEL_PATH))

    data = SAMPLE_INPUT.copy()
    del data["Weather_WaveHeight"]

    try:
        predictor.predict(data)
        assert False, "Expected ValueError"
    except ValueError as error:
        assert "Weather_WaveHeight" in str(error)

    print("PASS: Missing feature validation")


# ------------------------------------------------------------
# Test 5 — Unexpected feature
# ------------------------------------------------------------

def test_unexpected_feature():

    predictor = FuelPredictor(str(MODEL_PATH))

    data = SAMPLE_INPUT.copy()
    data["Extra_Feature"] = 123

    try:
        predictor.predict(data)
        assert False, "Expected ValueError"
    except ValueError as error:
        assert "Extra_Feature" in str(error)

    print("PASS: Unexpected feature validation")


# ------------------------------------------------------------
# Test 6 — NaN value
# ------------------------------------------------------------

def test_nan_value():

    predictor = FuelPredictor(str(MODEL_PATH))

    data = SAMPLE_INPUT.copy()
    data["Weather_WaveHeight"] = np.nan

    try:
        predictor.predict(data)
        assert False, "Expected ValueError"
    except ValueError as error:
        assert "missing value" in str(error).lower()

    print("PASS: NaN validation")


# ------------------------------------------------------------
# Test 7 — Wrong input type
# ------------------------------------------------------------

def test_wrong_input_type():

    predictor = FuelPredictor(str(MODEL_PATH))

    try:
        predictor.predict(["invalid"])
        assert False, "Expected TypeError"
    except TypeError as error:
        assert "dictionary" in str(error).lower()

    print("PASS: Input type validation")


# ------------------------------------------------------------
# Test 8 — Non-numeric feature
# ------------------------------------------------------------

def test_non_numeric():

    predictor = FuelPredictor(str(MODEL_PATH))

    data = SAMPLE_INPUT.copy()
    data["Ship_SpeedThroughWater"] = "5.5"

    try:
        predictor.predict(data)
        assert False, "Expected TypeError"
    except TypeError as error:
        assert "numeric" in str(error).lower()

    print("PASS: Numeric validation")


# ------------------------------------------------------------
# Test 9 — Batch prediction
# ------------------------------------------------------------

def test_batch_prediction():

    predictor = FuelPredictor(str(MODEL_PATH))

    dataframe = pd.DataFrame([
        SAMPLE_INPUT,
        SAMPLE_INPUT,
        SAMPLE_INPUT
    ])

    predictions = predictor.predict_batch(dataframe)

    assert isinstance(predictions, pd.Series)
    assert len(predictions) == 3
    assert np.all(np.isfinite(predictions))
    assert np.all(predictions >= 0)

    expected = 0.581898

    assert np.allclose(
        predictions.to_numpy(),
        expected,
        rtol=1e-5,
        atol=1e-6
    )

    print("PASS: Batch prediction")


# ------------------------------------------------------------
# Run tests
# ------------------------------------------------------------

if __name__ == "__main__":

    print("=" * 60)
    print("FUEL PREDICTOR PRODUCTION TEST SUITE")
    print("=" * 60)

    tests = [
        test_model_loading,
        test_feature_contract,
        test_single_prediction,
        test_missing_feature,
        test_unexpected_feature,
        test_nan_value,
        test_wrong_input_type,
        test_non_numeric,
        test_batch_prediction
    ]

    passed = 0

    for test in tests:

        try:
            test()
            passed += 1

        except Exception as error:

            print(f"FAIL: {test.__name__}")
            print(f"      {error}")

    print()
    print("=" * 60)
    print(f"RESULT: {passed}/{len(tests)} tests passed")
    print("=" * 60)

    if passed == len(tests):
        print("ALL PRODUCTION TESTS PASSED")
        sys.exit(0)

    else:
        print("PRODUCTION TESTS FAILED")
        sys.exit(1)
