from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.get("https://10fastfingers.com/advanced-typing-test/turkish")
time.sleep(3)
while True:
    try:
        kelime = browser.find_element_by_class_name("highlight").text
        browser.find_element_by_xpath("//*[@id='inputfield']").send_keys(kelime)
        browser.find_element_by_xpath("//*[@id='inputfield']").send_keys(Keys.SPACE)
        time.sleep(0.05)
    except:
        break