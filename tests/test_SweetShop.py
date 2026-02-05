from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

base_url = "https://sweetshop.netlify.app"
subscription = f"{base_url}/sweets"

def test_open_subscription():
    opts = Options()

    opts.add_argument("--window-size=1280,900")
    driver = webdriver.Chrome(options=opts)

    driver.get(subscription)

    assert driver.title == "Sweet Shop"
    assert driver.current_url == subscription
