from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#set up driver for chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("start-maximized")
driver = webdriver.Chrome(options=chrome_options)
#set up driver to open page
driver.get("https://en.wikipedia.org/wiki/Main_Page")
#get driver to search an ID with #
article_count = driver.find_element(By.CSS_SELECTOR, value='#articlecount a')
print(article_count.text)

#can click on a link
#article_count.click()

#find element by link text, use that search to click into link
all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
#all_portals.click()

#find the "Search" <input> by Name
search = driver.find_element(By.NAME, value="search")

#sending keyboard input to Selenium
#search.send_keys("Python", Keys.ENTER)



#driver.quit()#closes all tabs