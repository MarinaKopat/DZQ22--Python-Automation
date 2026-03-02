import time
import os
import pytest
from selenium.webdriver.common.by import By

URL = 'https://demoqa.com/upload-download'


@pytest.mark.download
def test_download(driver):
    url = 'https://demoqa.com/upload-download'
    driver.get(url)
    file_name = 'sampleFile.jpeg'
    driver.find_element(By.ID, 'downloadButton').click()
    time.sleep(6)

    driver.get('chrome://downloads/')
    assert file_name == 'sampleFile.jpeg'


URL = 'https://demoqa.com/upload-download'


@pytest.mark.upload
def test_upload(driver):
    driver.get(URL)
    driver.find_element(By.ID, 'uploadFile').send_keys(os.path.abspath
    ('C:/Users/user/Desktop/DZQ22--Python-Automation/file/sampleFile.jpeg'))
    time.sleep(2)

    result = driver.find_element(By.ID, 'uploadedFilePath')
    assert result.is_displayed()
    assert 'sampleFile.jpeg' in result.text
