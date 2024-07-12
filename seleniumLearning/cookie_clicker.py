from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#set up driver for chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("start-maximized")
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.CSS_SELECTOR, value="#cookie")
store_data = driver.find_elements(By.CSS_SELECTOR, value="#store div")
store_IDs = [item.get_attribute("id") for item in store_data]
money = ""
timeout = time.time() + 5
game_over = time.time() + (60*5)

def buy_stuff():
    global money
    global store_IDs
    money = int(driver.find_element(By.ID, value="money").text.replace(",",""))
    price_list = []
    store = []
    prices = driver.find_elements(By.CSS_SELECTOR, value="#store b")
    for item in prices:
        if item.text != "":
            add = int(item.text.split("-")[1].replace(",",""))
            price_list.append(add)
    for n in range(len(price_list), 0, -1):
        print(n)
        if money > price_list[n-1]:
            driver.find_element(By.ID, value=store_IDs[n-1]).click()
            print("did a thing")
            break


while True:
    cookie.click()
    if time.time() >= timeout:
        timeout += 5
        buy_stuff()
    if time.time() >= game_over:
        break
