import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("start-maximized")
driver = webdriver.Chrome(options=chrome_options)

ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"
GOOGLE_FORM = "https://docs.google.com/forms/d/e/1FAIpQLSdrY4aiwNQ9_5xwgBagTmTCO3FJdvRFFbtgjLcjklUsGO-itQ/viewform?usp=sf_link"
# cleaned_addresses = []
# cleaned_prices = []
# cleaned_links = []

response = requests.get(ZILLOW_URL)
soup = BeautifulSoup(response.text, "html.parser")
addresses = soup.find_all("address")
price_data = soup.find_all(attrs={"data-test": "property-card-price"})
link_data = soup.find_all(class_="property-card-link")
# for item in addresses:
#     new_item = item.getText().strip()
#     if "|" in new_item:
#         new_item = new_item.split("|")[1].strip()
#     cleaned_addresses.append(new_item)
cleaned_addresses = [address.getText().replace("|","").strip() for address in addresses]

# for item in price_data:
#     new_item = item.getText()
#     cleaned_item = new_item.split("+")[0].split("/")[0].replace("$", "").replace(",", "")
#     cleaned_prices.append(cleaned_item)
cleaned_prices = [price.getText().replace("$","").replace("/mo","").split("+")[0] for price in price_data]

# for item in link_data:
#     new_item = item.get("href")
#     cleaned_links.append(new_item)
cleaned_links = [link.get("href") for link in link_data]

for n in range(len(cleaned_addresses)):
    driver.get(GOOGLE_FORM)
    address_input = driver.find_element(By.XPATH,
                                        value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    time.sleep(2)
    address_input.send_keys(
        cleaned_addresses[n],
        Keys.TAB,
        cleaned_prices[n],
        Keys.TAB,
        cleaned_links[n],
        Keys.TAB,
        Keys.ENTER
    )

driver.quit()
