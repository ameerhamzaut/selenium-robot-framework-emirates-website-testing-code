import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseDriver:
    def __init__(self, driver, wait):
        self.wait = wait
        self.driver = driver

    def page_scroll(self):
        pageLength = self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);var pageLength=document.body.scrollHeight;return "
            "pageLength;")
        match = False
        while (match == False):
            lastCount = pageLength
            time.sleep(1)
            pageLength = self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);var pageLength=document.body.scrollHeight;return "
                "pageLength;")
            if lastCount == pageLength:
                match = True
        time.sleep(4)

    def element_to_be_clicked(self, locator_type, locator_location):
        wait = WebDriverWait(self.driver, 10)
        click_element = wait.until(EC.element_to_be_clickable((locator_type, locator_location)))
        return click_element

    def element_to_be_present(self, locator_type, locator_location):
        wait = WebDriverWait(self.driver, 10)
        present_element = wait.until(EC.presence_of_element_located((locator_type, locator_location)))
        return present_element

    def elements_to_be_present(self, locator_type, locator_location):
        wait = WebDriverWait(self.driver, 10)
        present_elements = wait.until(EC.presence_of_all_elements_located((locator_type, locator_location)))
        return present_elements
