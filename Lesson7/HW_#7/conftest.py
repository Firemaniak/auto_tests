from collections.abc import Iterator
import pytest
from api.booking_client import BookingClient

BOOKING_PAYLOAD = {
    "firstname": "Oleksii",
    "lastname": "Hrebennykov",
    "totalprice": 150,
    "depositpaid": True,
    "bookingdates": {"checkin": "2025-01-01", "checkout": "2025-01-10"},
    "additionalneeds": "Breakfast",
}


@pytest.fixture
def client() -> BookingClient:
    api = BookingClient()
    api.auth()
    return api


@pytest.fixture
def created_booking(client: BookingClient) -> Iterator[dict]:
    response = client.create_booking(BOOKING_PAYLOAD)
    booking_id = response.json()["bookingid"]
    yield {"id": booking_id, "data": BOOKING_PAYLOAD}

    client.delete_booking(booking_id)