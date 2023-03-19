# import logging
# import time
#
# from selenium.common import StaleElementReferenceException, TimeoutException
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
#
# from base.common_method import BaseDriver
#
#
# class launch_page_class(BaseDriver):
#
#     def __init__(self, driver):
#         self.driver = driver
#
#     # locators
#     cookies_locator = 'onetrust-accept-btn-handler'
#     going_from_locator = "//input[@type='component']"
#     wait_going_from_list = "/html/body/main/div[2]/div/div[2]/div[1]/div[2]/div/div/section/div[4]/div[1]/div[1]/div/div[1]/div/div/div[2]/section/ol/li/div/p"
#     going_from_searchlist = "/html/body/main/div[2]/div/div[2]/div[1]/div[2]/div/div/section/div[4]/div[1]/div[1]/div/div[1]/div/div/div[2]/section/ol/li/div/p"
#     going_to = "/html/body/main/div[2]/div/div[2]/div[1]/div[2]/div/div/section/div[4]/div[1]/div[1]/div/div[2]/div/div/div[1]/div/input"
#     wait_going_to_list = "/html/body/main/div[2]/div/div[2]/div[1]/div[2]/div/div/section/div[4]/div[1]/div[1]/div/div[1]/div/div/div[2]/section/ol/li/div/p"
#     going_to_searchlist = "//*[@id='panel0']/div[2]/div/div/section/div[4]/div[1]/div[1]/div/div[2]/div/div/div[2]/section/ol/li/div/p"
#     depart_locator = "//td[@class='ek-datepicker__day']"
#     arrival_locator = "//td[@class='ek-datepicker__day']"
#     wait_for_the_search_button = "/html/body/main/div[2]/div/div[2]/div[1]/div[2]/div/div/section/div[4]/div[2]/div[3]/form/button"
#     search_button = "/html/body/main/div[2]/div/div[2]/div[1]/div[2]/div/div/section/div[4]/div[2]/div[3]/form/button"
#     wait_for_the_presence_of_next_element = "//a[@id='option-0-1-0']"
#
#     def going_from_function(self, going_from_location):
#         self.element_to_be_clicked(By.ID, self.cookies_locator).click()
#         self.driver.execute_script("window.scrollTo(0, 400)")
#         going_from = self.element_to_be_present(By.XPATH, self.going_from_locator)
#         going_from.send_keys(going_from_location)
#         self.elements_to_be_present(By.XPATH, self.wait_going_from_list)
#         search_result = self.driver.find_elements(By.XPATH, self.going_from_searchlist)
#         try:
#             for search in search_result:
#                 if "LGW" in search.text:
#                     search.click()
#         except StaleElementReferenceException as e:
#             print(e)
#
#     def going_to_function(self, going_to_location):
#         going_to = self.element_to_be_present(By.XPATH, self.going_to)
#         going_to.send_keys(going_to_location)
#         self.element_to_be_present(By.XPATH, self.wait_going_to_list)
#         search_results = self.driver.find_elements(By.XPATH, self.going_to_searchlist)
#         try:
#             for arrive in search_results:
#                 if "KHI" in arrive.text:
#                     arrive.click()
#                     time.sleep(2)
#         except StaleElementReferenceException as a:
#             print(a)
#
#     # def depart_function(self, departure_date):
#     #     for date in self.depart_date_locator_field():
#     #         if date.get_attribute("data-string") == departure_date:
#     #             date.click()
#     #             time.sleep(2)
#     #             break
#
#     def depart_function(self, departure_date):
#         depart_date = self.driver.find_elements(By.XPATH, self.depart_locator)
#         for date in depart_date:
#             if date.get_attribute("data-string") == departure_date:
#                 try:
#                     wait = WebDriverWait(self.driver, 10)
#                     wait.until(EC.element_to_be_clickable((By.XPATH, self.depart_locator)))
#                 except TimeoutException:
#                     print("Timeout waiting for element to become clickable")
#                 else:
#                     date.click()
#                     time.sleep(2)
#                 break
#
#     def return_function(self, returned_date):
#         return_date = self.driver.find_elements(By.XPATH, self.arrival_locator)
#         for dates in return_date:
#             if dates.get_attribute("data-string") == returned_date:
#                 try:
#                     wait = WebDriverWait(self.driver, 10)
#                     wait.until(EC.element_to_be_clickable((By.XPATH, self.arrival_locator)))
#                 except TimeoutException:
#                     print("Timeout waiting for element to become clickable")
#                 else:
#                     dates.click()
#                     time.sleep(2)
#                 break
#         time.sleep(3)
#
#     def search_button_function(self):
#         try:
#             self.element_to_be_clicked(By.XPATH, self.search_button).click()
#
#         except StaleElementReferenceException as a:
#             print(a)
#
#         self.element_to_be_present(By.XPATH, self.wait_for_the_presence_of_next_element)
#
#
#
#
#         # launch_page_instance.remove_cookies_locator_field_function()
#         # launch_page_instance.going_from_field_function("london")
#         # launch_page_instance.going_to_field_function("karachi")
#         # launch_page_instance.select_Depart_date("2022023")
#         # launch_page_instance.select_Return_date("2522023")
#         # launch_page_instance.search_button()
#
#
#         # passenger_detail_page_instance.gender_function()
#         # passenger_detail_page_instance.first_name_function("Ameer")
#         # passenger_detail_page_instance.last_name_function("hamza")
#         # passenger_detail_page_instance.country_function("pakistan")
#         # passenger_detail_page_instance.number_function("3071323935")
#         # passenger_detail_page_instance.email_function("chhamza8700@gmail.com")
#
#         # flight_selection_page_instance.departure_function()
#         # flight_selection_page_instance.departure_economy_function()
#         # flight_selection_page_instance.arrival_function()
#         # flight_selection_page_instance.arrival_economy_function()
#         # flight_selection_page_instance.next_page_function()

# seat_selection_instance.seat_selection_function()
# seat_selection_instance.img_function()
# seat_selection_instance.confirm_seat_function()
# seat_selection_instance.proceed_function()


# payment_instance.payment_function()
#         payment_instance.country_function("pakistan")
#         payment_instance.address_function("madhali shareef sahiwal")
#         payment_instance.town_function("sahiwal")
#         payment_instance.checkbox_function()
#         payment_instance.payment_function()
