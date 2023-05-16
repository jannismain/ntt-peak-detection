import pytest
from fastapi.testclient import TestClient

from ntt_peaks.api import app


@pytest.fixture
def api():
    api = TestClient(app)
    assert api.get("/").json() == {"message": "Hello World"}
    yield api


def test_read_main(api):
    response = api.get("/detect_peaks?v=0,0,5,0,0")
    assert response.status_code == 200
    assert response.json() == [2]
