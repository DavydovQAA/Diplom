import time

from conftest import driver
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
    sp.select_product_by_filter()

    time.sleep(2)
