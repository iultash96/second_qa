import time

from locators.elements_page_locators import TextBoxPageLocators
from pages.base_page import BasePage
import time

"""Заполнение полей"""


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        self.element_is_visible(self.locators.FULL_NAME).send_keys('sdjgfhvsd')
        self.element_is_visible(self.locators.EMAIL).send_keys('sdfgvsdf@gmail.com')
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys('address')
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys('adress2')
        self.element_is_visible(self.locators.SUBMIT).click()
        time.sleep(5)
