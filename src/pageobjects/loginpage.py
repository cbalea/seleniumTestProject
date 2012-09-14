'''
Created on 14.09.2012

@author: cbalea
'''

from pageobjects import locators, selenium_server_connection
from pageobjects.basepageelement import BasePageElement
from pageobjects.basepageobject import BasePageObject
     
class UsernameElement(BasePageElement):
    def __init__(self):
        self.locator = locators["login.username"]

    def __set__(self, obj, val):
        se = selenium_server_connection.connection
        se.type(self.locator, val)
    
    
class PasswordElement(BasePageElement):
    def __init__(self):
        self.locator = locators["login.password"]

    def __set__(self, obj, val):
        se = selenium_server_connection.connection
        se.type(self.locator, val)


class LoginPageObject(BasePageObject):
    username = UsernameElement()
    password = PasswordElement()

    def __init__(self, se):
        self.se = se
        try:
            self.assertEqual("My Application - Login", self.se.get_title())
        except AssertionError:
            self.se.open("/login")
            self.se.wait_for_page_to_load("30000")
            self.assertEqual("My Application - Login", self.se.get_title())


    def submit(self):
        wait_for = "selenium.browserbot.getCurrentWindow().document.getElementById('LogoutButton')"
        self.se.click(locators["login.submit"])