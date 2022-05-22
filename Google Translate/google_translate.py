from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def EngToTurk():
    eng = str(input("İngilizce Kelimenizi Giriniz: "))
    browser = webdriver.Chrome()
    browser.get("https://translate.google.com/?hl=tr&sl=en&tl=tr&op=translate")
    time.sleep(2)
    enter = browser.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea").send_keys(eng)
    time.sleep(2)
    for k in browser.find_elements_by_class_name("Q4iAWc"):
        print(f'{eng} = {k.text}')
    time.sleep(1)

def TurkToEng():
    turk = str(input("Türkçe Kelimenizi Giriniz: "))
    browser = webdriver.Chrome()
    browser.get("https://translate.google.com/?hl=tr&sl=tr&tl=en&op=translate")
    time.sleep(2)
    enter = browser.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea").send_keys(turk)
    time.sleep(2)
    for k in browser.find_elements_by_class_name("Q4iAWc"):
        print(f'{turk} = {k.text}')
    time.sleep(1)

while True:
    secim = str(input("1-İngilizce'den Türkçeye Çevirmek İçin '1' Tuşlayınız.\n2-Türkçeden İngilizce'ye Çevirmek İçin '2' Tuşlayınız.\n3-Çıkmak İçin 'q' veya 'Q' Tuşlayınız.\n"))
    if (secim == '1'):
        EngToTurk()
    elif (secim == '2'):
        TurkToEng()
    elif (secim == 'q' or secim == 'Q'):
        print("İşlem Sonlandırıldı.")
        break
    else:
        print("Yanlış Tuşa Basıldı.")