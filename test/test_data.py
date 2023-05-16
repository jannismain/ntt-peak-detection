import pathlib

import pytest

import ntt_peaks

here = pathlib.Path(__file__).parent


@pytest.mark.parametrize(
    "problematic_data", [here / "empty-file.csv", here / "more-columns.csv"]
)
def test_load_problematic_data(caplog, problematic_data):
    """Test loading of empty file."""
    with caplog.at_level("ERROR"):
        with pytest.raises(SystemExit):
            ntt_peaks.load(problematic_data)
        assert len(caplog.records) >= 1, "an error should have been logged"
