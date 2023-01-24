from .data import *
from .graph import *


def fetch_and_show() -> None:
    info_and_measure = fetch_and_process()
    if info_and_measure is not None:
        fig = make(info_and_measure[1])
        fig.show()
