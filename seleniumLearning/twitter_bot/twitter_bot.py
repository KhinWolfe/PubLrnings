from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = "SOMENONSENSE"
TWITTER_EMAIL = "wolfekhin@gmail.com"
TWITTER_USERNAME = "WolfeKhin"
TWITTER_PASSWORD = "17UnseeingFountain^"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.chrome_options.add_argument("start-maximized")
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.up = ""
        self.down = ""

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/result/16122553412")
        self.driver.find_element(By.CLASS_NAME, value="start-text").click()
        time.sleep(50)
        self.down = self.driver.find_element(By.CSS_SELECTOR, value=".download-speed").text
        self.up = self.driver.find_element(By.CSS_SELECTOR, value=".upload-speed").text

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        time.sleep(2)
        email_input = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        email_input.send_keys(TWITTER_EMAIL)
        self.driver.find_element(By.XPATH , value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]').click()
        time.sleep(2)
        user_input = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        user_input.send_keys(TWITTER_USERNAME)
        self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div').click()
        time.sleep(2)
        pw_input = self.driver.find_element(By.NAME, value='password')
        pw_input.send_keys(TWITTER_PASSWORD)
        self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div').click()
        time.sleep(5)
        msg_input = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        msg_input.send_keys(f"My internet speed right now is {self.down}mbs down and {self.up}mbs up")
        self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]').click()
        time.sleep(2)
        self.driver.quit()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
time.sleep(5)
bot.tweet_at_provider()