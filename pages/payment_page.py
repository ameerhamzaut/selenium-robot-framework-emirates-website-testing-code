import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.common_method import BaseDriver


class payment_class(BaseDriver):

    def __init__(self, driver):
        self.driver = driver
    #locators
    paypall_locator = "/html/body/div[1]/main/div[5]/div[2]/div[1]/div/div/section/div/div/div[1]/div/div[2]/div/ul/li[3]/div[1]/div/button"
    country_Wait_locator = "/html/body/div[1]/main/div[5]/div[2]/div[1]/div/div/section/div/div/div[1]/div/div[2]/div/ul/li[3]/div[2]/div/div/div/fieldset/div/div[2]/div/div/div[2]/span/span/input"
    country_locator = "/html/body/div[1]/main/div[5]/div[2]/div[1]/div/div/section/div/div/div[1]/div/div[2]/div/ul/li[3]/div[2]/div/div/div/fieldset/div/div[2]/div/div/div[2]/span/span/input"
    address_locator = "/html/body/div[1]/main/div[5]/div[2]/div[1]/div/div/section/div/div/div[1]/div/div[2]/div/ul/li[3]/div[2]/div/div/div/fieldset/div/div[3]/span/span/input"
    town_locator = "/html/body/div[1]/main/div[5]/div[2]/div[1]/div/div/section/div/div/div[1]/div/div[2]/div/ul/li[3]/div[2]/div/div/div/fieldset/div/div[6]/div[1]/span/span/input"
    checkbox_locator = "/html/body/div[1]/main/div[5]/div[2]/div[2]/div[2]/div/div/div[2]/label"
    payment_locator = "/html/body/div[1]/main/div[5]/div[2]/div[2]/div[2]/div/div/div[3]/div[1]/button"

    def paypall_function(self):
        self.element_to_be_clicked(By.XPATH, self.paypall_locator).click()

    def country_function(self, country_location):
        self.elements_to_be_present(By.XPATH, self.country_Wait_locator)
        country = self.driver.find_element(By.XPATH, self.country_locator)
        country.send_keys(country_location)

    def address_function(self, address_location):
        self.element_to_be_present(By.XPATH, self.address_locator)
        address = self.driver.find_element(By.XPATH, self.address_locator)
        address.send_keys(address_location)

    def town_function(self, town_location):
        self.elements_to_be_present(By.XPATH, self.town_locator)
        town = self.driver.find_element(By.XPATH, self.town_locator)
        town.send_keys(town_location)

    def checkbox_function(self):
        self.element_to_be_clicked(By.XPATH, self.checkbox_locator).click()


    def payment_function(self):
        self.element_to_be_clicked(By.XPATH, self.paypall_locator).click()


    def payment_result(self, country_result, address_result, town_result):
        self.paypall_function()
        self.country_function(country_result)
        self.address_function(address_result)
        self.town_function(town_result)
        self.checkbox_function()
        self.payment_function()