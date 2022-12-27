from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
"""Родительский класс и функция для открытия браузера по ссылке"""

class BasePage():
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)
# """Функция ожидания что бы элемент был видимым"""

    def element_is_visible(self, timeout=5, locator=None):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def element_are_visible(self, timeout=5, locator=None):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, timeout=5, locator=None):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def element_are_present(self, timeout=5, locator=None):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, timeout=5, locator=None):
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def go_to_element(self, element):
        self.driver.execute_script("argument[0].scrollIntoView();")
