"""Load data from CSV files into Signal objects."""
import csv
import pathlib
from dataclasses import dataclass

headers = {
    "radius": "Radius [nm]",
    "frequency": "Relative\nprobability",
}


@dataclass
class Signal:
    x: list[float]
    y: list[float]
    label: str = "signal"


def load(
    fp: pathlib.Path, delim: str = ";", fieldnames: list[str] = headers.keys()
) -> Signal:
    with fp.open() as f:
        reader = csv.DictReader(f, fieldnames=fieldnames, delimiter=delim)
        next(reader)  # skip header
        data = [tuple(float(x) for x in row.values()) for row in reader]
        return Signal(
            x=[sample[0] for sample in data],
            y=[sample[1] for sample in data],
            label=fp.stem,
        )
