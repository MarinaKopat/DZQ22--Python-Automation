import time
from selenium.webdriver.common.by import By

url = 'http://localhost:3000/automation-lab/subscription'


def get_css_element(driver, selector):
    return driver.find_element(By.CSS_SELECTOR, selector)


def test_period_switcher(driver):
    driver.get(url)
    driver.maximize_window()
    driver.find_element(By.CSS_SELECTOR, '[data-testid="period-3"]').click()
    time.sleep(5)


def tariff_period_badge(driver):
    driver.get(url)
    driver.maximize_window()
    driver.find_element(By.CSS_SELECTOR, '[data-testid="tariff-premium"]').click()
    time.sleep(5)








