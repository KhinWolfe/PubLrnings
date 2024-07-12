from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#set up driver for chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("start-maximized")
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://secure-retreat-92358.herokuapp.com/")
fname_input = driver.find_element(By.NAME, value="fName")
fname_input.send_keys("Name1",
                      Keys.TAB,
                      "Name2",
                      Keys.TAB,
                      "email1@dunworry.com",
                      Keys.TAB,
                      Keys.ENTER
                      )
# lname_input = driver.find_element(By.NAME, value="lName")
# email_input = driver.find_element(By.NAME, value="email")
# sign_up_btn = driver.find_element(By.CSS_SELECTOR, value="form button")
# sign_up_btn.click()