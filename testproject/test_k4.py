"""
## 4 Feladat: Műveletek karakterekkel
Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.
Feladatod, hogy automatizáld selenium webdriverrel a Műveletek karakterekkel app tesztelését.
Az applikáció minden frissítésnél véletlenszerűen változik!
Az ellenőrzésekhez használj `pytest` keretrendszert. A tesztjeidben használj `assert` összehasonlításokat használj!
"""

import time
from selenium import webdriver   # kell a PIP hozzá: pip install selenium
from selenium.webdriver.chrome.options import Options  # headless módhoz többek között
from webdriver_manager.chrome import ChromeDriverManager  # webdriverManager, kell a PIP: pip install webdriver-manager

options = Options()
options.headless = False

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k4.html"
driver.get(URL)
time.sleep(2)

fields = [{"abc_par_xp": "//div/div/p[3]"}, {"chr_id": "chr"}, {"op_id": "op"}, {"submit_btn_id": "submit"},
          {"result_id": "result"}, {"num_id": "num"}]

test_data = [{"op_field": ["+", "-"]}]


def locator_by_xp(f_xp):
    element = driver.find_element_by_xpath(f_xp)
    return element


def locator_by_id(f_id):
    element = driver.find_element_by_id(f_id)
    return element


def test_tc01():
    """
    Helyesen betöltődik az applikáció:
    * Megjelenik az ABCs műveleti tábla, pontosan ezzel a szöveggel:
      * !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~
    """
    abc_field = locator_by_xp(fields[0]["abc_par_xp"]).text
    char_list = []
    for _ in range(33, 127):
        char_list.append(chr(_))

    def list_to_string(s):
        str1 = ""
        for _ in s:
            str1 += _
        return str1

    assert list_to_string(char_list) == abc_field


def test_tc02():
    """
    Megjelenik egy érvényes művelet:
    * `chr` megző egy a fenti ABCs műveleti táblából származó karaktert tartalmaz
    * `op` mező vagy + vagy - karaktert tartlamaz
    * `num` mező egy egész számot tartalamaz
    """
    assert locator_by_id(fields[1]["chr_id"]).text in locator_by_xp(fields[0]["abc_par_xp"]).text
    assert test_data[0]["op_field"][0] or test_data[0]["op_field"][1] in locator_by_id(fields[2]["op_id"]).text


def test_tc03():
    """
    Gombnyomásra helyesen végződik el a random művelet a fenti ABCs tábla alapján:
    * A megjelenő `chr` mezőben lévő karaktert kikeresve a táblában
    * Ha a `+` művelet jelenik meg akkor balra lépve ha a `-` akkor jobbra lépve
    * A `num` mezőben megjelenő mennyiségű karaktert
    * az `result` mező helyes karaktert fog mutatni
    """

    locator_by_id(fields[3]["submit_btn_id"]).click()
