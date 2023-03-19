import time
from selenium.webdriver.common.by import By

from base.common_method import BaseDriver


class seat_selection_class(BaseDriver):

    def __init__(self, driver):
        self.driver = driver

    # locators
    # seat_select_locator = "/html/body/form/div[3]/div[3]/div[4]/div[4]/div/div/div[3]/div[1]/div/div[2]/div[3]/a[1]"
    # img_click_locator = "/html/body/form/div[3]/div[3]/div[4]/div[4]/div/div/div[3]/div[2]/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div[1]/div[6]/div[1]/div[2]/div[4]/div/div/div[2]/table/tbody/tr[5]/td[9]/div/img"
    # confirm_seat_locator = "/html/body/form/div[3]/div[3]/div[4]/div[4]/div/div/div[3]/div[2]/div/div/div[2]/div[3]/div/div[1]/a"
    pop_up = "/html/body/form/div[3]/div[3]/div[4]/div[4]/div/div/div[3]/div[2]/div/div/div[2]/button"
    proceed_next_locator = "/html/body/form/div[3]/div[3]/div[4]/div[7]/div[3]/div[1]/a"

    #
    # def seat_selection_function(self):
    #     self.element_to_be_clicked(By.XPATH, self.seat_select_locator).click()

    # def pop_up_function(self):
    #     self.elements_to_be_present(By.XPATH, self.pop_up)
    #     self.element_to_be_clicked(By.XPATH, self.pop_up).click()

    # def img_function(self):
    #     self.element_to_be_present(By.XPATH, self.img_click_locator)
    #     self.element_to_be_clicked(By.XPATH, self.img_click_locator).click()
    #
    # def confirm_seat_function(self):
    #     self.element_to_be_clicked(By.XPATH, self.confirm_seat_locator).click()

    def proceed_function(self):
        self.element_to_be_clicked(By.XPATH, self.proceed_next_locator).click()

    def seat_selection_result(self):
        # self.seat_selection_function()
        # self.img_function()
        # self.confirm_seat_function()
        # self.pop_up_function()
        self.proceed_function()
