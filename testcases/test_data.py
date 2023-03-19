

import pytest
import softest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from ddt import ddt, data, unpack
from pages.flight_selection_page import flight_selection_class
from pages.launch_page import launch_page_class
from pages.passenger_detail_page import passenger_detail_class
from pages.payment_page import payment_class
from pages.seat_selection_page import seat_selection_class
from selenium.webdriver.support import expected_conditions as EC

from utilities.utils import Utils


@pytest.mark.usefixtures("setupForBrowsers")
@ddt
class TestFirst(softest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.launch_page_instance = launch_page_class(self.driver)
        self.passenger_detail_instance = passenger_detail_class(self.driver)
        self.payment_page_instance = payment_class(self.driver)
        self.ut = Utils()

    # launch_page_test
    # @data(*Utils.read_data_from_excel("C:\\Users\\ameer\\Documents\\SecondProject\\testdata\\tdataexcel.xlsx", "Sheet1"))
    # @unpack
    @data(*Utils.read_data_from_csv("C:\\Users\\ameer\\Documents\\SecondProject\\testdata\\tdatacsv.csv"))
    # @data(("london", "karachi", "2032023", "2542023", "Ameer", "Hamza", "pakistan", "3071323935", "chhamza8700@gmail.com", "pakistan", "madhali shareef sahiwal", "sahiwal"))
    @unpack
    def test_function(self, first, second, third, forth, fifth, sixth, seven, eight, nine, ten, eleven, twelve):
        self.launch_page_instance.launch_page_result(first, second, third, forth)
        WebDriverWait(self.driver, 100).until(
                EC.presence_of_element_located((By.XPATH, "//a[@id='option-0-1-0']")))

        flight_selection_page_instance = flight_selection_class(self.driver)
        flight_selection_page_instance.flight_selection_page_result()
        WebDriverWait(self.driver, 100).until(
            EC.presence_of_element_located((By.XPATH,
                                            "/html/body/form/div[3]/div[3]/div[4]/div[2]/div[6]/div/table/tbody/tr/td/div/div/div[1]/img")))

    # passenger_detail_page_test
        self.passenger_detail_instance.passenger_detail_result(fifth, sixth, seven, eight, nine)
        WebDriverWait(self.driver, 100).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/form/div[3]/div[3]/div[4]/div[1]/div/div/div[1]/ul/li[1]/a")))

    # seat_selection_page_test
        seat_selection_instance = seat_selection_class(self.driver)
        seat_selection_instance.seat_selection_result()
        WebDriverWait(self.driver, 100).until(
            EC.presence_of_element_located(
                (By.XPATH,
                 "/html/body/div[1]/main/div[5]/div[2]/div[1]/div/div/section/div/div/div[1]/div/div[2]/div/ul/li[1]/div[1]/div/button/img")))

    # payment_page_test
        self.payment_page_instance.payment_result(ten, eleven, twelve)
