"""Load data from CSV files into Signal objects."""
import csv
import importlib.resources
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


def load_example_data() -> dict[str, Signal]:
    """Load example data from package."""
    example_data = []
    # sort by length of filename first, then alphabetically
    # so that size-distribution10 comes after size-distribution9
    for traversable in sorted(
        importlib.resources.files("ntt_peaks").joinpath("data").iterdir(),
        key=lambda x: (len(x.stem), x),
    ):
        with importlib.resources.as_file(traversable) as fp:
            if fp.suffix == ".csv":
                example_data.append(load(fp))
    return example_data


def load(
    fp: pathlib.Path, delim: str = ";", fieldnames: list[str] = headers.keys()
) -> Signal:
    """Load csv data from file."""
    with fp.open() as f:
        reader = csv.DictReader(f, fieldnames=fieldnames, delimiter=delim)
        next(reader)  # skip header
        data = [tuple(float(x) for x in row.values()) for row in reader]
        return Signal(
            x=[sample[0] for sample in data],
            y=[sample[1] for sample in data],
            label=fp.stem,
        )


if __name__ == "__main__":
    print(load_example_data())
