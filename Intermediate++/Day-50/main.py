from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

chrome_drive_path = "D:\Personal Projects\ChromeDriver\chromedriver.exe"

driver = webdriver.Chrome(service=Service(chrome_drive_path))

driver.get("https://tinder.com/")
attempts = 0
sleep(2)
log_in_button = driver.find_element(By.XPATH, '//*[@id="c24809439"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
log_in_button.click()

sleep(2)
log_in_fb = driver.find_element(By.XPATH, '//*[@id="c-1703571637"]/main/div/div/div[1]/div/div/div[3]/span/div[2]/button')
log_in_fb.click()
sleep(60)

while attempts < 100:
    like_button = driver.find_element(
        By.XPATH, "//*[@id='c24809439']/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button")
    like_button.click()
    sleep(3)
    attempts += 1
