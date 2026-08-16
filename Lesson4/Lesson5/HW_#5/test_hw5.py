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


def accept_cookies_via_js(driver):

    driver.execute_script(
        """
        var selectors = [
            '#cookie_action_close_header',
            '#cookie-law-info-bar .cli_action_button',
            '.cli-plugin-main-button',
            '.wt-cli-accept-all-btn',
            '#cookie-law-info-bar a',
            '.cookie-notice-accept-button',
            '#CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll'
        ];
        selectors.forEach(function (sel) {
            var el = document.querySelector(sel);
            if (el) { el.click(); }
        });

        var overlays = document.querySelectorAll(
            '#cookie-law-info-bar, .cli-modal-backdrop, #cookie-notice, .cookie-notice-container, #CybotCookiebotDialog'
        );
        overlays.forEach(function (el) { el.remove(); });
        """
    )


def js_drag_and_drop(driver, source, target, steps=15):

    driver.execute_script(
        """
        function fireMouseEvent(type, elem, x, y) {
            var event = new MouseEvent(type, {
                view: window,
                bubbles: true,
                cancelable: true,
                clientX: x,
                clientY: y,
                button: 0,
                buttons: 1
            });
            elem.dispatchEvent(event);
        }

        var source = arguments[0];
        var target = arguments[1];
        var steps = arguments[2];

        var srcRect = source.getBoundingClientRect();
        var tgtRect = target.getBoundingClientRect();

        var startX = srcRect.left + srcRect.width / 2;
        var startY = srcRect.top + srcRect.height / 2;
        var endX = tgtRect.left + tgtRect.width / 2;
        var endY = tgtRect.top + tgtRect.height / 2;

        fireMouseEvent('mouseover', source, startX, startY);
        fireMouseEvent('mousedown', source, startX, startY);

        for (var i = 1; i <= steps; i++) {
            var x = startX + (endX - startX) * (i / steps);
            var y = startY + (endY - startY) * (i / steps);
            fireMouseEvent('mousemove', document, x, y);
        }

        fireMouseEvent('mouseover', target, endX, endY);
        fireMouseEvent('mousemove', target, endX, endY);
        fireMouseEvent('mouseup', target, endX, endY);
        """,
        source,
        target,
        steps,
    )


def test_text_present_in_iframe(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/iframes.html")
    wait = WebDriverWait(driver, 10)

    target_text = "semper posuere integer et senectus justo curabitur."

    wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "my-iframe")))

    paragraphs = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "p")))
    matching_paragraph = next((p for p in paragraphs if target_text in p.text), None)

    assert matching_paragraph is not None, (
        f"Текст '{target_text}' не найден ни в одном из {len(paragraphs)} "
        f"параграфов внутри iframe"
    )
    assert matching_paragraph.is_displayed(), "Найденный элемент с текстом не отображается на странице"

    driver.switch_to.default_content()


def test_drag_and_drop_photo_to_trash(driver):
    driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
    wait = WebDriverWait(driver, 15)

    accept_cookies_via_js(driver)

    wait.until(
        EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe.demo-frame"))
    )

    gallery = wait.until(EC.presence_of_element_located((By.ID, "gallery")))
    trash = driver.find_element(By.ID, "trash")

    driver.switch_to.default_content()
    accept_cookies_via_js(driver)
    driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, "iframe.demo-frame"))

    photos_before = gallery.find_elements(By.TAG_NAME, "li")
    assert len(photos_before) == 4, (
        f"Ожидалось 4 фото в галерее до перетаскивания, найдено: {len(photos_before)}"
    )

    first_photo = photos_before[0]

    js_drag_and_drop(driver, first_photo, trash)

    wait.until(lambda d: len(gallery.find_elements(By.TAG_NAME, "li")) == 3)

    photos_after = gallery.find_elements(By.TAG_NAME, "li")
    trashed_photos = trash.find_elements(By.TAG_NAME, "li")

    assert len(trashed_photos) == 1, (
        f"В корзине должна быть 1 фотография, найдено: {len(trashed_photos)}"
    )

    assert len(photos_after) == 3, (
        f"В галерее должно остаться 3 фотографии, найдено: {len(photos_after)}"
    )

    driver.switch_to.default_content()
