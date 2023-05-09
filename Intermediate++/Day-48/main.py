from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "D:\Personal Projects\ChromeDriver\chromedriver.exe"

driver = webdriver.Chrome(service=Service(chrome_driver_path))

driver.get("https://www.python.org/")
price = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(price.text)
