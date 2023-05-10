from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

chrome_drive_path = "D:\Personal Projects\ChromeDriver\chromedriver.exe"
USER_NAME = "moenguyenx"
PASSWORD = "sonya7iv"


class InstaFollower:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(service=Service(driver_path))

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        sleep(5)
        user_name = self.driver.find_element(
            By.XPATH,
            '//*[@id="loginForm"]/div/div[1]/div/label/input'
        )
        user_name.send_keys(USER_NAME)
        password = self.driver.find_element(
            By.XPATH,
            '//*[@id="loginForm"]/div/div[2]/div/label/input'
        )
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)

    def find_follower(self):
        self.driver.get("https://www.instagram.com/moenguyenx/")
        sleep(5)
        followers = self.driver.find_element(
            By.XPATH,
            '//*[@id="mount_0_0_H+"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a/span/span'
        ).text
        following = self.driver.find_element(
            By.XPATH,
            '//*[@id="mount_0_0_H+"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[3]/a/span/span'
        ).text
        print(f"{USER_NAME} has {followers} followers and following {following}")


bot = InstaFollower(chrome_drive_path)
bot.login()
bot.find_follower()
