import pytest

from fixtures.pulse_api_client import BookPulseRestApi
from fixtures.hw_pulseApiRoles import Pulse_Api_Roles


@pytest.fixture(scope="session")
def app_book():
    fixture = BookPulseRestApi(resourse="books")
    return fixture

@pytest.fixture(scope="module")
def app_role():
    fixture = Pulse_Api_Roles(resourse="roles")
    return fixture

