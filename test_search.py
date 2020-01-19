import pytest
from selenium import webdriver
from time import sleep


@pytest.fixture()
def wd():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1200,800")
    wd = webdriver.Chrome("chromedriver.exe", options=options)
    yield wd
    wd.quit()


def test_search(wd):
    wd.get("https://www.mytheresa.com/en-de/")
    search_field = wd.find_element_by_css_selector("#search")
    search_field.send_keys("Gucci bags")
    wd.find_element_by_css_selector(
        "#search_mini_form > div > button").submit()
    assert len(wd.find_elements_by_css_selector(".item")) > 0
    assert wd.find_elements_by_css_selector(".ph1")[0].text == "GUCCI"
