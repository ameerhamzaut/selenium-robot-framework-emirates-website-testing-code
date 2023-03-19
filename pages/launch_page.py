import logging
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC

from base.common_method import BaseDriver
from utilities.utils import Utils


class launch_page_class(BaseDriver):
    log = Utils.custom_logger(logLevel=logging.WARNING)

    def __init__(self, driver):
        self.driver = driver
        # self.wait = wait

    # locators
    remove_cookies_locator = "onetrust-accept-btn-handler"
    scroll_window = "window.scrollTo(0, 500);"
    going_from_locator = "//input[@type='component']"
    wait_going_from_locator = "/html/body/main/div[2]/div/div[2]/div[1]/div[2]/div/div/section/div[4]/div[1]/div[1]/div/div[1]/div/div/div[2]/section/ol/li/div/p"
    going_from_locator_searchList = "/html/body/main/div[2]/div/div[2]/div[1]/div[2]/div/div/section/div[4]/div[1]/div[1]/div/div[1]/div/div/div[2]/section/ol/li/div/p"
    going_from_location_condition = "LGW"
    going_to_locator = "/html/body/main/div[2]/div/div[2]/div[1]/div[2]/div/div/section/div[4]/div[1]/div[1]/div/div[2]/div/div/div[1]/div/input"
    wait_going_to_locator = "/html/body/main/div[2]/div/div[2]/div[1]/div[2]/div/div/section/div[4]/div[1]/div[1]/div/div[1]/div/div/div[2]/section/ol/li/div/p"
    going_to_locator_searchList = "//*[@id='panel0']/div[2]/div/div/section/div[4]/div[1]/div[1]/div/div[2]/div/div/div[2]/section/ol/li/div/p"
    going_to_location_condition = "KHI"
    depart_date_locator = "//td[@class='ek-datepicker__day']"
    return_date_locator = "//td[@class='ek-datepicker__day']"
    search_buttons = '/html/body/main/div[2]/div/div[2]/div[1]/div[2]/div/div/section/div[4]/div[2]/div[3]/form/button'
    wait_for_the_presence_of_next_element = "/html/body/form/div[3]/div[3]/div[6]/div/div[1]/div/div[1]/p[2]/a"

    # locator_field
    def remove_cookies_locator_field(self):
        return self.element_to_be_clicked(By.ID, self.remove_cookies_locator)

    def going_from_locator_field(self):
        return self.driver.find_element(By.XPATH, self.going_from_locator)

    def going_to_locator_field(self):
        return self.driver.find_element(By.XPATH, self.going_to_locator)

    def depart_date_locator_field(self):
        return self.driver.find_elements(By.XPATH, self.depart_date_locator)

    def return_date_locator_field(self):
        return self.driver.find_elements(By.XPATH, self.return_date_locator)

    def search_button_field(self):
        return self.element_to_be_clicked(By.XPATH, self.search_buttons)

    # locator_field_function

    def remove_cookies_locator_field_function(self):
        d = self.remove_cookies_locator_field()
        d.click()
        self.log.warning("clicked on the cookies accept button")
        self.driver.execute_script(self.scroll_window)

    def going_from_field_function(self, location):
        a = self.going_from_locator_field()
        a.send_keys(location)
        self.log.warning("enter london location in the input field")
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.XPATH, self.wait_going_from_locator)))
        search_result = self.driver.find_elements(By.XPATH, self.going_from_locator_searchList)
        try:
            for search in search_result:
                if self.going_from_location_condition in search.text:
                    search.click()
                    self.log.warning("clicked on the london bsed on the LGW location")
        except StaleElementReferenceException as e:
            print(e)

    def going_to_field_function(self, locations):
        b = self.going_to_locator_field()
        b.send_keys(locations)
        time.sleep(5)
        self.log.warning("enter the karachi location in the input fields")
        WebDriverWait(self.driver, 50).until(
            EC.presence_of_all_elements_located((By.XPATH, self.wait_going_to_locator)))
        search_results = self.driver.find_elements(By.XPATH, self.going_to_locator_searchList)
        try:
            for arrive in search_results:
                if self.going_to_location_condition in arrive.text:
                    arrive.click()
                    self.log.warning("clicked on karachi based on KHI location")


        except StaleElementReferenceException as a:
            print(a)

    def select_Depart_date(self, select):
        for date in self.depart_date_locator_field():
            if date.get_attribute("data-string") == select:
                date.click()
                self.log.warning("clicked on the departure date")
                break

    def select_Return_date(self, selects):
        for dates in self.return_date_locator_field():
            if dates.get_attribute("data-string") == selects:
                dates.click()
                self.log.warning("clicked on the return location")
                break

    def search_button(self):
        try:
            self.search_button_field().click()
            self.log.warning("clicked on the search button")
        except TimeoutException as ex:
            print(ex)

    def launch_page_result(self, going_from_result, going_to_result, depart_date_result, arrival_data_result):
        self.remove_cookies_locator_field_function()
        self.going_from_field_function(going_from_result)
        self.going_to_field_function(going_to_result)
        self.select_Depart_date(depart_date_result)
        self.select_Return_date(arrival_data_result)
        self.search_button()
