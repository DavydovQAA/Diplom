import time
import allure

from pages.cart_page import CartPage
from pages.checkout_main_page import CheckoutMain
from pages.main_page import MainPage
from pages.phones_and_photo_equipment_page import SmartphonesAndPhotoEquipmentPage
from pages.smartphones_page import SmartphonesPage


@allure.description('Test buy product')
def test_buy_product(driver):
    print("Start Test")
    mp = MainPage(driver)
    mp.authorization()
    mp.select_smartphones_and_photo_equipment_catalog()

    pap = SmartphonesAndPhotoEquipmentPage(driver)
    pap.select_smartphones_category()

    sp = SmartphonesPage(driver)
    sp.buy_product_by_filter()

    cp = CartPage(driver)
    cp.checking_purchases()

    cmp = CheckoutMain(driver)
    time.sleep(30)
    cmp.finish()

    time.sleep(10)
