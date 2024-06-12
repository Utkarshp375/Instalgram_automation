import pytest
import configparser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
confi=configparser.ConfigParser()
confi.read("utilites/input.properties")
@pytest.fixture
def setup(request):
    options = Options()
    options.add_experimental_option("detach",True)
    request.cls.driver=webdriver.Chrome(options=options)
    request.cls.driver.maximize_window()
    request.cls.driver.get(confi.get("confi","base_url"))
    yield
    request.cls.driver.quit()
