from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Cart_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    checkout_button = "//button[@id='buy-btn-main']"

    main_word = "//h1[text()='Корзина']"

    # Getters
    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    # Actions

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print('Checking Purchases')

    # Methods

    def checking_purchases(self):
        self.get_current_url()
        self.assert_word(self.get_main_word(), 'Корзина')  # Кликаем 'Перейти к оформлению'
        self.click_checkout_button()
