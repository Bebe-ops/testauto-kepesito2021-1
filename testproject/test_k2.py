"""
## 2 Feladat: Színes reakció
Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.
Feladatod, hogy automatizáld selenium webdriverrel a Színes reakció app tesztelését.
Az ellenőrzésekhez használj `pytest` keretrendszert. A tesztjeidben használj `assert` összehasonlításokat használj!
Az alábbi teszteseteket kell lefedned:
"""
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.headless = False

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k2.html"
driver.get(URL)
time.sleep(2)

fields = [{"random_c_n_id": "randomColorName"}, {"t_color_id": "testColor"}, {"start_btn_id": "start"},
          {"stop_btn_id": "stop"}, {"result_id": "result"}, {"allcolors_id": "allcolors"},
          {"t_color_name_id": "testColorName"}]
test_data = [{"start_page_t_color": "[     ]"}, {"hit_result": "Correct!"}, {"no_hit_result": "Incorrect!"}]


def locator_by_id(f_id):
    element = driver.find_element_by_id(f_id)
    return element


all_colors = locator_by_id(fields[5]["allcolors_id"]).text
all_colors_list = all_colors.replace('"', "").replace(" ", "").split(",")


def start_stop():
    start_btn = locator_by_id(fields[2]["start_btn_id"])
    stop_btn = locator_by_id(fields[3]["stop_btn_id"])
    start_btn.click()
    time.sleep(3)
    stop_btn.click()


def test_tc01_start_page():
    """
    Helyesen jelenik meg az applikáció betöltéskor:
    * Alapból egy random kiválasztott szín jelenik meg az `==` bal oldalanán. A jobb oldalon csak a `[  ]`
    szimbólum látszik.
    <szín neve> [     ] == [     ]
    """
    assert locator_by_id(fields[0]["random_c_n_id"]).text in all_colors_list
    assert locator_by_id(fields[1]["t_color_id"]).text == test_data[0]["start_page_t_color"]


def test_tc02_start_stop():
    """
    El lehet indítani a játékot a `start` gommbal.
    * Ha elindult a játék akkor a `stop` gombbal le lehet állítani.
    """
    start_stop()
    start_btn = locator_by_id(fields[2]["start_btn_id"])
    stop_btn = locator_by_id(fields[3]["stop_btn_id"])
    assert start_btn.is_enabled()
    assert stop_btn.is_enabled()


def test_tc03_hits():
    """
    Eltaláltam, vagy nem találtam el.
    * Ha leállítom a játékot két helyes működés van, ha akkor állítom épp le
    amikor a bal és a jobb oldal ugyan azt a színt tartalmazza akkor a `Correct!` felirat jelenik meg.
      ha akkor amikor eltérő szín van a jobb és bal oldalon akkor az `Incorrect!` felirat kell megjelenjen.
    """
    test_color_name = locator_by_id(fields[6]["t_color_name_id"])
    rand_color_name = locator_by_id(fields[0]["random_c_n_id"])
    result = locator_by_id(fields[4]["result_id"])

    for _ in range(10):
        start_stop()
        if rand_color_name.text == test_color_name.text:
            assert result.text == test_data[1]["hit_result"]
        else:
            assert result.text == test_data[2]["no_hit_result"]
