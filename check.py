import time
from selenium import webdriver
import random
from datetime import datetime, time


def check():
    try:
        driver.find_element_by_xpath('//*[@id="username"]')
    except:
        return False
    else:
        return True

DAY_START = time(8, 00)
DAY_END = time(12, 00)

NIGHT_START = time(20, 30)
NIGHT_END = time(22, 00)

while 1:
    current_time = datetime.now().time()

    if (DAY_START <= current_time <= DAY_END) or (NIGHT_START <= current_time <= NIGHT_END):
        driver = webdriver.Chrome()
        driver.get("https://ehall.jlu.edu.cn/infoplus/form/72423623/render")
        time.sleep(random.randint(5,10))
        if(check()):
            driver.find_element_by_xpath('//*[@id="username"]').send_keys('liangyz2019')
            time.sleep(random.randint(5,10))
            driver.find_element_by_xpath('//*[@id="password"]').send_keys('Liangyz0526')
            time.sleep(random.randint(5,10))
        article = driver.find_element_by_xpath('//*[@id="login-submit"]')
        article.click()
        time.sleep(random.randint(10,20))
        js = "document.getElementsByClassName('command_button_content')[0].click();"
        time.sleep(random.randint(1,2))
        driver.execute_script(js)
        time.sleep(random.randint(10,20))
        js = "document.getElementsByClassName('dialog_button')[0].click();"
        time.sleep(random.randint(5,10))
        driver.execute_script(js)
        time.sleep(random.randint(5,10))
        driver.close()