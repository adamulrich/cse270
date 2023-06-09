# pip install selenium
from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


import time

class SearchParams():

    def __init__(self,       
        search_text = "", 
        color_black = False,
        color_blue = False, 
        color_white = False, 
        color_red = False, 
        color_green = False, 
        color_multicolor = False, 
        color_exclude_unselected = False,
        search_type_name = False,
        search_type_type = False,
        search_type_text = False,
        search_type_flavor_text = False,
        search_type_artist_text = False,
        search_type_set_number_text = False,
        power_operator = "",
        power_value = "",
        toughness_operator = "",
        toughness_value = "",
        cmc_operator = "",
        cmc_value = "",
        rarity_common = False,
        rarity_uncommon = False,
        rarity_rare = False,
        rarity_mythic = False,
        card_type = "",
        card_legality = "",
        card_set_filter = ""
        ):
        self.search_text = search_text
        self.color_black = color_black
        self.color_blue = color_blue
        self.color_white = color_white
        self.color_red = color_red
        self.color_green = color_green
        self.color_multicolor = color_multicolor
        self.color_exclude_unselected = color_exclude_unselected
        self.search_type_name = search_type_name
        self.search_type_type = search_type_type
        self.search_type_text = search_type_text
        self.search_type_flavor_text = search_type_flavor_text
        self.search_type_artist_text = search_type_artist_text
        self.search_type_set_number_text = search_type_set_number_text
        self.power_operator = power_operator
        self.power_value = power_value
        self.toughness_operator = toughness_operator
        self.toughness_value = toughness_value
        self.cmc_operator = cmc_operator
        self.cmc_value = cmc_value
        self.rarity_common = rarity_common
        self.rarity_uncommon = rarity_uncommon
        self.rarity_rare = rarity_rare
        self.rarity_mythic = rarity_mythic
        self.card_type = card_type
        self.card_legality = card_legality
        self.card_set_filter = card_set_filter

