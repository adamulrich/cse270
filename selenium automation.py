from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()      
        # self.addCleanup(self.browser.refresh)  

    def loadElements(self):
        self.browser.get('https://adamulrich.github.io/javascript_calculator/')
        self.one_button = self.browser.find_element(By.ID, "1")
        self.two_button = self.browser.find_element(By.ID,"2")
        self.three_button = self.browser.find_element(By.ID,"3")
        self.four_button = self.browser.find_element(By.ID,"4")
        self.five_button = self.browser.find_element(By.ID,"5")
        self.six_button = self.browser.find_element(By.ID,"6")
        self.seven_button = self.browser.find_element(By.ID,"7")
        self.eight_button = self.browser.find_element(By.ID,"8")
        self.nine_button = self.browser.find_element(By.ID,"9")
        self.zero_button = self.browser.find_element(By.ID,"0")
        self.plus_button = self.browser.find_element(By.ID,"plus")
        self.minus_button = self.browser.find_element(By.ID,"minus")
        self.multiply_button = self.browser.find_element(By.ID,"multiply")
        self.divide_button = self.browser.find_element(By.ID,"divide")
        self.equals_button = self.browser.find_element(By.ID,"equals")
        self.main_display = self.browser.find_element(By.ID,"display")
        self.plus_minus_button = self.browser.find_element(By.ID,"plus_minus")
        self.decimal_button = self.browser.find_element(By.ID,"dot")
        self.clear_button = self.browser.find_element(By.ID,"clear")
        self.all_clear_button = self.browser.find_element(By.ID,"all_clear")
        self.back_button = self.browser.find_element(By.ID,"backspace")


    def test_addition(self):
        self.loadElements()

        self.one_button.click()
        self.two_button.click()
        self.seven_button.click()

        self.plus_button.click()

        self.two_button.click()
        self.five_button.click()
        self.five_button.click()

        self.equals_button.click()

        self.assertIn(self.main_display.text,'382', "main display is not equal to 382; it is " + self.main_display.text)


    def test_negative_number(self):
        self.loadElements()

        self.three_button.click()
        self.plus_minus_button.click()

        self.assertIn(self.main_display.text,'-3', "main display is not equal to -3; it is " + self.main_display.text)


if __name__ == '__main__':
    unittest.main(verbosity=2)

