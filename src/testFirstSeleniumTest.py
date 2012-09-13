'''
Created on 11.09.2012

@author: cbalea
'''
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
import unittest

class FirstTest(unittest.TestCase):
    
    def googlePage(self):
#        seleniumHub = 'http://localhost:4444/wd/hub'
        seleniumHub = 'http://ec2-204-236-220-204.compute-1.amazonaws.com:4445/wd/hub'
        desiredCapabilities = {"browserName":"firefox"}
        browserProfile = None
        driver = WebDriver(seleniumHub, desiredCapabilities, browserProfile)
        
        print "Running test on hub: %s" %seleniumHub
        
        # go to the google home page
        driver.get("http://www.google.com")
    
        # find the element that's name attribute is q (the google search box)
        inputElement = driver.find_element_by_name("q")
        
        # type in the search
        inputElement.send_keys("Cheese!")
        
        # submit the form (although google automatically searches now without submitting)
        inputElement.submit()
        
        # the page is ajaxy so the title is originally this:
        print driver.title
        
        try:
            # we have to wait for the page to refresh, the last thing that seems to be updated is the title
            WebDriverWait(driver, 10).until(lambda driver : driver.title.lower().startswith("cheese!"))
        
            # You should see "cheese! - Google Search"
            print driver.title
            self.assertEquals(driver.title.index("cheese"), 0, "The expected page was not found!")
        
        finally:
            driver.quit()
    
    def test_1(self):
        self.googlePage()
    
    def test_2(self):
        self.googlePage()
        
    def test_3(self):
        self.googlePage()
    
    def test_4(self):
        self.googlePage()
    
    def test_6(self):
        seleniumHub = 'http://ec2-204-236-220-204.compute-1.amazonaws.com:4445/wd/hub'
        desiredCapabilities = {"browserName":"firefox"}
        browserProfile = None
        driver = WebDriver(seleniumHub, desiredCapabilities, browserProfile)
        
        print "Running test on hub: %s" %seleniumHub
        
        # go to the google home page
        driver.get("http://www.google.com")
    
        # find the element that's name attribute is q (the google search box)
        inputElement = driver.find_element_by_name("q")
        
        # type in the search
        inputElement.send_keys("Cheese!")
        
        # submit the form (although google automatically searches now without submitting)
        inputElement.submit()
        
        # the page is ajaxy so the title is originally this:
        print driver.title
        
        try:
            # we have to wait for the page to refresh, the last thing that seems to be updated is the title
            WebDriverWait(driver, 10).until(lambda driver : driver.title.lower().startswith("cheese!"))
        
            # You should see "cheese! - Google Search"
            print driver.title
            self.assertEquals(driver.title.index("aaa"), 0, "The expected page was not found!")
        
        finally:
            driver.quit()
    
    def test_5(self):
        self.googlePage()