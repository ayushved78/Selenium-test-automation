from pip import main
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def run():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.amazon.in/')
    time.sleep(2)
    # btn = driver.find_element_by_id('nav_cs_mobiles').click()
    select = driver.find_element_by_link_text('Mobiles').click()
    time.sleep(5)
    src = driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']").send_keys('iPhone')
    time.sleep(2)
    btn = driver.find_element_by_xpath("//input[@id='nav-search-submit-button']").click()
    time.sleep(5)
    list = driver.find_elements_by_xpath("//span[@class='a-size-medium a-color-base a-text-normal']")
    print(str(len(list)) + ' products found.' + 'Here\'s the list of items:')

    for i in list:
        print(i.text)

    driver.quit()
    while(True):
        pass
    return False
    

if __name__ == '__main__':
    run()