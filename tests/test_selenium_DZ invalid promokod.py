import pytest
import time
from selenium.webdriver.common.by import By


url = 'http://localhost:3000/automation-lab/subscription'


@pytest.mark.parametrize('invalid_code', ['1254', '0000', 'CD', '@#$%'])
def test_fill_promocode_invalid(driver, invalid_code):
    driver.get(url)
    driver.maximize_window()
    time.sleep(5)

    promo_input = driver.find_element(By.CSS_SELECTOR, ".promo-input-wrapper input")
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", promo_input)

    promo_input.send_keys(invalid_code)
    time.sleep(5)

    promo_apply_btn = driver.find_element(By.CLASS_NAME, "promo-apply-btn")
    assert promo_apply_btn.is_enabled()

    driver.execute_script("arguments[0].click();", promo_apply_btn)
    time.sleep(5)

    promo_message_error = driver.find_element(By.CSS_SELECTOR, ".promo-message.error")
    assert promo_message_error.text == "Промокод не найден"
    time.sleep(5)






