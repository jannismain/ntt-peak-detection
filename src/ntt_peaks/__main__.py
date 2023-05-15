"""Command-line interface for manual evaluation of peak detection algorithms."""
import pathlib

import plotly.graph_objects as go
from plotly.subplots import make_subplots

from ntt_peaks import Signal, detect_peaks, load
from ntt_peaks.data import load_example_data

algorithms = ["neighbours"]


def cli():
    import sys

    dataset_args = sys.argv[1:]

    if len(dataset_args) == 0:
        datasets = load_example_data()
    elif len(dataset_args) == 1:
        datasets = [pathlib.Path(dataset_args[0])]
    else:
        datasets = [pathlib.Path(arg) for arg in dataset_args]

    fig = make_subplots(rows=len(datasets), cols=1)

    for n, fp in enumerate(datasets, start=1):
        results = main(fp)
        for idx, signal in enumerate(results):
            fig.append_trace(
                go.Scatter(
                    x=signal.x,
                    y=signal.y,
                    **dict(
                        name=signal.label,
                        mode="lines" if idx == 0 else "markers",
                        legendgroup="data" if idx == 0 else algorithms[idx - 1],
                    ),
                ),
                row=n,
                col=1,
            )

    fig.show()


def main(dataset: pathlib.Path) -> list[Signal]:
    data = load(dataset) if isinstance(dataset, pathlib.Path) else dataset
    return [
        data,
        *[process(data, algorithm) for algorithm in algorithms],
    ]


def process(data: Signal, algorithm: str) -> Signal:
    result = detect_peaks(data, algorithm)
    print(f"{algorithm}: {result}")
    return Signal(
        x=[data.x[idx] for idx in result],
        y=[data.y[idx] for idx in result],
        label=algorithm,
    )


if __name__ == "__main__":
    cli()
