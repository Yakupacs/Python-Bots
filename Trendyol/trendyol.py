from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

loop = 0
count = 0
productLink = input("Please enter product link: ")
commentNum = int(input("Please enter how many comments there are: "))
browser = webdriver.Chrome()
browser.get(productLink)
time.sleep(2)
browser.find_element_by_xpath("//*[@id='product-detail-app']/div/article[1]/div/div[2]/a/span").click()
time.sleep(2)
action = webdriver.ActionChains(browser)
loop = commentNum / 6

for i in range(int(loop)):
    browser.find_element_by_xpath("//*[@id='rating-and-review-app']").click()
    action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
    time.sleep(0.15)

time.sleep(2)
comments = browser.find_elements_by_class_name("rnr-com-tx")
time.sleep(2)
for i in comments:
    print(str(count) + "--> " + i.text)
    count += 1