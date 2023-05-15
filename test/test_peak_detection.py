import pytest

import ntt_peaks
from ntt_peaks.data import Signal


@pytest.mark.parametrize("data,n_peaks_expected", [([0, 0, 5, 0, 0], 1)])
@pytest.mark.parametrize("peak_detection_algorithm", ["neighbours"])
def test_peak_detection_synthetic_data(
    data, n_peaks_expected, peak_detection_algorithm
):
    data = [0, 0, 5, 0, 0]
    peak_idxs: list[int] = ntt_peaks.detect_peaks(
        Signal(x=list(range(len(data))), y=data), peak_detection_algorithm
    )
    assert isinstance(peak_idxs, list)
    assert len(peak_idxs) == n_peaks_expected
