from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_drive_path = "D:\Personal Projects\ChromeDriver\chromedriver.exe"

driver = webdriver.Chrome(service=Service(chrome_drive_path))
driver.get("https://en.wikipedia.org/wiki/Main_Page")
article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
print(article_count.text)
