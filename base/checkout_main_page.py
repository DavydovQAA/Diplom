import time

from base.base_class import Base


class Checkout_main(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Methods

    def finish(self):
        time.sleep(3)
        self.get_current_url()
        self.assert_url("https://www.dns-shop.ru/checkout-main/")
        self.get_screenshot()
