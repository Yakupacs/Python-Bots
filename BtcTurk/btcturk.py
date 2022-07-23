from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.get("https://pro.btcturk.com/pro/al-sat/BTC_TRY")
time.sleep(3)
price = 0

while True:
    lastPrice = browser.find_element_by_id("ex-advanced-ticker-last").text
    highPrice = browser.find_element_by_id("ex-advanced-ticker-high").text
    lowPrice = browser.find_element_by_id("ex-advanced-ticker-low").text
    if (lastPrice != price):
        print(f'\nBITCOIN\nPrice: {lastPrice}\nHigh Price: {highPrice} TRY\nLow Price: {lowPrice} TRY\n')        
        price = browser.find_element_by_id("ex-advanced-ticker-last").text
    time.sleep(1)