import time

import allure

from base.base_class import Base
from logger import Logger


class Checkout_main(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Methods

    def finish(self):
        with allure.step('Checking Final Page'):
            Logger.add_start_step(method='finish')
            time.sleep(3)
            self.get_current_url()
            self.assert_url("https://www.dns-shop.ru/checkout-main/")
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method='finish')

