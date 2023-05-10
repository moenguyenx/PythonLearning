import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 21.042277
MY_LONG = 105.881341
MY_EMAIL = "qminh1908@gmail.com"
PASSWORD = "gvosjbtnqjvaauwq"


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    data = response.json()
    longitude = float(data['iss_position']['longitude'])
    latitude = float(data['iss_position']['latitude'])
    if 16 <= latitude <= 26 and 100 <= longitude <= 111:
        return True


def is_night_time():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    now = datetime.utcnow().hour
    if now >= sunset or now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_night_time() and is_iss_overhead():
        with smtplib.SMTP(host="smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs="minh.nq214010@sis.hust.edu.vn",
                                msg="Subject: Look up the sky!\n\nThe ISS is right above you, check it out!")
