import pytest
import time
from selenium.webdriver.common.by import By


url = 'http://localhost:3000/automation-lab/subscription'


def get_css_element(driver, selector):
    return driver.find_element(By.CSS_SELECTOR, selector)


@pytest.mark.parametrize('card_number, card_expiry, card_cvv', [
    ('3213 2123 1321 3121', '12/28', '666')
])
def test_payment_card_visual(driver, card_number, card_expiry, card_cvv):
    driver.get(url)
    driver.maximize_window()
    time.sleep(5)

    card_input = driver.find_element(By.CSS_SELECTOR, ".card-number.card-input ")
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", card_input)
    card_input.send_keys(card_number)

    expiry_input = driver.find_element(By.CSS_SELECTOR, ".card-expiry.card-input")
    expiry_input.send_keys(card_expiry)
    time.sleep(5)

    cvv_input = driver.find_element(By.CSS_SELECTOR, ".card-cvv.card-input")
    cvv_input.send_keys(card_cvv)
    time.sleep(5)







