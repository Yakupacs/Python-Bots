from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from userinfo import username, password
import time

try:
    allLikes = []
    likeList = []
    filePath = 100
    browser = webdriver.Chrome()
    def Login(username, password):
        browser.get("https://www.instagram.com")
        time.sleep(3)
        usernameInput = browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
        passwordInput = browser.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")
        usernameInput.send_keys(username)
        passwordInput.send_keys(password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(5)

    def LetsGo(url, filePath):
        browser.get(url)
        time.sleep(2)

        browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[2]/div/div/div/a/div/span").click()
        input("If you can see the list of likes, press a button")
        time.sleep(1)

        action = webdriver.ActionChains(browser)
        browser.find_element_by_xpath("/html/body/div[6]/div/div/div[2]/div").click()
        action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
        time.sleep(1)

        begenenlerinSayisi = len(browser.find_elements_by_class_name("_7UhW9.xLCgt.qyrsm.KV-D4.se6yk.T0kll"))
        begenenler = browser.find_elements_by_class_name("_7UhW9.xLCgt.qyrsm.KV-D4.se6yk.T0kll")
        for begeni in begenenler:
            likeList.append(begeni.text)   
        time.sleep(0.5)

        while True: 
            browser.find_element_by_xpath("/html/body/div[6]/div/div/div[2]/div").click()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()        
            browser.find_element_by_xpath("/html/body/div[6]/div/div/div[2]/div").click()   
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()                           
            time.sleep(0.5) 

            newSayi = len(browser.find_elements_by_class_name("_7UhW9.xLCgt.qyrsm.KV-D4.se6yk.T0kll"))
            if begenenlerinSayisi == newSayi:
                begenenlerinSayisi = newSayi
                begenenler = browser.find_elements_by_class_name("_7UhW9.xLCgt.qyrsm.KV-D4.se6yk.T0kll")
                for begeni in begenenler:
                    likeList.append(begeni.text)    
                time.sleep(0.5)

            else:
                break
        begenenler = browser.find_elements_by_class_name("_7UhW9.xLCgt.qyrsm.KV-D4.se6yk.T0kll")
        for begeni in begenenler:
            likeList.append(begeni.text)   
        time.sleep(0.5)

        for x in likeList:
            if x not in allLikes:
                allLikes.append(x)

        print(f'Likers number: {len(allLikes)}')
        i = 0
        for k in allLikes:
            i += 1
            print(str(i) + " -> " + k)

        allLikes.sort()
        with open(filePath + "_.txt", "w", encoding="UTF-8") as file:
            for item in allLikes:
                file.write(item + "\n")

        print("------------SUCCESFULLY---------------")

    Login(username, password)

    while True:
        print("Press the 'q', if you want quit.")
        url = input("Post URL: ")
        time.sleep(1)    
        if (url == 'q'):
            break
        else:
            filePath = str(filePath)
            LetsGo(url, filePath)
            filePath = int(filePath)
            
        filePath += 1

    print("-------------------FINISH.-----------------")

except:
    print("-----------ERROR---------------------")