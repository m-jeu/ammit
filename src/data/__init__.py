from .types import InformationMeasurementCombo
from .load import fetch
from .preprocessing import process


def fetch_and_process() -> InformationMeasurementCombo:
    raw = fetch()  # FIXME(m-jeu): Don't throw exception on but propagate None.
    return process(raw) if raw is not None else None
