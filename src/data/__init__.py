from .types import InformationMeasurementCombo
from .load import fetch
from .preprocessing import process


def fetch_and_process() -> InformationMeasurementCombo:
    raw = fetch()
    return process(raw)
