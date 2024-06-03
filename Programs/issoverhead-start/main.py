import requests
import smtplib
import time
from datetime import datetime

MY_EMAIL = "testing.email.python.001@gmail.com"
MY_PASSWORD = "mfrhizehvitkdgex"

MY_LAT = 50.066998 # Your latitude
MY_LONG = 20.014294 # Your longitude

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if iss_latitude - 5 <= MY_LAT <= iss_latitude + 5:
        if iss_longitude - 5 <= MY_LONG <= iss_longitude + 5:
            return True

def is_night():
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

    time_now = datetime.now().hour

    if time_now in range(sunset, sunrise):
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.google.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject:Look up!\n\nLook up! There's an ISS over your head"
            )