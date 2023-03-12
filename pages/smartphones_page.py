import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from base.base_class import Base


class Smartphones_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    price_locator = "//input[@value='a0c869ef13542a4a63d4ee843c977939']"
    stock_locator = "//input[@value='rassrockailivygoda']"
    manufacturer_apple_locator = "//input[@value='apple']"
    memory_locator = "//input[@value='32tg']"
    release_year_locator = "//input[@value='o8r3o']"
    value_of_ram_locator = "//div[@data-id='f[9a8]']"
    ram_8gb_locator = "//input[@value='i2ft']"
    model_locator = "//i[@class='ui-collapse__icon ui-collapse__icon_left ui-collapse__icon_down']"
    model_12_locator = "//input[@value='vqmuu']"
    apply_button = "//button[@data-role='filters-submit']"

    # Getters

    def get_price_button(self):

        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_locator)))

    # Actions

    def click_price_button(self):
        price_button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_locator)))
        action = ActionChains(self.driver)
        action.move_to_element(price_button)
        self.get_price_button().click()
        print("Click Price Button")

    # Methods

    def select_product_by_filter(self):
        self.click_price_button()
