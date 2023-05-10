import requests
from bs4 import BeautifulSoup
import smtplib

MY_EMAIL = "qminh1908@gmail.com"
PASSWORD = "gvosjbtnqjvaauwq"
amazon_url = "https://www.amazon.com/gp/product/B09H1D7Y93/ref=ox_sc_act_title_3?smid=ATVPDKIKX0DER&psc=1"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 "
                  "Safari/537.36",
    "Accept-Language": "en-US,en;q=0.5"
}
response = requests.get(url=amazon_url, headers=headers)
amazon_web = response.text

soup = BeautifulSoup(amazon_web, "html.parser")
price_whole = soup.find(name="span", class_="a-price-whole")
price_fraction = soup.find(name="span", class_="a-price-fraction")
product_price = float(price_whole.getText() + price_fraction.getText())

product_id = soup.find(name="span", id="productTitle").getText().strip()

if product_price <= 230:
    with smtplib.SMTP(host="smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="minh.nq214010@sis.hust.edu.vn",
            msg=f"Subject: Get your fav item on Amazon now\n\n"
                f"The price of {product_id} has gone down to \"{product_price}\". Buy it now!!"
        )
