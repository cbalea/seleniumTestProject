'''
Created on 11.09.2012

@author: cbalea
'''
from selenium import webdriver
import os
import unittest

class TestEnvironmentalVariable(unittest.TestCase):
    
    def test_env_var(self):
        try:
            url = "http://api-%s.pbslm.org/" %os.environ["ENVIRONMENT"]
            driver = webdriver.Firefox()
            driver.get(url)
            driver.get_screenshot_as_file("/tmp/env_var.png")
        except KeyError: 
            print "Variable not received" 
