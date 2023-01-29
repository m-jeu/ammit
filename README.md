# Ammit
## Visualize heart rhythms

## What?

A simple tool to visualize the heart rhythm as measured by apple watches. Apple watch allows users to export short recordings in a very specific .csv format. Ammit processes these .csv files and visualizes the recordings.

## How?

### The simple method

A windows application that shouldn't require installing Python can be found at `dist/main.exe`.

### The slightly less simple method

The source code can be executed with a Python interpreter with the required packages at `main.py`.

## Where?

`main.py` contains an entrypoint to the `src/` package. `dist/` contains a packaged version as `.exe` packaged through pyinstaller. `exploration.ipynb` contains my initial exploration of the provided `.csv` in order to understand its format and make a useful graph.

## Why?

Research.

## Who?

[Maarten de Jeu](https://www.linkedin.com/in/maarten-de-jeu/)

## Can I use this?

Short answer: Yes. Long answer: Read the `LICENSE` file. If using this in your research, you might want to cite it. See `citation.bib`.