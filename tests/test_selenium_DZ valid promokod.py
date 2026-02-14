import pytest
import time
from selenium.webdriver.common.by import By

url = 'http://localhost:3000/automation-lab/subscription'


@pytest.mark.only
def test_fill_promocode_valid(driver):
    driver.get(url)
    driver.maximize_window()
    time.sleep(6)

    promo_input = driver.find_element(By.CSS_SELECTOR, '.promo-input-wrapper input')
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", promo_input)

    promo_input.send_keys('ALWAYS')

    promo_apply_btn = driver.find_element(By.CLASS_NAME, 'promo-apply-btn')
    assert promo_apply_btn.is_enabled()

    driver.execute_script("arguments[0].click();", promo_apply_btn)

    promo_message_success = driver.find_element(By.CSS_SELECTOR, '.promo-message.success')
    assert promo_message_success.text == "Промокод применён: Скидка 15% для для всех тарифов"
    time.sleep(6)




