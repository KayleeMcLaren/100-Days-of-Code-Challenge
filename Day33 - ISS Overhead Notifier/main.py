
import requests
from datetime import datetime
import smtplib
import time

# CONSTANTS
MY_LAT = -33.924870  # Your latitude
MY_LONG = 18.424055  # Your longitude
MY_EMAIL = "myemail@gmail.com" # your email
PASSWORD = "mypassword" # your email account password

# is_iss_overhead
def is_iss_close():
    """Function to get the current position of the ISS and check if it is near the user's current position"""
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    data = response.json()

    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])

    # Check if your position is within +5 or -5 degrees of the ISS position
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True

# is_it_nightime
def is_it_nighttime():
    """Function to get the current time of day and check if it is currently nighttime"""
    parameters = {

        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) # Split to get the hour at sunrise 
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) # Split to get the hour at sunset 
    print(sunrise, sunset)

    time_now = datetime.now().hour # Get the hour of the current time

    if time_now >= sunset or time_now <= sunrise:
        return True

while True:  
"""While loop runs every 60 seconds to check if the ISS is close to the user and if it is nighttime and if so, 
it will send an email to tell the user to go outside and see the ISS overhead"""
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
            
