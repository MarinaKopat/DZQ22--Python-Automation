import time
import pytest
from selenium.webdriver.common.by import By

URL = "https://demoqa.com/frames"


@pytest.mark.frame
def test_frame(driver):
    driver.get(URL)
    time.sleep(5)
    driver.switch_to.frame(driver.find_element(By.ID, 'frame1'))
    text = driver.find_element(By.CSS_SELECTOR, '#sampleHeading')
    assert text.text == 'This is a sample page'
    driver.switch_to.default_content()
