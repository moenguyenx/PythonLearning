from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_drive_path = "D:\Personal Projects\ChromeDriver\chromedriver.exe"

driver = webdriver.Chrome(service=Service(chrome_drive_path))
driver.get("https://web.archive.org/web/20220120120408/https://secure-retreat-92358.herokuapp.com/")
# article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("dmdm")

last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("ahaha")

email = driver.find_element(By.NAME, "email")
email.send_keys("ahihi@ohiihi.com")

sign_up = driver.find_element(By.CSS_SELECTOR, "Button")
sign_up.click()

driver.quit()
