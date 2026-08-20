from api.booking_client import BookingClient
from conftest import BOOKING_PAYLOAD

def test_create_booking(client: BookingClient) -> None:
    response = client.create_booking(BOOKING_PAYLOAD)

    assert response.status_code == 200, response.text
    body = response.json()
    assert "bookingid" in body
    assert body["booking"]["firstname"] == BOOKING_PAYLOAD["firstname"]
    assert body["booking"]["totalprice"] == BOOKING_PAYLOAD["totalprice"]


def test_partial_update_booking(
    client: BookingClient, created_booking: dict
) -> None:
    booking_id = created_booking["id"]
    new_data = {"firstname": "Vasia", "lastname": "Trump"}

    response = client.partial_update_booking(booking_id, new_data)

    assert response.status_code == 200, response.text
    body = response.json()
    assert body["firstname"] == "Vasia"
    assert body["lastname"] == "Trump"
    assert body["totalprice"] == BOOKING_PAYLOAD["totalprice"]


def test_delete_booking(client: BookingClient) -> None:
    booking_id = client.create_booking(BOOKING_PAYLOAD).json()["bookingid"]

    delete_response = client.delete_booking(booking_id)
    assert delete_response.status_code == 201, delete_response.text

    get_response = client.get_booking(booking_id)
    assert get_response.status_code == 404


def test_partial_update_without_token_is_forbidden(
    created_booking: dict,
) -> None:
    booking_id = created_booking["id"]

    no_auth = BookingClient()
    response = no_auth.partial_update_booking(
        booking_id, {"firstname": "Hacker"}
    )

    assert response.status_code == 403, response.text