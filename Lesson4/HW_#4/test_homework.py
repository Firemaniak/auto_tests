import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_text_input_button(driver):
    driver.get("http://uitestingplayground.com/textinput")

    wait = WebDriverWait(driver, 10)


    input_field = wait.until(EC.element_to_be_clickable((By.ID, "newButtonName")))
    input_field.clear()
    input_field.send_keys("ITCH")

    button = wait.until(EC.element_to_be_clickable((By.ID, "updatingButton")))
    button.click()


    wait.until(EC.text_to_be_present_in_element((By.ID, "updatingButton"), "ITCH"))
    assert button.text == "ITCH", f"Ожидался текст кнопки 'ITCH', получено: '{button.text}'"


def test_loading_images(driver):

    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    wait = WebDriverWait(driver, 15)

    locator = (By.CSS_SELECTOR, "img[alt]")

    def all_images_loaded(drv):
        imgs = drv.find_elements(*locator)
        loaded = [img for img in imgs if img.get_attribute("src")]
        return loaded if len(loaded) >= 3 else False

    images = wait.until(all_images_loaded)

    print("Найденные alt изображений:", [img.get_attribute("alt") for img in images])

    assert len(images) >= 3, f"Ожидалось минимум 3 изображения, найдено: {len(images)}"
    third_image_alt = images[2].get_attribute("alt")

    assert third_image_alt == "award", f"Ожидался alt='award', получено: '{third_image_alt}'"