from selenium import webdriver
import pytest
import unittest
from manages.browserManages import get_browser
from pages.homePage import HomePage
from pages.landingPage import LandingPage
from data.data import UrlData, MailData, ValueData

@pytest.mark.usefixtures("driver_class")
class TestHomePage(unittest.TestCase):
    def setUp(self) :
        self.driver = get_browser(self.volta.browser)
        self.driver.get(UrlData.home_page_url())
        self.window_before = self.driver.window_handles[0]
        self.home = HomePage(self.driver)
        self.landing = LandingPage(self.driver)
                
    def tearDown(self):
        self.driver.quit()
        
    def test_about_us_button(self):
        self.landing.about_us_btn.is_existing()
        self.landing.about_us_btn.is_enable()
        self.assertTrue(self.landing.about_us_btn.text()=='About Us')
        print('Click About Us button')
        self.landing.about_us_btn.click()
        self.assertTrue(self.driver.current_url == UrlData.about_us_url())
        
    def test_contact_button(self):
        self.landing.contact_btn.is_existing()
        self.landing.contact_btn.is_enable()
        self.assertTrue(self.landing.contact_btn.text()=='Contact')
        print('Click Contact button')
        self.landing.contact_btn.click()
        self.assertTrue(self.driver.current_url == UrlData.contact_page_url())
        
    def test_email_input(self):
        self.home.input_email.is_existing()
        self.assertTrue(self.home.input_email.get_value() == ValueData.empty())
        self.home.input_email.enter_value(MailData.email())
        self.assertTrue(self.home.input_email.get_value() == MailData.email())
    
    def test_scroll_down_button(self):
        self.home.scroll_down_btn.is_existing()
        self.home.scroll_down_btn.is_enable()
        self.home.scroll_down_btn.click()
        self.home.comming_days.is_existing()