import time

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from base.base_class import Base
from logger import Logger


class Smartphones_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    rating_locator = "//div[@data-id='rating']"

    apply_button_locator = "//button[@data-role='filters-submit']"

    field_price_locator = "//input[@placeholder='от 2 999']"

    buy_phone_locator = '''(//button[text()="Купить"][preceding::span[contains(text(), '6.67" Смартфон Honor 70 256 ГБ зеленый [ядер - 8x(1.9 ГГц, 2.2 ГГц, 2.5 ГГц), 8 Гб, 2 SIM, OLED, 2400x1080, камера 54+50+2 Мп, NFC, 5G, GPS, 4800 мА*ч]')]])[1]'''

    cart_locator = "//a[@data-commerce-target='CART']"

    main_word = "//h1[text()='Смартфоны']"

    # Getters
    def get_input_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.field_price_locator)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    # Actions

    def click_rating_button(self):
        rating_button = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.rating_locator)))
        action = ActionChains(self.driver)
        action.move_to_element(rating_button).perform()
        rating_button.click()
        print('Click Rating button')

    def click_apply_button(self):
        apply_button = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.apply_button_locator)))
        action = ActionChains(self.driver)
        action.move_to_element(apply_button).perform()
        apply_button.click()
        print('Click Apply button')

    def write_price(self):
        self.get_input_price().send_keys('40000')
        print('Write Price')

    def buy_phone(self):
        buy_phone = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.buy_phone_locator)))
        action = ActionChains(self.driver)
        action.move_to_element(buy_phone).perform()
        buy_phone.click()
        print('Buy Phone')

    def click_cart(self):
        cart = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_locator)))
        action = ActionChains(self.driver)
        action.move_to_element(cart).perform()
        cart.click()
        print('Click Cart')
    # Methods

    def buy_product_by_filter(self):
        with allure.step('Buy Product by filter'):
            Logger.add_start_step(method='buy_product_by_filter')
            self.get_current_url()
            self.assert_word(self.get_main_word(), 'Смартфоны')   # Выбираем товар по фильтрам, покупаем и переходим в корзину
            self.click_rating_button()
            self.scroll()
            self.write_price()
            self.click_apply_button()
            self.buy_phone()
            time.sleep(3)
            self.click_cart()
            Logger.add_end_step(url=self.driver.current_url, method='buy_product_by_filter')
