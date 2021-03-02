#add birthday details in birthdays.csv
#it has example data. Do fill it with your own details
#to automate the running of the code everyday use https://www.pythonanywhere.com
#add main.py and birthdays.csv in files section and create a new directory with the name letter templates and
# add the three letter text files in therm.
#after adding the files and directory, go to tasks and create a new one. add the command- python3 main.py - and set
#time of the day you want to run it daily.

import pandas
import smtplib
import datetime as dt
import random

my_mail = "srishtik01233@gmail.com"
password = "Sanxywrubryh9vevdy"
connection = smtplib.SMTP("smtp.gmail.com", 587)

birthday_df = pandas.read_csv("birthdays.csv")
birthday_list = birthday_df.to_dict(orient="records")

random_letter = f"letter_{random.randint(1,3)}.txt"
today = (dt.datetime.today().day, dt.datetime.today().month)

def birthday_wisher():
    for dict in birthday_list:
        if (dict["day"], dict["month"]) == today:
            name = dict["name"]
            email = dict["email"]
            with open(f"letter_templates/{random_letter}") as letter:
                contents = letter.read()
                contents = contents.replace('[NAME]', f"{name}")

            connection.starttls()
            connection.login(user=my_mail, password=password)
            connection.sendmail(from_addr=my_mail, to_addrs=f"{email}",
                                msg=f"Subject:Happy Birthday!!\n\n{contents}")
            connection.close()

birthday_wisher()


