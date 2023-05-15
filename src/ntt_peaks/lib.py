import numpy as np

from . import Signal


def neighbours(s: Signal) -> Signal:
    """Detect peak by comparing values to left and right neighbours.

    A peak is detected if the value is greater than its left and right neighbours.
    """
    return [
        idx for idx in range(1, len(s.y) - 1) if s.y[idx - 1] < s.y[idx] > s.y[idx + 1]
    ]


def threshold(s: Signal) -> Signal:
    """Detect a peak by comparing values to a threshold value."""
    threshold = np.mean(s.y) * 5
    return [idx for idx in range(len(s.y)) if s.y[idx] > threshold]


def local_threshold(s: Signal) -> Signal:
    """Detect a peak by comparing values to a threshold value."""
    window = 2
    results = []
    for idx, v in enumerate(s.y):
        local_threshold = np.mean(s.y[idx - window : idx + window])
        if v > (local_threshold * 1.2):
            results.append(idx)
    return results


def scipy_regular(s: Signal) -> list[int]:
    import scipy

    peaks, _ = scipy.signal.find_peaks(s.y)
    return peaks


def scipy_cwt(s: Signal) -> list[int]:
    import scipy

    return scipy.signal.find_peaks_cwt(s.y, widths=[1, 2, 3, 4, 5])
