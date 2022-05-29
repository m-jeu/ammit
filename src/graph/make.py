import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def _construct(
        measurement_s: pd.Series,
        override_title: str = "Personal device ECG measurements over time",
) -> go.Figure:
    """Construct a plotly Figure that plots the ECG time series data with the proper title/axis labels.

    Args:
        measurement_s: measurement series object as specified in src/data.
        override_title: title if non-default is desired.

    Returns:
        Plotly figure."""
    return px.line(measurement_s,
                   x=measurement_s.index,
                   y=measurement_s,
                   title=override_title,
                   labels={
                       "index": "Seconds since start",
                       "y": "Measurement amplitude (unit unknown)"
                   })


def _add_point_two_second_vlines(fig: go.Figure, measurement_s: pd.Series) -> None:
    """Add an ECG-style vertical line every .2 seconds.

    NOTE: INPLACE.

    Args:
        fig: figure to add lines to.
        measurement_s: measurement series object as specified in src/data.

    Returns:
        None."""
    x_line_interval_dist: float = .2     # Set invervals
    x_line_pos: np.ndarray = np.arange(  # Create positions
        0,
        np.max(measurement_s.index),
        x_line_interval_dist
    )

    # Vectorize and apply
    np.vectorize(lambda x: fig.add_vline(x, line_color="rgba(255, 0, 0, 0.5)", line_width=.9))(x_line_pos)

    return None


def _finish(fig: go.Figure) -> None:
    """Finish the ECG-style figure with proper coloring, and a range slider.

    NOTE: INPLACE.

    Args:
        fig: Plotly figure.

    Returns:
        None."""
    fig.update_traces(line_color="#000000", line_width=1)
    fig.update_layout(xaxis_rangeslider_visible=True, xaxis_range=[0, 2])

    return None


def make(measurement_s: pd.Series) -> go.Figure:
    """Top level function that creates an ECG-like figure from a measurement Series object as specified in src/data.

    Args:
        measurement_s: measurement series object as specified in src/data.

    Returns:
        Plotly figure."""
    fig = _construct(measurement_s)
    _add_point_two_second_vlines(fig, measurement_s)
    _finish(fig)
    return fig
