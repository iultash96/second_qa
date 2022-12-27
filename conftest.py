import pytest as pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

"""Открытие браузера"""


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield driver
    driver.quit()
