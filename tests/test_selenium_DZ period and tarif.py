import time
from selenium.webdriver.common.by import By

URL = 'http://localhost:3000/automation-lab/subscription'


def test_period_switcher(driver):
    driver.get(URL)
    period_btn = driver.find_element(By.CSS_SELECTOR, '[data-testid="period-3"]')
    period_btn.click()
    time.sleep(5)
    assert "active" in period_btn.get_attribute("class"), "Кнопка периода не стала активной"

    tariff_card = driver.find_element(By.CSS_SELECTOR, '[data-testid="tariff-premium"]')
    tariff_card.click()
    time.sleep(5)
    assert "selected" in tariff_card.get_attribute("class"), "Карточка тарифа не выбрана"














