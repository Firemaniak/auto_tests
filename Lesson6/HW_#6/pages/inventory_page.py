from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class InventoryPage(BasePage):

    CART_LINK = (By.CSS_SELECTOR, ".shopping_cart_link")

    def add_to_cart(self, item_id: str) -> None:
        locator = (By.ID, f"add-to-cart-{item_id}")
        self._click(locator)

    def go_to_cart(self) -> None:
        self._click(self.CART_LINK)