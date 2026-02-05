from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

base_url = "http://localhost:3000"
subscription = f"{base_url}/automation-lab/subscription"


def test_open_subscription():
    opts = Options()

    opts.add_argument("--window-size=1280,900")
    driver = webdriver.Chrome(options=opts)

    driver.get(subscription)

    assert driver.title == "Task Management Board"
    assert driver.current_url == subscription

    element_payment_section = driver.find_element(By.CSS_SELECTOR, ".payment-section")
    assert element_payment_section.is_displayed()
