import requests

class BookingClient:

    BASE_URL = "https://restful-booker.herokuapp.com"

    def __init__(self) -> None:
        self.session = requests.Session()
        self.session.headers.update(
            {"Content-Type": "application/json", "Accept": "application/json"}
        )
        self.token: str | None = None

    def auth(self, username: str = "admin", password: str = "password123") -> str:
        response = self.session.post(
            f"{self.BASE_URL}/auth",
            json={"username": username, "password": password},
        )
        response.raise_for_status()
        self.token = response.json()["token"]
        return self.token

    def create_booking(self, payload: dict) -> requests.Response:
        return self.session.post(f"{self.BASE_URL}/booking", json=payload)

    def get_booking(self, booking_id: int) -> requests.Response:
        return self.session.get(f"{self.BASE_URL}/booking/{booking_id}")

    def partial_update_booking(
        self, booking_id: int, payload: dict
    ) -> requests.Response:
        return self.session.patch(
            f"{self.BASE_URL}/booking/{booking_id}",
            json=payload,
            headers={"Cookie": f"token={self.token}"},
        )

    def delete_booking(self, booking_id: int) -> requests.Response:
        return self.session.delete(
            f"{self.BASE_URL}/booking/{booking_id}",
            headers={"Cookie": f"token={self.token}"},
        )