from collections.abc import Iterator
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver


@pytest.fixture
def driver() -> Iterator[WebDriver]:
    options = Options()
    options.add_argument("--start-maximized")


    options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False,
        },
    )
    options.add_argument("--guest")

    chrome = webdriver.Chrome(options=options)
    chrome.implicitly_wait(5)
    try:
        yield chrome
    finally:
        chrome.quit()
