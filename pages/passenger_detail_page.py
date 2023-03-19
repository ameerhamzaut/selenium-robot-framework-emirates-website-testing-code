import time

from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By

from base.common_method import BaseDriver


class passenger_detail_class(BaseDriver):

    def __init__(self, driver):
        self.driver = driver

    # locators
    gender_locator = "/html/body/form/div[3]/div[3]/div[4]/div[2]/div[8]/div/div[1]/div[1]/div/div[2]/fieldset[1]/div[1]/div/div/span[3]"
    gender_lists = "//li[@role='option']"
    first_name_locator = "/html/body/form/div[3]/div[3]/div[4]/div[2]/div[8]/div/div[1]/div[1]/div/div[2]/fieldset[1]/div[3]/div/input"
    last_name_locator = "/html/body/form/div[3]/div[3]/div[4]/div[2]/div[8]/div/div[1]/div[1]/div/div[2]/fieldset[1]/div[4]/div/input"
    save_and_next_locator = "/html/body/form/div[3]/div[3]/div[4]/div[2]/div[8]/div/div[1]/div[1]/div/div[2]/fieldset[3]/div/a/span"
    country_locator = "/html/body/form/div[3]/div[3]/div[4]/div[2]/div[8]/div/div[2]/div[1]/div/div/fieldset/div[2]/div[1]/div[1]/div/div[1]/input"
    country_list_locator = "/html/body/form/div[3]/div[3]/div[4]/div[2]/div[8]/div/div[2]/div[1]/div/div/fieldset/div[2]/div[1]/div[1]/div/div[2]/ul/li"
    phone_locator = "/html/body/form/div[3]/div[3]/div[4]/div[2]/div[8]/div/div[2]/div[1]/div/div/fieldset/div[2]/div[1]/div[2]/div/input"
    email_locator = "/html/body/form/div[3]/div[3]/div[4]/div[2]/div[8]/div/div[2]/div[1]/div/div/fieldset/div[2]/div[2]/div[1]/input"
    next_page_locator = "/html/body/form/div[3]/div[3]/div[4]/div[2]/div[8]/div/div[5]/div[1]/a"

    def gender_function(self):
        # gender = self.driver.find_element(By.XPATH, self.gender_locator)
        self.element_to_be_clicked(By.XPATH, self.gender_locator).click()
        # gender.click()
        gender_list = self.elements_to_be_present(By.XPATH, self.gender_lists)
        for lists in gender_list:
            if "Mr" in lists.text:
                lists.click()
                break

    def first_name_function(self, first_name_provide):
        first_name = self.driver.find_element(By.XPATH, self.first_name_locator)
        first_name.send_keys(first_name_provide)

    def last_name_function(self, last_name_provide):
        last_name = self.driver.find_element(By.XPATH, self.last_name_locator)
        last_name.send_keys(last_name_provide)
        time.sleep(2)
        next_button = self.driver.find_element(By.XPATH, self.save_and_next_locator)
        next_button.click()

    def country_function(self, country_location):
        country = self.driver.find_element(By.XPATH, self.country_locator)
        country.click()
        country.send_keys(country_location)
        country_list = self.driver.find_elements(By.XPATH, self.country_list_locator)
        try:
            for search_country in country_list:
                if "Pakistan (+92)" in search_country.text:
                    search_country.click()
                    break
        except StaleElementReferenceException as a:
            print(a)

    def number_function(self, number_provide):
        phone = self.driver.find_element(By.XPATH, self.phone_locator)
        phone.send_keys(number_provide)

    def email_function(self, email_provide):
        email = self.driver.find_element(By.XPATH, self.email_locator)
        email.send_keys(email_provide)
        clicks = self.driver.find_element(By.XPATH, self.next_page_locator)
        clicks.click()

    def passenger_detail_result(self, first_result, last_result, country_result, number_result, email_result):
        self.gender_function()
        self.first_name_function(first_result)
        self.last_name_function(last_result)
        self.country_function(country_result)
        self.number_function(number_result)
        self.email_function(email_result)
