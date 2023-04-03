from locators.homePageLocator import *
from .baseElement import BaseElement, Locator
from selenium.webdriver.common.by import By

class  HomePage:
    def __init__(self, driver):
        self.driver = driver
    
    @property
    def input_email(self):
        locator = Locator(by=By.ID, value=get_email_input_id())
        return BaseElement(
            driver=self.driver,
            locator=locator
        )
        
    @property    
    def get_access_early_btn(self):
        locator = Locator(by=By.XPATH, value=get_early_access_button_xpath())
        return BaseElement(
            driver=self.driver,
            locator=locator
        )
     
    @property    
    def scroll_down_btn(self):
        locator = Locator(by=By.XPATH, value=get_scroll_down_button_xpath())
        return BaseElement(
            driver=self.driver,
            locator=locator
        )
        
    @property
    def comming_days(self):
        locator = Locator(by=By.ID, value=get_comming_days_id())
        return BaseElement(
            driver=self.driver,
            locator=locator
        )
        
    @property
    def title1_section1(self):
        locator = Locator(by=By.XPATH, value=get_title1_section1_xpath())
        return BaseElement(
            driver=self.driver,
            locator=locator
        )
        
    @property
    def title2_section1(self):
        locator = Locator(by=By.XPATH, value=get_title2_section1_xpath())
        return BaseElement(
            driver=self.driver,
            locator=locator
        )
        
    @property
    def title3_section1(self):
        locator = Locator(by=By.XPATH, value=get_title3_section1_xpath())
        return BaseElement(
            driver=self.driver,
            locator=locator
        )
        
    @property
    def right_btn(self):
        locator = Locator(by=By.XPATH, value=get_right_button_xpath())
        return BaseElement(
            driver=self.driver,
            locator=locator
        )