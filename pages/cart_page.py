import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from base.base_page import BasePage
from logger import Logger


class CartPage(BasePage):
    # Locators

    checkout_button = "//button[@id='buy-btn-main']"

    main_word = "//h1[text()='Корзина']"

    # Getters
    def get_checkout_button(self):
        return self.wait().until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))

    def get_main_word(self):
        return self.wait().until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    # Actions

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print('Checking Purchases')

    # Methods

    def checking_purchases(self):
        with allure.step('Checking Purchases'):
            Logger.add_start_step(method='checking_purchases')
            self.get_current_url()
            self.assert_word(self.get_main_word(), 'Корзина')  # Кликаем 'Перейти к оформлению'
            self.click_checkout_button()
            Logger.add_end_step(url=self.driver.current_url, method='checking_purchases')
