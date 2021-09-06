"""
## 5 Feladat: Bingo

Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.
Feladatod, hogy automatizáld selenium webdriverrel a Bingoapp tesztelését.
Az applikáció indulo bingo táblája minden frissítésnél véletlenszerűen változik!
Az ellenőrzésekhez használj `pytest` keretrendszert. A tesztjeidben használj `assert` összehasonlításokat használj!

A feladatod az alábbi tesztesetek lefejlesztése:
"""

import time
from selenium import webdriver   # kell a PIP hozzá: pip install selenium
from selenium.webdriver.chrome.options import Options  # headless módhoz többek között
from webdriver_manager.chrome import ChromeDriverManager  # webdriverManager, kell a PIP: pip install webdriver-manager

options = Options()
options.headless = False

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k5.html"
driver.get(URL)
time.sleep(2)

fields = [{"bingo_tds": "//td"}, {"numbers": "//ol//li"}, {"": ""}, {"": ""}, {"": ""}, {"": ""}, {"": ""}]


def locators_by_xp(f_xp):
    elements = driver.find_elements_by_xpath(f_xp)
    return elements


def test_tc01():
    """
    Az applikáció helyesen megjelenik:
    * A bingo tábla 25 darab cellát tartalmaz
    * A számlista 75 számot tartalmaz
    """
    test_data_tc01 = [{"bingo_table_cells": "25"}, {"numbers": "75"}]
    bingo_cells = locators_by_xp(fields[0]["bingo_tds"])
    assert len(bingo_cells) == test_data_tc01[0]["bingo_table_cells"]

    numbers = locators_by_xp(fields[1]["numbers"])
    assert numbers == test_data_tc01[1][numbers]


def test_tc02():
    """
     Bingo számok ellenőzrzése:
    * Addig nyomjuk a `play` gobot amíg az első bingo felirat meg nem jelenik
    * Ellenőrizzük, hogy a bingo sorában vagy oszlopában lévő számok a szelvényről tényleg a már kihúzott számok közül
      kerültek-e ki
    """


def test_tc03():
    """
    Új játékot tudunk indítani
    * az init gomb megnyomásával a felület visszatér a kiindulási értékekhez
    * új bingo szelvényt kapunk más számokkal.
    """