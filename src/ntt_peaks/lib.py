import numpy as np

from . import Signal


def neighbours(values: list[int | float]) -> Signal:
    """Detect peak by comparing values to left and right neighbours.

    A peak is detected if the value is greater than its left and right neighbours.
    """
    return [
        idx
        for idx in range(1, len(values) - 1)
        if values[idx - 1] < values[idx] > values[idx + 1]
    ]


def threshold(values: list[int | float]) -> Signal:
    """Detect a peak by comparing values to a threshold value."""
    threshold = np.mean(values) * 2
    return [idx for idx in range(len(values)) if values[idx] > threshold]


def neighbours_and_threshold(values: list[int | float]) -> Signal:
    """Detect a peak by comparing values to a threshold value and neighbours."""
    return set(neighbours(values)) & set(threshold(values))


def scipy_regular(values: list[int | float]) -> list[int]:
    import scipy

    peaks, _ = scipy.signal.find_peaks(values)
    return peaks


def scipy_cwt(values: list[int | float]) -> list[int]:
    import scipy

    return scipy.signal.find_peaks_cwt(values, widths=[1, 2, 3, 4, 5])
