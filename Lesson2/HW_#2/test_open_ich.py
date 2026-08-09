import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


# Написать скрипт, который:
#
#     Открывает в браузере Firefox https://itcareerhub.de/ru
#     Переходит в раздел "Способы оплаты"
#     Делает скриншот этой секции страницы
#
# В качестве ответа на задание необходимо приложить ссылку на git репозиторий.

@pytest.fixture
def driver():
    service = FirefoxService(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_about_page(driver):
    driver.get("https://itcareerhub.de/ru")
    sleep(3)
    about_link = driver.find_element(By.LINK_TEXT, "Способы оплаты")
    about_link.click()
    sleep(3)
    # about_link.screenshot("ich_page.png") # Make screen HTML-elemnet, but not a page
    driver.save_screenshot("ICH_Page.png")  # ok
    sleep(3)