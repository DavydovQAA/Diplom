import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from selenium.webdriver.support import expected_conditions as EC

from logger import Logger


class Smartphones_and_photo_equipment_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    smartphones_category_locators = "//a[@href='/catalog/17a8a01d16404e77/smartfony/']"

    # Getters

    def get_smartphones_category(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.smartphones_category_locators)))

    # Actions

    def click_smartphones_category(self):
        self.get_smartphones_category().click()
        print('Select Smartphones category')

    # Methods

    def select_smartphones_category(self):   # Выбираем раздел 'Смартфоны'
        with allure.step('Select Smartphones Category'):
            Logger.add_start_step(method='select_smartphones_category')
            self.get_current_url()
            self.click_smartphones_category()
            Logger.add_end_step(url=self.driver.current_url, method='select_smartphones_category')

