import pandas as pd

from src.data import types


def _configure_info_df(raw: pd.DataFrame) -> None:
    """Configure the information portion of the CSV file for proper use.

    Currently, fairly primitive, just fixes the index to the actual index column.
    NOTE: WORKS IN PLACE.

    Args:
        raw: unprocessed information portion of the original CSV file as DataFrame.

    Returns:
        None."""
    raw.set_index(0, inplace=True)
    return None


def _configure_measurement_s(measurement: pd.Series, information: pd.DataFrame) -> pd.Series:
    """Configure the measurement portion of the CSV file for proper use, using the processed
    information portion..

    Currently fixes the index to be measured in actual seconds, instead of amount of measurements, and fixes
    the datatype.

    Args:
        measurement: unprocessed measurements portion from original CSV file.
        information: processed information portion from original CSV file.

    Returns:
        Processed measurement DataFrame."""
    measurement.reset_index(drop=True, inplace=True)
    measurement = pd.to_numeric(measurement)

    measurement.index = measurement.index / int(information.loc["Meetfrequentie", 1])

    return measurement


def process(raw: pd.DataFrame) -> types.InformationMeasurementCombo:
    """Split and process the raw CSV file as DataFrame into an information portion, and a measurement portion,
    ready for use.

    Args:
        raw: unprocessed CSV file as DataFrame.

    Returns:
        Processed information and measurement portions, ready for use."""
    information_df = raw.loc[:7, :2]
    _configure_info_df(information_df)

    measurement_s = raw.loc[13:, 0]
    measurement_s = _configure_measurement_s(measurement_s, information_df)

    return (information_df, measurement_s)
