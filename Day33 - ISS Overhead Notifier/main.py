
import requests
from datetime import datetime
import smtplib
import time

MY_LAT = -33.924870  # Your latitude
MY_LONG = 18.424055  # Your longitude
MY_EMAIL = "myemail@gmail.com" # your email
PASSWORD = "mypassword" # your email account password


def is_iss_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    data = response.json()

    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])

    # Your position is within +5 or -5 degrees of the ISS position
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


def is_it_nighttime():
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
    print(sunrise, sunset)

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_close() and is_it_nighttime():
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=["recipientemail@yahoo.com"],
                msg=f"Subject:ISS Overhead!\n\nGo outside and look up!"
            )
            
