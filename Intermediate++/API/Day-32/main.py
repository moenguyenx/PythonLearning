import smtplib
import datetime as dt
import random

now = dt.datetime.now()

MY_EMAIL = "qminh1908@gmail.com"
PASSWORD = "gvosjbtnqjvaauwq"

with open("quotes.txt", "r") as data:
    motivation_quotes = data.readlines()

with smtplib.SMTP(host="smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=PASSWORD)
    if now.weekday() == 0:
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="minh.nq214010@sis.hust.edu.vn",
                            msg=f"Subject: Monday Motivation\n\n {random.choice(motivation_quotes)} ")


