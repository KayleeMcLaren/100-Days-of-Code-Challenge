
import datetime as dt
import pandas
import random
import smtplib

my_email = "myemail@gmail.com"
password = "mypassword"

now = dt.datetime.now()
today_month = now.month
today_day = now.day
today_tuple = (today_month, today_day) # today's month and day

birthdays_df = pandas.read_csv("birthdays.csv") # read list of recipients and create a data frame

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in birthdays_df.iterrows()} # create a dictionary from "birthdays_df" data frame

"""Checks to see if today's date matches someone's birthday in the birthdays_dict. If so, it randomly picks one of the letter templates, replaces the placeholder [NAME] 
with the recipients actual name and sends them the letter to their email address."""
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"

    with open(file_path) as letter:
        birthday_msg = letter.read()
        birthday_msg = birthday_msg.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{birthday_msg}"
        )
        
