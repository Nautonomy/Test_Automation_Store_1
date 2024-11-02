# IMPORTS
import random

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class BasePage:

    # INITIALIZER

    def __init__(self, driver):
        self.driver = driver

    # INTERACTIONS

    def go_to_url(self, url):
        self.driver.get(url)

    def find(self, locator):
        return self.driver.find_element(*locator)

    def text(self, locator, content, time: int = 10):
        self.wait_until_visible(locator, time)
        self.find(locator).send_keys(content)

    def text_and_hit_enter(self, locator, content, time: int = 10):
        self.wait_until_visible(locator, time)
        self.find(locator).send_keys(content)
        self.find(locator).send_keys(Keys.RETURN)

    def click(self, locator, time: int = 10):
        self.wait_until_visible(locator, time)
        self.find(locator).click()

    def point(self, locator, time: int = 10):
        self.wait_until_visible(locator, time)
        point_object = self.find(locator)
        ActionChains(self.driver).move_to_element(point_object).perform()

    def dropdown_selection_by_text(self, locator, text, time: int = 10):
        self.wait_until_visible(locator, time)
        dropdown_menu = Select(self.find(locator))
        dropdown_menu.select_by_visible_text(text)

    def dropdown_selection_by_index(self, locator, index: int = 2, time: int = 10):
        self.wait_until_visible(locator, time)
        dropdown_menu = Select(self.find(locator))
        dropdown_menu.select_by_index(index)

    # VALIDATIONS

    def wait_until_visible(self, locator, time: int = 10):
        wait = WebDriverWait(self.driver, time)
        wait.until(expected_conditions.visibility_of_element_located(locator))

    def check_if_element_is_visible(self, locator, time: int = 10):
        wait = WebDriverWait(self.driver, time)
        visibility = expected_conditions.visibility_of_element_located(locator)
        return visibility

    def random_item_from_dropdown_list(self, locator):
        dropdown_list = self.find(locator)
        select = Select(dropdown_list)
        items_list = [option.text for option in select.options]
        random_item = random.choice(items_list)
        return random_item