class test_mtg_vault_card_search(unittest.TestCase):

    def setUp(self):

        # reduce selenium noise
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        # set page load to eager to speed up the test
        caps = DesiredCapabilities().CHROME
        caps["pageLoadStrategy"] = "eager"

        #create webdriver
        self.browser = webdriver.Chrome(desired_capabilities=caps,
             options=options)

    # identifies html elements
    def loadElements(self):
        self.browser.get('https://www.mtgvault.com/cards/search/')
        
        self.search_textbox = self.browser.find_element(By.ID, 'ctl00_ContentPlaceHolder1_TextBox_SearchTerm')

        self.search_button = self.browser.find_element(By.ID, 'ctl00_ContentPlaceHolder1_Button_Search')

        self.name_radio_button = self.browser.find_element(By.ID, 'ctl00_ContentPlaceHolder1_RadioButtonList_SearchType_0')
        self.type_radio_button = self.browser.find_element(By.ID, 'ctl00_ContentPlaceHolder1_RadioButtonList_SearchType_1')
        self.text_radio_button = self.browser.find_element(By.ID, 'ctl00_ContentPlaceHolder1_RadioButtonList_SearchType_2')
        self.flavor_text_radio_button = self.browser.find_element(By.ID, 'ctl00_ContentPlaceHolder1_RadioButtonList_SearchType_3')
        self.artist_radio_button = self.browser.find_element(By.ID, 'ctl00_ContentPlaceHolder1_RadioButtonList_SearchType_4')
        self.set_number_radio_button = self.browser.find_element(By.ID, 'ctl00_ContentPlaceHolder1_RadioButtonList_SearchType_5')

        self.color_white_checkbox = self.browser.find_element(By.ID, 'ctl00_ContentPlaceHolder1_CheckBox_Color_White')       
        self.color_blue_checkbox = self.browser.find_element(By.ID, 'ctl00_ContentPlaceHolder1_CheckBox_Color_Blue')        
        self.color_black_checkbox = self.browser.find_element(By.ID, 'ctl00_ContentPlaceHolder1_CheckBox_Color_Black')        
        self.color_red_checkbox = self.browser.find_element(By.ID, 'ctl00_ContentPlaceHolder1_CheckBox_Color_Red')        
        self.color_green_checkbox = self.browser.find_element(By.ID, 'ctl00_ContentPlaceHolder1_CheckBox_Color_Green')
        self.color_multi_checkbox = self.browser.find_element(By.ID, 'ctl00_ContentPlaceHolder1_CheckBox_MultiColored')
        self.color_exclude_unselected_checkbox = self.browser.find_element(By.ID, 'ctl00_ContentPlaceHolder1_CheckBox_ExcludeUnselected')        

        self.power_operator_dropdown = Select(self.browser.find_element(By.ID, 'ctl00_ContentPlaceHolder1_DropDownList_Power_Operator'))
        self.power_value_dropdown = Select(self.browser.find_element(By.ID, 'ctl00_ContentPlaceHolder1_DropDownList_Power_Value'))

        self.toughness_operator_dropdown = Select(self.browser.find_element(By.ID, 'ctl00_ContentPlaceHolder1_DropDownList_Toughness_Operator'))
        self.toughness_value_dropdown = Select(self.browser.find_element(By.ID, 'ctl00_ContentPlaceHolder1_DropDownList_Toughness_Value'))

        self.cmc_operator_dropdown = Select(self.browser.find_element(By.ID, 'ctl00_ContentPlaceHolder1_DropDownList_ManaCost_Operator'))
        self.cmc_value_textbox = self.browser.find_element(By.ID, 'ctl00_ContentPlaceHolder1_TextBox_ManaCost_Value')
        
        self.common_checkbox = self.browser.find_element(By.ID, 'ctl00_ContentPlaceHolder1_CheckBox_Rarity_Common')       
        self.uncommon_checkbox = self.browser.find_element(By.ID, 'ctl00_ContentPlaceHolder1_CheckBox_Rarity_Uncommon')       
        self.rare_checkbox = self.browser.find_element(By.ID, 'ctl00_ContentPlaceHolder1_CheckBox_Rarity_Rare')       
        self.mythic_checkbox = self.browser.find_element(By.ID, 'ctl00_ContentPlaceHolder1_CheckBox_Rarity_MythicRare')       

        self.card_type_dropdown = Select(self.browser.find_element(By.ID, 'ctl00_ContentPlaceHolder1_DropDownList_Type'))
        self.card_legality_dropdown = Select(self.browser.find_element(By.ID, 'ctl00_ContentPlaceHolder1_DropDownList_Legality')) 

        self.card_set_filter_listbox = Select(self.browser.find_element(By.ID, 'ctl00_ContentPlaceHolder1_ExtendedListBox_Expansions'))

    # search test helper. 
    # this function will drive the UI based on the search_params object,
    # then will confirm the result count == expected count
    def search_helper(self, search_params: SearchParams, expected_count):

        self.loadElements()
        
        if search_params.search_text != "":
            self.search_textbox.send_keys(search_params.search_text)

        if search_params.card_legality != "":
            self.card_legality_dropdown.select_by_visible_text(search_params.card_legality)
            
        if search_params.card_set_filter != "":
            self.card_set_filter_listbox.select_by_visible_text(search_params.card_set_filter)

        if search_params.card_type != "":
            self.card_type_dropdown.select_by_visible_text(search_params.card_type)

        if search_params.cmc_operator != "":
            self.cmc_operator_dropdown.select_by_visible_text(search_params.cmc_operator)

        if search_params.cmc_value != "":
            self.cmc_value_textbox.send_keys(search_params.cmc_value)

        if search_params.color_black:
            self.color_black_checkbox.click()
        
        if search_params.color_blue:
            self.color_blue_checkbox.click()
        
        if search_params.color_exclude_unselected:
            self.color_exclude_unselected_checkbox.click()
            
        if search_params.color_green:
            self.color_green_checkbox.click()
        
        if search_params.color_multicolor:
            self.color_multi_checkbox.click()

        if search_params.color_red:
            self.color_red_checkbox.click()
        
        if search_params.color_white:
            self.color_white_checkbox.click()

        if search_params.power_operator != "":
            self.power_operator_dropdown.select_by_visible_text(search_params.power_operator)

        if search_params.power_value != "":
            self.power_value_dropdown.select_by_visible_text(search_params.power_value)

        if search_params.rarity_common:
            self.common_checkbox.click()

        if search_params.rarity_mythic:
            self.mythic_checkbox.click()

        if search_params.rarity_rare:
            self.rare_checkbox.click()

        if search_params.rarity_uncommon:
            self.uncommon_checkbox.click()
        
        if search_params.search_type_artist_text:
            self.artist_radio_button.click()

        if search_params.search_type_flavor_text:
            self.flavor_text_radio_button.click()
        
        if search_params.search_type_name:
            self.name_radio_button.click()
    
        if search_params.search_type_set_number_text:
            self.set_number_radio_button.click()
        
        if search_params.search_type_text:
            self.text_radio_button.click()

        if search_params.search_type_type:
            self.type_radio_button.click()

        if search_params.toughness_operator != "":
            self.toughness_operator_dropdown.select_by_visible_text(search_params.toughness_operator)
        
        if search_params.toughness_value != "":
            self.toughness_value_dropdown.select_by_visible_text(search_params.toughness_value)

        # now search, wait a second for the results
        self.search_button.click()

        # try to get the result count
        elements = []
        count =  0
            
            # get the html element
        while True:
            # find the element
            elements = self.browser.find_elements(By.XPATH, "/html/body/form/div[4]/div[2]/div[3]/p")
            # if we have it, then break out
            if len(elements) != 0 or count >= 5:
                break
            else:
            # increment and wait a second
                count += 1
                time.sleep(1)

        # if we never found the right element, assert
        if len(elements) == 0:        
            self.assertTrue(False,"could not find result count")
            return

        else:
            result_count = eval(elements[0].text.split(" ")[1])

        #check count
        self.assertEqual(result_count, expected_count, "expected count not equal")


    # set text = mill
    # check color blue
    # select search type text
    # select all sets
    # should return 73
    def test_01_text_search(self):

        search = SearchParams(
            search_text="mill", 
            color_blue=True, 
            search_type_text=True, 
            card_set_filter= "All Sets"
        )

        self.search_helper(search,73)

    # set text = vigilance
    # check color white
    # select search type text
    # select card set to All Sets
    # should return 456
    def test_02_text_color_white(self):

        search = SearchParams(
            search_text="vigilance", 
            color_white=True, 
            search_type_text=True, 
            card_set_filter= "All Sets"
        )

        self.search_helper(search,456)

    # check exclude unselected
    # select card type = "Instant"
    # select search type = "Text"
    # set text search = "exile"
    # select card set to All Sets
    # should return 3
    def test_03_exclude_color_exile_instant(self):

        search = SearchParams(
            
            color_exclude_unselected=True,
            card_type="Instant",
            search_type_text=True,
            card_set_filter= "All Sets",
            search_text="exile"
        )

        self.search_helper(search,3)

    # check color green
    # set power operator to '>='
    # set power value to '10'
    # select card set to All Sets
    # should return 25
    def test_04_green_power_greater_equal_10(self):

        search = SearchParams(
            
            color_green=True,
            power_operator=">=",
            power_value="10",
            card_set_filter= "All Sets"
        )

        self.search_helper(search,25)

    # check exclude unselected
    # set toughness operator to '<='
    # set toughness value to '1'
    # should return 247
    def test_05_no_color_toughness_less_than_or_equqal_1(self):

        search = SearchParams(
            
            color_exclude_unselected=True, 
            toughness_operator= "<=",
            toughness_value="1",
        )

        self.search_helper(search,247)

    # check rarity rare
    # check exclude unselected
    # set cmc operator to '='
    # set cmc value to '0'
    # should return 42
    def test_06_rare_no_color_filter_cmc_equals_0(self):

        search = SearchParams(
            rarity_rare=True,
            color_exclude_unselected=True,
            cmc_operator="=",
            cmc_value="0"
        )

        self.search_helper(search,42)
    
    # check rarity rare
    # check rarity mythic
    # select card set MOM: Aftermath
    # should return 35
    def test_07_multi_rarity(self):
        
        search = SearchParams(
            rarity_rare=True,
            rarity_mythic=True,
            card_set_filter= "March of the Machine: The Aftermath"
        )

        self.search_helper(search,35)

    # check exclude unselected
    # check multicolor
    # select legal in standard
    # should return 253
    def test_08_standard_legal(self):

        search = SearchParams(
            color_exclude_unselected=True,
            color_multicolor=True,
            card_legality="Legal in Standard"
        )

        self.search_helper(search,253)

    # set text = ally
    # select search type text
    # should return 96
    def test_09_ally(self):

        search = SearchParams(
            search_text="ally",
            search_type_type=True
        )

        self.search_helper(search,96)

    # set text = obedience
    # select flavor text type
    # should return 6
    def test_10_obedience_flavor_text(self):

        search = SearchParams(
            search_text="obedience",
            search_type_flavor_text=True
        )

        self.search_helper(search,6)

    # set text = john matson
    # select artist text type
    # should return 106
    def test_11_artist(self):

        search = SearchParams(
            search_text="john matson",
            search_type_artist_text=True
        )

        self.search_helper(search,106)

    # check rarity rare
    # check rarity uncommon
    # set cmc operator to "="
    # set cmc value to "X"
    # should return 61
    def test_12_rare_uncommon_CMC_X(self):

        search = SearchParams(
            rarity_rare=True,
            rarity_uncommon=True,
            cmc_operator="=",
            cmc_value="X"
        )

        self.search_helper(search,61)




if __name__ == '__main__':
    unittest.main(verbosity=2, warnings='ignore')
