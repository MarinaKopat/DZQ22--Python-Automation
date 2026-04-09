import pytest
import time
from selenium.webdriver.common.by import By

URL = "https://demoqa.com/browser-windows"


@pytest.mark.window
def test_tab(driver):
    driver.get(URL)
    driver.find_element(By.ID, "tabButton").click()
    time.sleep(6)
    window_handles = driver.window_handles

    assert len(window_handles) == 2
    driver.switch_to.window(window_handles[-1])

    assert driver.find_element(By.ID, "sampleHeading").text == "This is a sample page"

    driver.close()
    time.sleep(6)
    driver.switch_to.window(window_handles[0])
    assert driver.current_url == URL
