"""
## 3 Feladat: Alfanumerikus mező
Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.
Feladatod, hogy automatizáld selenium webdriverrel a Alfanumerikus mező app tesztelését.
Az ellenőrzésekhez használj `pytest` keretrendszert. A tesztjeidben használj `assert` összehasonlításokat használj!
"""
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.headless = False

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k3.html"
driver.get(URL)
time.sleep(2)

fields = [{"input_id": "title"}, {"error_msg_xp": "//span[@class='error active']"}]


def locator_by_id(f_id):
    element = driver.find_element_by_id(f_id)
    return element


def locator_by_xp(f_xp):
    element = driver.find_element_by_xpath(f_xp)
    return element


def fill_input_field_n_check_error_msg(input_data, error_msg):
    locator_by_id(fields[0]["input_id"]).clear()
    locator_by_id(fields[0]["input_id"]).send_keys(input_data)
    if len(driver.find_elements_by_xpath(fields[1]["error_msg_xp"])) != 0:
        assert locator_by_xp(fields[1]["error_msg_xp"]).text == error_msg


def tc01_correct_filling():
    """
    Helyes kitöltés esete:
    * title: abcd1234
    * Nincs validációs hibazüzenet
    """
    test_data_tc01 = [{"input_field": "abcd1234"}, {"error_msg_text": ""}]
    fill_input_field_n_check_error_msg(test_data_tc01[0]["input_field"], test_data_tc01[1]["error_msg_text"])
    assert len(driver.find_elements_by_xpath(fields[1]["error_msg_xp"])) == 0


def tc02_illegal_chars():
    """
    Illegális karakterek esete:
    * title: teszt233@
    * Only a-z and 0-9 characters allewed.
    """
    test_data_tc02 = [{"input_field": "teszt233@"}, {"error_msg_text": "Only a-z and 0-9 characters allewed"}]
    fill_input_field_n_check_error_msg(test_data_tc02[0]["input_field"], test_data_tc02[1]["error_msg_text"])


def tc03_short_input():
    """
    Tul rövid bemenet esete:
    * title: abcd
    * Title should be at least 8 characters; you entered 4.
    """
    test_data_tc03 = [{"input_field": "abcd"},
                      {"error_msg_text": "Title should be at least 8 characters; you entered 4."}]
    fill_input_field_n_check_error_msg(test_data_tc03[0]["input_field"], test_data_tc03[1]["error_msg_text"])
