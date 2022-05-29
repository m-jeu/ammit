from typing import Tuple

import pandas as pd


# Because the files we're loading come combined as both a portion that contains information about the measurements
# and the actual measurements, we'll combine both in one datatype so we can easily pass them together.
InformationMeasurementCombo = Tuple[pd.DataFrame, pd.DataFrame]