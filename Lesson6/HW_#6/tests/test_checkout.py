from selenium.webdriver.chrome.webdriver import WebDriver

from pages.cart_page import CartPage
from pages.checkout_pages import CheckoutOverviewPage, CheckoutStepOnePage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_login_smoke(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")
    assert "inventory" in driver.current_url

EXPECTED_TOTAL = 58.29


def test_checkout_total(driver: WebDriver) -> None:
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    inventory.add_to_cart("sauce-labs-backpack")
    inventory.add_to_cart("sauce-labs-bolt-t-shirt")
    inventory.add_to_cart("sauce-labs-onesie")

    inventory.go_to_cart()

    cart = CartPage(driver)
    cart.checkout()

    step_one = CheckoutStepOnePage(driver)
    step_one.fill_form("Oleg", "Vasilyev", "32120")

    overview = CheckoutOverviewPage(driver)
    total = overview.get_total()

    assert total == EXPECTED_TOTAL, (
        f"Ожидали ${EXPECTED_TOTAL}, получили ${total}"
    )