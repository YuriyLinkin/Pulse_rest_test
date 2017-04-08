import pytest

from fixtures.pulse_api_client import BookPulseRestApi


@pytest.fixture()
def app():
    fixture = BookPulseRestApi(resourse="books")
    return fixture