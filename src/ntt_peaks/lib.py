import inspect
import sys
from types import FunctionType

from ntt_peaks.data import Signal


def detect_peaks(s: Signal, algorithm: str = "neighbours") -> list[int]:
    """Detect peaks in given signal and return their indices."""
    return _get_all_algorithms()[algorithm](s)


def _get_all_algorithms() -> dict[str, FunctionType]:
    return {
        name: obj
        for name, obj in inspect.getmembers(sys.modules[__name__])
        if inspect.isfunction(obj) and name != detect_peaks
    }


def neighbours(s: Signal) -> Signal:
    """Detect peak by comparing values to left and right neighbours.

    A peak is detected if the value is greater than its left and right neighbours.
    """
    return [
        idx for idx in range(1, len(s.y) - 1) if s.y[idx - 1] < s.y[idx] > s.y[idx + 1]
    ]


if __name__ == "__main__":
    print(_get_all_algorithms())
