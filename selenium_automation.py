# pip install selenium

from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
import time

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()      
        # self.addCleanup(self.browser.refresh)  

    def loadElements(self):

        # test javascript implementation
        #self.browser.get('https://adamulrich.github.io/javascript_calculator/')

        # test typescript implementation
        self.browser.get('https://adamulrich.github.io/typescript-calculator/public/index.html')

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
        self.divide_button =self.browser.find_element(By.ID,"divide")
        self.equals_button = self.browser.find_element(By.ID,"equals")
        self.main_display = self.browser.find_element(By.ID,"display")
        self.plus_minus_button = self.browser.find_element(By.ID,"plus_minus")
        self.decimal_button = self.browser.find_element(By.ID,"dot")
        self.clear_button = self.browser.find_element(By.ID,"clear")
        self.all_clear_button = self.browser.find_element(By.ID,"all_clear")
        self.back_button = self.browser.find_element(By.ID,"backspace")

        self.buttons = {
            "1": self.one_button,
            "2": self.two_button,
            "3": self.three_button,
            "4": self.four_button,
            "5": self.five_button,
            "6": self.six_button,
            "7": self.seven_button,
            "8": self.eight_button,
            "9": self.nine_button,
            "0": self.zero_button,
            ".": self.decimal_button,
            "/": self.divide_button,
            "*": self.multiply_button,
            "+": self.plus_button,
            "-": self.minus_button,
            "=": self.equals_button,
            "<": self.back_button,
            "C": self.clear_button,
            "A": self.all_clear_button,
            "±": self.plus_minus_button
        }

    def test_addition(self):
        self.computation_helper("127+255=","382")

    def test_negative_number(self):
        self.computation_helper("3±", "-3")

    def test_multiplication(self):
        self.computation_helper("25*25=", "625")

    def test_division(self):
        self.computation_helper("25/2=", "12.5")

    def test_clear(self):
        self.computation_helper("25/2C5=", "5")

    def test_clear_new_operand(self):
        self.computation_helper("25/2C*5=", "125")
    
    def test_allclear(self):
        self.computation_helper("25*5=A", "0")

    def test_backspace(self):
        self.computation_helper("50+500<=", "100")

    def test_multiply_negative(self):
        self.computation_helper("127±*127=","-16129")

    def test_divide_two_negatives(self):
        self.computation_helper("12±/3=","-4")

    def test_add_twelve_digit_numbers(self):
        self.computation_helper("123456789012+123456789012=","246913578024")
    
    def test_add_string_of_digits(self):
        self.computation_helper("1+2+3+4=","10")

    def test_complex_calculation(self):
        self.computation_helper("34/17+5*10-1=","69")




    def computation_helper(self, expression, result):
        
        self.loadElements()

        for button in expression:
            self.buttons[button].click()
            time.sleep(0.1)
        
        
        self.assertEqual(self.main_display.text,result, f"main display is not equal to {result}.")
        



if __name__ == '__main__':
    unittest.main(verbosity=2)

