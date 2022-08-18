from selenium import webdriver
import json
import time, random
from selenium.webdriver.common.keys import Keys
import pandas as pd

data = pd.read_csv("tedhena.csv")
data_dict = data.to_dict('list')
emri = data_dict['emer']
password = data_dict['password']
tedhena_list = zip(emri,password)

data = pd.read_csv("userlist.csv")
data_dict = data.to_dict('list')
user = data_dict['user']
user_list = zip(user,)

index = 0
browser=webdriver.Chrome("C:\chromedriver.exe")

for emer,Password in tedhena_list:
        browser.get("https://www.instagram.com/")
        time.sleep(5)

        #Login
        login=browser.find_element_by_css_selector("#loginForm > div > div:nth-child(1) > div > label > input")
        login.send_keys(emer)
        time.sleep(2)

        #Password
        password=browser.find_element_by_css_selector("#loginForm > div > div:nth-child(2) > div > label > input")
        password.send_keys(Password)
        password.submit()
        print(" --- U logua me sukses ["+ emer + "]")
        time.sleep(5)

        #Notnow
        notnow=browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
        notnow.click()
        time.sleep(10)

        #Notification
        noti=browser.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm")
        noti.click()
        time.sleep(10)

        #message
        browser.get("https://www.instagram.com/p/CXmI16PKjCi/")
        time.sleep(5)
        for user1 in user_list:
            browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[1]/span[3]/button").click()
            time.sleep(5)
            share_post = browser.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div.qF0y9.Igw0E.IwRSH.eGOV_.vwCYk.i0EQd > div.TGYkm > div > div.HeuYH > input")
            share_post.send_keys(user1)
            time.sleep(5)
            send = browser.find_element_by_xpath("/html/body/div[6]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/div").click()
            time.sleep(7)
            browser.find_element_by_xpath("/html/body/div[6]/div/div/div[2]/div[4]/button").click()
            time.sleep(7)
            print(f'--- Mesazhi u cu me sukses te {user1}')
            index += 1
            if index == 10 or index == 20 or index == 30 or index == 40 or index == 50 or index == 60 or index == 70 or index == 80 or index == 90 or index == 100 or index == 110 or index == 120 or index == 130 or index == 140 or index == 150 or index == 160 or index == 170 or index == 180 or index == 190 or index == 200 or index == 210 or index == 220 or index == 230 or index == 240 or index == 250:
                browser.close()
                break
