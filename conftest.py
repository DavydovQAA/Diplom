import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

CHROME_VERSION = "111.0.5563.64"


@pytest.fixture(autouse=True)
def driver():
    service = ChromeService(ChromeDriverManager(CHROME_VERSION).install())
    browser = webdriver.Chrome(service=service)
    browser.maximize_window()
    yield browser
    browser.quit()
