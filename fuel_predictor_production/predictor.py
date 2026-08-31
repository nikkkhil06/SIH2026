import os
import joblib
import pandas as pd


class FuelPredictor:
    """
    Production interface for the Random Forest
    fuel-consumption prediction model.

    Output unit:
        kg/s
    """

    FEATURES = [
        "Ship_SpeedThroughWater",
        "Environment_SeaFloorDepth",
        "Weather_Temperature2M",
        "Weather_WindSpeed10M",
        "Weather_WaveHeight",
        "Weather_WavePeriod",
        "Weather_OceanCurrentVelocity"
    ]

    TARGET = "Consumer_Total_MomentaryFuel"

    UNITS = {
        "Ship_SpeedThroughWater": "m/s",
        "Environment_SeaFloorDepth": "m",
        "Weather_Temperature2M": "°C",
        "Weather_WindSpeed10M": "m/s",
        "Weather_WaveHeight": "m",
        "Weather_WavePeriod": "s",
        "Weather_OceanCurrentVelocity": "m/s"
    }

    def __init__(self, model_path):
        if not os.path.exists(model_path):
            raise FileNotFoundError(
                f"Model file not found: {model_path}"
            )

        self.model = joblib.load(model_path)

        model_features = list(
            self.model.feature_names_in_
        )

        if model_features != self.FEATURES:
            raise ValueError(
                "Model feature contract does not match "
                "production feature contract."
            )

    def predict(self, data):
        """
        Predict fuel consumption for one observation.

        Parameters
        ----------
        data : dict
            Seven required model features.

        Returns
        -------
        float
            Predicted fuel consumption in kg/s.
        """

        if not isinstance(data, dict):
            raise TypeError(
                "Input must be a dictionary."
            )

        missing = [
            feature
            for feature in self.FEATURES
            if feature not in data
        ]

        if missing:
            raise ValueError(
                f"Missing required features: {missing}"
            )

        unexpected = [
            key
            for key in data
            if key not in self.FEATURES
        ]

        if unexpected:
            raise ValueError(
                f"Unexpected features provided: {unexpected}"
            )

        input_df = pd.DataFrame(
            [[data[feature] for feature in self.FEATURES]],
            columns=self.FEATURES
        )

        for feature in self.FEATURES:

            value = input_df[feature].iloc[0]

            if pd.isna(value):
                raise ValueError(
                    f"Feature '{feature}' contains "
                    "a missing value."
                )

            if not isinstance(value, (int, float)):
                raise TypeError(
                    f"Feature '{feature}' must be numeric."
                )

        prediction = self.model.predict(input_df)[0]

        return float(prediction)

    def predict_batch(self, data):
        """
        Predict fuel consumption for multiple observations.

        Parameters
        ----------
        data : pandas.DataFrame

        Returns
        -------
        pandas.Series
            Predicted fuel consumption in kg/s.
        """

        if not isinstance(data, pd.DataFrame):
            raise TypeError(
                "Batch input must be a pandas DataFrame."
            )

        missing = [
            feature
            for feature in self.FEATURES
            if feature not in data.columns
        ]

        if missing:
            raise ValueError(
                f"Missing required features: {missing}"
            )

        input_df = data[self.FEATURES].copy()

        if input_df.isnull().any().any():

            missing_columns = (
                input_df.columns[
                    input_df.isnull().any()
                ].tolist()
            )

            raise ValueError(
                f"Missing values found in: "
                f"{missing_columns}"
            )

        non_numeric = (
            input_df
            .select_dtypes(exclude="number")
            .columns
            .tolist()
        )

        if non_numeric:
            raise TypeError(
                f"Non-numeric features found: "
                f"{non_numeric}"
            )

        predictions = self.model.predict(input_df)

        return pd.Series(
            predictions,
            index=data.index,
            name=self.TARGET
        )