from ntt_peaks import Signal


def neighbours(s: Signal) -> Signal:
    """Detect peak by comparing values to left and right neighbours.

    A peak is detected if the value is greater than its left and right neighbours.
    """
    return [
        idx for idx in range(1, len(s.y) - 1) if s.y[idx - 1] < s.y[idx] > s.y[idx + 1]
    ]


if __name__ == "__main__":
    print(_get_all_algorithms())
