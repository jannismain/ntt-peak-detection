import pytest
from fastapi.testclient import TestClient

from ntt_peaks.api import app


@pytest.fixture
def api():
    api = TestClient(app)
    assert api.get("/").json() == {"message": "Hello World"}
    yield api


@pytest.mark.parametrize(
    "data,peak_idx_expected",
    [
        ("0,0,5,0,0", [2]),
        ("0,0,0,5.5,0", [3]),
    ],
)
def test_api_detect_peaks(api, data, peak_idx_expected):
    response = api.get(f"/detect_peaks?v={data}")
    assert response.status_code == 200
    assert response.json() == peak_idx_expected
