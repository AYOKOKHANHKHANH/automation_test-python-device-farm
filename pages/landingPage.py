from selenium.webdriver.common.by import By
from .baseElement import BaseElement, Locator
from locators.landingPageLocator import *

class LandingPage:
    def __init__(self, driver):
        self.driver = driver
        
    @property
    def about_us_btn(self):
        locator = Locator(by=By.XPATH, value=get_about_us_button_xpath())
        return BaseElement(
            driver=self.driver,
            locator=locator
        )
        
    @property
    def home_btn(self):
        locator = Locator(by=By.XPATH,value=get_home_button_xpath())
        return BaseElement(
            driver=self.driver,
            locator=locator
        )
        
    @property
    def contact_btn(self):
        locator = Locator(by=By.XPATH, value=get_contact_button_xpath())
        return BaseElement(
            driver=self.driver,
            locator=locator
        )