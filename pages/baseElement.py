from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.common.exceptions import NoSuchElementException
from collections import namedtuple

Locator = namedtuple('Locator', ['by', 'value'])

class BaseElement(object):
    timeout = 20
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        
    def find(self):
        element = Wait(self.driver, self.timeout).until(EC.presence_of_element_located(locator=self.locator))
        return element
        
    def click(self):
        element = Wait(self.driver, self.timeout).until(EC.element_to_be_clickable(self.locator))
        element.click()
        return None
    
    def enter_value(self, value):
        self.find().send_keys(value)
        
    def find_all(self):
        elements = Wait(self.driver, self.timeout).until(EC.presence_of_all_elements_located(locator=self.locator))
        for element in elements:
            print(element)
            
    def text(self):
        text = self.find().text
        return text
    
    def is_enable(self):
        if self.find().is_enabled():
            print(" ==> Element is enable")
            return True
        else:
            print(" ==> Element is not enable")
            return False
        
    def is_existing(self):
        try:
            self.find()
            print('Element is existing')
        except NoSuchElementException as error:
            print(error)
            
    def get_placeholder(self):
        placeholder = self.find().get_attribute("placeholder")
        print("Placeholder: ",placeholder)
        
    def get_value(self):
        value = self.find().get_attribute("value")
        print("Value: ",value)
        return value
        
    def is_radio_button(self):
        if self.find().get_attribute("type") == "radio":
            print(" ==> It is a Radio button")
            return True
        else:
            print(" ==> It is not a Radio button")
            return False
        
    def is_button_checked(self):
        if self.find().get_attribute("checked") == "true":
            print(" ==> Button is Selected")
            return True
        else:
            print(" ==> Button is Not Selected")
            return False
        
    def is_checkbox(self):
        if self.find().get_attribute("type") == "checkbox":
            print(" ==> It is a Checkbox button")
            return True
        else:
            print(" ==> It is not a Checkbox button")
            return False
    
    def is_checkbox_selected(self):
        if self.find().is_selected():
            print(" ==> Check clicked to deselected")
            return True
        else:
            print(" ==> Checkbox is not selected")
            return False