import time

from conftest import driver
from pages.main_page import Main_page


def test_buy_product():
    print("Start Test")
    mp = Main_page(driver)
    mp.authorization()
    mp.select_smartphones_and_photo_equipment_catalog()
    time.sleep(2)


