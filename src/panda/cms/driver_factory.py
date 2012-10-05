'''
Created on 14.09.2012

@author: cbalea
'''
from selenium.webdriver.remote.webdriver import WebDriver


class DriverFactory(object):
    
    def initializeFirefoxDriver(self):
        seleniumHub = 'http://localhost:4444/wd/hub'
#        seleniumHub = 'http://ec2-204-236-220-204.compute-1.amazonaws.com:4445/wd/hub'
        desiredCapabilities = {"browserName":"firefox", "OS":"Linux"}
        browserProfile = None
        driver = WebDriver(seleniumHub, desiredCapabilities, browserProfile)
        return driver
    