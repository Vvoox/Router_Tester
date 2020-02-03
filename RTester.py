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

url = "http://192.168.1.1/"
# Message = "Sbah lkher 3ameto , Jomo3a mobaraka <3"
print("Sending...to ")
chrome_options = Options()
chrome_options.add_argument("user-data-dir=./User_Data2")
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')
#chrome_options.add_argument('--disable-dev-shm-usage')
display = Display(visible=0, size=(800, 800))
display.start()
webdriver1= webdriver.Chrome(options=chrome_options)
# self.driver.minimize_window()
webdriver1.get(url)
print("Open the url is done ...")
sleep(50)

def send_message(username):

    webdriver1.find_element_by_xpath("//input[contains(@class, '_2zCfw copyable-text selectable-text')]") \
        .send_keys(username)
    sleep(1)
    webdriver1.find_element_by_xpath("//input[contains(@class, '_2zCfw copyable-text selectable-text')]") \
            .send_keys(Keys.ENTER)

    webdriver1.find_element_by_xpath("//div[contains(@class, '_3u328 copyable-text selectable-text')]") \
            .send_keys(Message)
    sleep(1)
    webdriver1.find_element_by_xpath("//div[contains(@class, '_3u328 copyable-text selectable-text')]") \
            .send_keys(Keys.ENTER)
    sleep(20)
    print("Your message was sent")
    sleep(5)
    if(username=="Aunt Happiness"):
        webdriver1.quit()

send_message("painful")


