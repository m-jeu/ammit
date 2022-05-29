from typing import Union

import tkinter as tk
from tkinter.filedialog import askopenfilename

import pandas as pd


def _user_file_select() -> str:
    """Ask the user to select a .csv file through the windows file explorer, through a tkinter window.

    Returns:
        File path of the selected file as string. File path will show as empty string when choice is not made by user."""
    tk.Tk().withdraw()
    path = askopenfilename(filetypes=[("Comma separated values", "*.csv")])
    return path


def _load_raw_csv(path: str) -> pd.DataFrame:
    """Load a CSV file with the specified formatting as discovered in exploration.ipynb.

    Args:
        path: path to load file from.

    Returns:
        Raw dataframe."""
    return pd.read_csv(path, delimiter=",", header=None)


def fetch() -> Union[pd.DataFrame, None]:
    """Ask user to select a file .CSV through _user_file_select(), and load selected file as Pandas dataframe
    with _load_raw_csv().

    File will only load properly if in specified formatting such as discovered in exploration.ipynb.

    Returns:
        Dataframe if file selection/load successful, None otherwise."""
    if (path := _user_file_select()) == "":
        return None
    return _load_raw_csv(path)
