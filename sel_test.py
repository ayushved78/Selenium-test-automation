# IMPORT 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# driver = webdriver.Chrome()
'''
def launch_browser():
    driver = webdriver.Chrome()

    while(True):
        pass

    # driver.get('https://stackoverflow.com/questions/47508518/google-chrome-closes-immediately-after-being-launched-with-selenium')

launch_browser()
'''

# class automation:
def launch_browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.google.com/')
    input = driver.find_element_by_name('q').send_keys('Flutter')
    btn = driver.find_element_by_name('q').send_keys(Keys.ENTER)
    time.sleep(5)

    # NAVIGATION
    driver.back()
    time.sleep(2)
    driver.forward()

    

    # CLOSE BROWSER
    '''
    time.sleep(1)
    driver.quit()
    '''

    # return driver
    while(True):
        pass

    

# a = automation()
launch_browser()
