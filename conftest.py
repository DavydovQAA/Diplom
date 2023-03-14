import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

@pytest.fixture(scope='module')
def set_up():
    print('Start Test')
    yield
    print('Finish Test')

@pytest.fixture(scope='module')
def set_group():
    print('Enter System')
    yield
    print('Exit System')

