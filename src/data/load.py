from typing import Union

import io
import tkinter as tk
from tkinter.filedialog import askopenfilename

import pandas as pd


def _correct_trailing_commas(path: str, comma_n: int) -> io.StringIO:
    """Correct a file that doesn't contain a consistent amount of commas per line by adding the required
    amount of commas to the end of lines still missing them.

    Args:
        path: path of file to correct.
        comma_n: amount of commas that every line should have.

    Returns:
        File with specified amount of commas on every line, as StringIO."""

    with open(path, "r") as file:
        lines = file.readlines()  # Will already include \n at end of line

    lines = [
        elem[:-1] + ((comma_n - elem.count(",")) * ",")
        for elem in lines
    ]

    return io.StringIO("\n".join(lines))


def _user_file_select() -> str:
    """Ask the user to select a .csv file through the windows file explorer, through a tkinter window.

    Returns:
        File path of the selected file as string. File path will show as empty string when choice is not made by user."""
    tk.Tk().withdraw()
    path = askopenfilename(filetypes=[("Comma separated values", "*.csv")])
    return path


def _load_raw_csv(content: Union[str, io.StringIO]) -> pd.DataFrame:
    """Load a CSV file with the specified formatting as discovered in exploration.ipynb.

    Args:
        content: thing to load, could either be path to file or (String)IO.

    Returns:
        Raw dataframe."""
    return pd.read_csv(content, delimiter=",", header=None)


def fetch() -> Union[pd.DataFrame, None]:
    """Ask user to select a file .CSV through _user_file_select(), pre-process it with _correct_trailing_commas(),
    and load selected file as Pandas dataframe with _load_raw_csv().

    File will only load properly if in specified formatting such as discovered in exploration.ipynb.

    Returns:
        Dataframe if file selection/load successful, None otherwise."""
    if (path := _user_file_select()) == "":
        return None
    return _load_raw_csv(
        _correct_trailing_commas(
            path,
            2
        )
    )
