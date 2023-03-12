import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Main_page(Base):
    url = 'https://www.dns-shop.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    authorization_locator = "//button[@class='base-ui-button-v2_medium base-ui-button-v2_white base-ui-button-v2_ico-none base-ui-button-v2 personal-block-desktop__buttons_sign-in']"
    entrance_with_password_locator = "//div[@class='block-other-login-methods__password-caption']"
    email_locator = "//input[@autocomplete='username']"
    password_locator = "//input[@autocomplete='current-password']"
    entrance_button_locator = "//button[@class='base-ui-button-v2_big base-ui-button-v2_brand base-ui-button-v2_ico-none base-ui-button-v2']"
    smartphones_and_photo_equipment_catalog_locator = "//a[@href='/catalog/17a890dc16404e77/smartfony-i-fototexnika/']"

    # Getters

    def get_authorization_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.authorization_locator)))

    def get_entrance_with_password(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.entrance_with_password_locator)))

    def get_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email_locator)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password_locator)))

    def get_entrance_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.entrance_button_locator)))

    def get_select_smartphones_and_photo_equipment_catalog(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.smartphones_and_photo_equipment_catalog_locator)))

    # Actions

    def click_authorization_button(self):
        self.get_authorization_button().click()
        print('Click Authorization button')

    def click_entrance_with_password(self):
        self.get_entrance_with_password().click()
        print('Click Entrance with password button')

    def input_email(self, user_email):
        self.get_email().send_keys(user_email)
        print('Input user email')

    def input_password(self, user_password):
        self.get_password().send_keys(user_password)
        print('Input user password')

    def click_entrance_button(self):
        self.get_entrance_button().click()
        print('Click Entrance  button')

    def click_smartphones_and_photo_equipment_catalog(self):
        self.get_select_smartphones_and_photo_equipment_catalog().click()
        print('Select Smartphones and photo equipment catalog')

    # Methods

    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_authorization_button()
        self.click_entrance_with_password()
        self.input_email('ghostinside80@gmail.com')
        self.input_password('shop1234')
        self.click_entrance_button()

    def select_smartphones_and_photo_equipment_catalog(self):
        time.sleep(10)
        self.click_smartphones_and_photo_equipment_catalog()
        self.get_current_url()

