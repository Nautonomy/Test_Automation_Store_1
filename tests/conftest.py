import pytest
from selenium import webdriver


@pytest.fixture(autouse=True)
def driver():
    drv = webdriver.Chrome()
    drv.maximize_window()
    return drv
