from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.get("https://www.binance.com/tr/trade/SAND_USDT?layout=pro&theme=dark&type=spot")
time.sleep(1)

while True:
    instant = browser.find_elements_by_class_name("showPrice")[0].text
    highest =  browser.find_elements_by_class_name("tickerPriceText")[1].text
    lowest = browser.find_elements_by_class_name("tickerPriceText")[2].text    
    print(f'SAND\nInstant Price: {instant}\n24h High: {highest}\n24h Low: {lowest}')
    time.sleep(5)
    print("-------------------------------------------")