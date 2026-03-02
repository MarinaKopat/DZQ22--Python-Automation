import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


URL = 'http://localhost:3000/automation-lab/subscription'


def test_all_click_methods(driver):
    driver.get(URL)

    element = driver.find_element(By.CSS_SELECTOR, "button.task-goals-btn")
    element.click()
    time.sleep(6)
    element = driver.find_element(By.CSS_SELECTOR, "button.modal-close-x")
    element.click()

    time.sleep(6)
    element = driver.find_element(By.CSS_SELECTOR, "button.period-btn")
    driver.execute_script("arguments[0].click();", element)

    promo_input = driver.find_element(By.CSS_SELECTOR, '.promo-input-wrapper input')
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", promo_input)
    promo_input.send_keys('ALWAYS')
    time.sleep(6)

    element = driver.find_element(By.CSS_SELECTOR, "button.promo-apply-btn")
    element.send_keys(Keys.ENTER)
    promo_message_success = driver.find_element(By.CSS_SELECTOR, '.promo-message.success')
    assert promo_message_success.text == "Промокод применён: Скидка 15% для для всех тарифов"
    time.sleep(6)

    promo_input = driver.find_element(By.CSS_SELECTOR, '.promo-input-wrapper input')
    promo_input.clear()

    actions = ActionChains(driver)
    element = driver.find_element(By.CSS_SELECTOR, "button.promo-hint-btn")
    actions.move_to_element(element).click().perform()
    time.sleep(6)
    element = driver.find_element(By.CSS_SELECTOR, "button.modal-close-x")
    element.click()
















