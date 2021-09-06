"""
## 1 Feladat: Pitagorasz-tétel
Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.
Feladatod, hogy automatizáld selenium webdriverrel az alábbi funkcionalitásokat a Pitagorasz-tétel appban:
Az ellenőrzésekhez használj `pytest` keretrendszert. A tesztjeidben használj `assert` összehasonlításokat használj!
"""
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.headless = False

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k1.html"
driver.get(URL)
time.sleep(2)

fields = [{"a_id": "a"}, {"b_id": "b"}, {"submit_id": "submit"}, {"result_id": "result"}]


def locator_by_id(f_id):
    element = driver.find_element_by_id(f_id)
    return element


def fill_data_n_check_result(test_data_a, test_data_b, test_data_c):
    locator_by_id(fields[0]["a_id"]).clear()
    locator_by_id(fields[0]["a_id"]).send_keys(test_data_a)
    locator_by_id(fields[1]["b_id"]).clear()
    locator_by_id(fields[1]["b_id"]).send_keys(test_data_b)
    locator_by_id(fields[2]["submit_id"]).click()
    result = locator_by_id(fields[3]["result_id"]).text
    assert result == str(test_data_c)


def test_tc01_start_page():
    """
    Helyesen jelenik meg az applikáció betöltéskor:
    * a: <üres>
    * b: <üres>
    * c: <nem látszik>
    """
    test_data_tc01 = [{"a": ""}, {"b": ""}]
    assert locator_by_id(fields[0]["a_id"]).text == test_data_tc01[0]["a"]
    assert locator_by_id(fields[1]["b_id"]).text == test_data_tc01[1]["b"]
    assert not locator_by_id(fields[3]["result_id"]).is_displayed()


def test_tc02_correct_calculating():
    """
    Számítás helyes, megfelelő bemenettel
    * a: 2
    * b: 3
    * c: 10
    """
    test_data_tc02 = [{"a": 2}, {"b": 3}, {"c": 10}]
    fill_data_n_check_result(test_data_tc02[0]["a"], test_data_tc02[1]["b"], test_data_tc02[2]["c"])


def test_tc03_empty_filling():
    """
    Üres kitöltés:
    * a: <üres>
    * b: <üres>
    * c: NaN
    """
    test_data_tc03 = [{"a": ""}, {"b": ""}, {"c": "NaN"}]
    fill_data_n_check_result(test_data_tc03[0]["a"], test_data_tc03[1]["b"], test_data_tc03[2]["c"])
