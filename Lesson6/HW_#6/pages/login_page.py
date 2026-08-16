from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    URL = "https://www.saucedemo.com/"

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def open(self) -> None:
        self.driver.get(self.URL)

    def login(self, username: str, password: str) -> None:
        self._type(self.USERNAME, username)
        self._type(self.PASSWORD, password)
        self._click(self.LOGIN_BUTTON)