import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from base.common_method import BaseDriver


class flight_selection_class(BaseDriver):

    def __init__(self, driver):
        self.driver = driver

    # locator
    departure_locator = "//a[@id='option-0-1-0']"
    departure_economy_locator = "/html/body/form/div[3]/div[3]/div[9]/div/div[15]/div[2]/div[1]/div[3]/div[1]/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/div/table/tbody[3]/tr[2]/td/div/a/span[2]"
    arrival_locator = "//a[@id='option-1-1-0']"
    arrival_economy_locator = "/html/body/form/div[3]/div[3]/div[9]/div/div[15]/div[2]/div[2]/div[3]/div[1]/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/div/table/tbody[3]/tr[2]/td/div/a/span[2]"
    next_page_locator = "/html/body/form/div[3]/div[3]/div[9]/div/div[15]/div[8]/div[1]/a"

    def departure_function(self):
        self.element_to_be_clicked(By.XPATH, self.departure_locator).click()

    def departure_economy_function(self):
        self.element_to_be_clicked(By.XPATH, self.departure_economy_locator).click()
        # depart_economy_flight = self.driver.find_element(By.XPATH, self.departure_economy_locator)
        # depart_economy_flight.click()

    def arrival_function(self):
        self.element_to_be_clicked(By.XPATH, self.arrival_locator).click()
        # arrival_flight = self.driver.find_element(By.XPATH, self.arrival_locator)
        # arrival_flight.click()

    def arrival_economy_function(self):
        self.element_to_be_clicked(By.XPATH, self.arrival_economy_locator).click()
        # arrival_economy_flight = self.driver.find_element(By.XPATH, self.arrival_economy_locator)
        # arrival_economy_flight.click()

    def next_page_function(self):
        self.element_to_be_present(By.XPATH, self.next_page_locator)
        self.element_to_be_clicked(By.XPATH, self.next_page_locator).click()

    def flight_selection_page_result(self):
        self.departure_function()
        self.departure_economy_function()
        self.arrival_function()
        self.arrival_economy_function()
        self.next_page_function()