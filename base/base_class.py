import datetime

class Base():

    def __init__(self, driver):
        self.driver = driver

    """Method get current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url " + get_url)

    """Method scroll"""

    def scroll(self):
        self.driver.execute_script('window.scrollTo(0,500)')

    """Method assert word"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print('Good value word')

    """Method assert URL"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print('Good value URL')

    """Method Screenshot"""

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot('./screen/' + name_screenshot)

