import time
from selenium.webdriver.common.by import By

URL = "https://demo.automationtesting.in/Alerts.html"


def test_alert_simple(driver):
    url = "https://demo.automationtesting.in/Alerts.html"
    driver.get(url)

    element = driver.find_element(By.CSS_SELECTOR, "[onclick='alertbox()']")
    element.click()
    time.sleep(6)

    alert = driver.switch_to.alert
    assert alert.text == "I am an alert box!"
    alert.accept()


def test_alert_cancel(driver):
    url = "https://demo.automationtesting.in/Alerts.html"
    driver.get(url)

    element = driver.find_element(By.LINK_TEXT, 'Alert with OK & Cancel')
    element.click()
    time.sleep(1)

    element = driver.find_element(By.CSS_SELECTOR, "[onclick='confirmbox()']")
    element.click()
    time.sleep(6)

    alert = driver.switch_to.alert
    assert alert.text == 'Press a Button !'

    alert.dismiss()

    element = driver.find_element(By.ID, 'demo')
    assert element.text == "You Pressed Cancel"


def test_alert_input_text(driver):
    url = "https://demo.automationtesting.in/Alerts.html"
    driver.get(url)

    element = driver.find_element(By.LINK_TEXT, 'Alert with Textbox')
    element.click()
    time.sleep(1)

    element = driver.find_element(By.CSS_SELECTOR, '[onclick="promptbox()"]')
    element.click()
    alert = driver.switch_to.alert

    assert alert.text == "Please enter your name"
    name = "Marina"
    alert.send_keys(name)
    alert.accept()
    time.sleep(6)

    result_element = driver.find_element(By.ID, 'demo1')
    assert name in result_element.text


def test_alert_text(driver):
    url = "https://demo.automationtesting.in/Alerts.html"
    driver.get(url)

    element = driver.find_element(By.LINK_TEXT, 'Alert with Textbox')
    element.click()
    time.sleep(1)

    element = driver.find_element(By.CSS_SELECTOR, '[onclick="promptbox()"]')
    element.click()
    prompt = driver.switch_to.alert
    assert prompt.text == "Please enter your name"

    text = 'Automation Testing user'

    prompt.send_keys(text)
    prompt.accept()
    time.sleep(6)
    result_element = driver.find_element(By.ID, 'demo1')
    assert text in result_element.text
