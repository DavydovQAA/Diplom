import datetime
from selenium.webdriver.support.wait import WebDriverWait

TIMEOUT = 15


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def wait(self, timeout=TIMEOUT):
        return WebDriverWait(self.driver, timeout)

    def get_current_url(self):
        """Method get current url"""
        get_url = self.driver.current_url
        print("Current url " + get_url)

    def scroll(self):
        """Method scroll"""
        self.driver.execute_script('window.scrollTo(0,500)')

    def assert_word(self, word, result):
        """Method assert word"""
        print(result)
        print(word)
        value_word = word.text
        assert value_word == result
        print('Good value word')

    def assert_url(self, result):
        """Method assert URL"""
        get_url = self.driver.current_url
        assert get_url == result
        print('Good value URL')

    def get_screenshot(self):
        """Method Screenshot"""
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot('./screen/' + name_screenshot)
