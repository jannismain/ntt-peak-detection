import pytest

import ntt_peaks
from ntt_peaks.data import load_example_data

algorithms = ["neighbours_and_threshold"]


@pytest.mark.parametrize("data,n_peaks_expected", [([0, 0, 5, 0, 0], 1)])
@pytest.mark.parametrize(
    "peak_detection_algorithm",
    algorithms,
)
def test_peak_detection_synthetic_data(
    data, n_peaks_expected, peak_detection_algorithm
):
    data = [0, 0, 5, 0, 0]
    peak_idxs = ntt_peaks.detect_peaks(data, peak_detection_algorithm)
    assert isinstance(peak_idxs, list)
    assert len(peak_idxs) == n_peaks_expected


@pytest.mark.parametrize(
    "peak_detection_algorithm",
    algorithms,
)
@pytest.mark.parametrize(
    "data",
    load_example_data(),
    ids=lambda x: x.label,
)
def test_peak_detection_real_data(data, peak_detection_algorithm):
    """Test peak detection algorithms detect expected number of peaks."""
    peaks = ntt_peaks.detect_peaks(data.y, peak_detection_algorithm)
    assert len(peaks) == 2
