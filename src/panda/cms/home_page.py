'''
Created on 18.09.2012

@author: cbalea
'''
from selenium.webdriver.remote.webelement import WebElement

class HomePage(object):
    usernameField = WebElement(None, None)
    passwordField = WebElement(None, None)
    usernameId = "id_username"
    passwordId = "id_password"
    
    def __init__(self, driver):
        driver.get("http://api-qa.pbslm.org/admin/")
        self.usernameField = driver.find_element_by_id(self.usernameId)
        self.passwordField = driver.find_element_by_id(self.passwordId)
        
    def typeUsername(self, username):
        self.usernameField.send_keys(username)
        
    def typePassword(self, password):
        self.passwordField.send_keys(password)
        
    def submitForm(self):
        self.usernameField.submit()
    
    def login(self, username, password):
        self.typeUsername(username)
        self.typePassword(password)
        self.submitForm()