import inspect
from types import FunctionType

from . import Signal


def detect_peaks(v: list[int | float], algorithm: str = "neighbours") -> list[int]:
    """Detect peaks in given signal and return their indices."""
    return _get_all_algorithms()[algorithm](v)


def _get_all_algorithms() -> dict[str, FunctionType]:
    from . import lib

    return dict(inspect.getmembers(lib, inspect.isfunction))
