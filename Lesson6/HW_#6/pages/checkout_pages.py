from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutStepOnePage(BasePage):

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")

    def fill_form(self, first_name: str, last_name: str, postal_code: str) -> None:

        self._type(self.FIRST_NAME, first_name)
        self._type(self.LAST_NAME, last_name)
        self._type(self.POSTAL_CODE, postal_code)
        self._click(self.CONTINUE_BUTTON)


class CheckoutOverviewPage(BasePage):

    TOTAL_LABEL = (By.CSS_SELECTOR, ".summary_total_label")

    def get_total(self) -> float:

        text = self._text_of(self.TOTAL_LABEL)
        return float(text.split("$")[1])