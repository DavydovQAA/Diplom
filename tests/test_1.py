import time

from base.checkout_main_page import Checkout_main
from conftest import driver
from pages.cart_page import Cart_page
from pages.main_page import Main_page
from pages.phones_and_photo_equipment_page import Smartphones_and_photo_equipment_page
from pages.smartphones_page import Smartphones_page


def test_buy_product():
    print("Start Test")
    mp = Main_page(driver)
    mp.authorization()
    mp.select_smartphones_and_photo_equipment_catalog()

    pap = Smartphones_and_photo_equipment_page(driver)
    pap.select_smartphones_category()

    sp = Smartphones_page(driver)
    sp.buy_product_by_filter()

    cp = Cart_page(driver)
    cp.checking_purchases()

    cmp = Checkout_main(driver)
    cmp.finish()

    time.sleep(10)

    driver.quit()
