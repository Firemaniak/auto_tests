from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver: WebDriver, timeout: int = 10) -> None:

        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def _find(self, locator: tuple[str, str]) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located(locator))

    def _click(self, locator: tuple[str, str]) -> None:
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def _type(self, locator: tuple[str, str], text: str) -> None:
        self._find(locator).send_keys(text)

    def _text_of(self, locator: tuple[str, str]) -> str:
        return self._find(locator).text