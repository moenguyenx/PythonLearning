from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
import smtplib

PROMISED_DOWN = 100
PROMISED_UP = 100
MY_EMAIL = "qminh1908@gmail.com"
PASSWORD = "gvosjbtnqjvaauwq"
chrome_drive_path = "D:\Personal Projects\ChromeDriver\chromedriver.exe"


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.test_button = None
        self.driver = webdriver.Chrome(service=Service(driver_path))
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        sleep(2)
        self.test_button = self.driver.find_element(
            By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a'
        )
        self.test_button.click()
        sleep(40)
        self.down = self.driver.find_element(
            By.XPATH,
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span'
        ).text
        self.up = self.driver.find_element(
            By.XPATH,
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span'
        ).text

    def send_email(self):
        if float(self.up) < PROMISED_UP and float(self.down) < PROMISED_DOWN:
            with smtplib.SMTP(host="smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs="minh.nq214010@sis.hust.edu.vn",
                    msg=f"Subject: HUST Internet speed report\n\n"
                        f"Download speed is: {self.down} and Upload speed is: {self.up}\n"
                        f"Which is suck according to the speed which school advertised!!"
                )


bot = InternetSpeedTwitterBot(chrome_drive_path)
bot.get_internet_speed()
bot.send_email()
