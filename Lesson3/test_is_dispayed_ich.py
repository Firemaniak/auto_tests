from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import pytest
# import os

# Написать автотест с использованием Python и Pytest, который:
# 1.Открывает https://itcareerhub.de/ru
# 2.Проверяет, что на странице отображаются:
# -Логотип ITCareerHub
#     -Ссылка “Программы”
#     -Ссылка “Способы оплаты”
#     -Ссылка “О нас”
#     -Ссылка “Контакты”
#     -Ссылка “Отзывы”
#     -Ссылка “Блог”
#     -Кнопки переключения языка (ru и de)
# 3.Кликнуть по разделу “Контакты”
# 4.Кликнуть по кнопке “Обратный звонок”
# 5.Проверить что текст “Запишитесь на бесплатную карьерную консультацию” отображается во всплывающем окне.

@pytest.fixture
def driver():
    # service = Service("/Users/romansurkov/Documents/chromedriver-mac-arm64/chromedriver")
    # options = Options()
    # driver = webdriver.Chrome(service=service, options=options)
    driver = webdriver.Chrome()
    driver.maximize_window()
    # driver.set_window_size(640, 460)
    # driver = webdriver.Chrome(service=service)
    # driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_is_dispayed(driver):
    driver.get("https://itcareerhub.de/ru")
    sleep(3)
    about_link = driver.find_element(By.LINK_TEXT, "Программы")
    assert about_link.is_displayed()
    pay_link = driver.find_element(By.LINK_TEXT, "Способы оплаты")
    assert pay_link.is_displayed()
    about_link = driver.find_element(By.LINK_TEXT, "О нас")
    assert about_link.is_displayed()
    cont_link = driver.find_element(By.LINK_TEXT, "О нас")
    cont_link.click()
    contact_link = driver.find_element(By.LINK_TEXT, "Контакты")
    assert contact_link.is_displayed()
    fid_link = driver.find_element(By.LINK_TEXT, "Отзывы")
    assert fid_link.is_displayed()
    blog_link = driver.find_element(By.LINK_TEXT, "Блог")
    assert blog_link.is_displayed()
    lang_link = driver.find_element(By.CSS_SELECTOR, "a[href='/']")
    assert lang_link.is_displayed()
    # contact_link.click()
    # back_call = driver.find_element(By.CSS_SELECTOR, "a[href='#popup:form-tr']")
    # back_call.click()
    # sleep(2)

def test_back_call(driver):
    driver.get("https://itcareerhub.de/ru")
    sleep(3)
    cont_link = driver.find_element(By.PARTIAL_LINK_TEXT, "О нас")
    cont_link.click()
    sleep(2)
    contact_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Контакты")
    contact_link.click()
    sleep(2)
    back_call = driver.find_element(By.CSS_SELECTOR, "a[href ='#popup:form-tr']")
    driver.execute_script("arguments[0].click();", back_call)
    # back_call.click()
    sleep(2)
    check_text = driver.find_element(By.CSS_SELECTOR, "[field='tn_text_175871291756015470']")
    assert check_text.is_displayed()
