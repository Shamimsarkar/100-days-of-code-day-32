import random
import pandas as pd
import datetime as dt
from smtplib import SMTP

my_email = "rezamdshamim034@gmail.com"
my_password = "odli hfeg oopt ejzl"

now = dt.datetime.now()
today_tuple = (now.month, now.day)

data = pd.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthday_dict:
    person = birthday_dict[today_tuple]

    with open(file=f"letter_templates/letter_{random.randint(1,3)}.txt") as letter_file:
        letter_contains = letter_file.read()
        new_letter = letter_contains.replace("[NAME]", person["name"])

    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=person["email"],
            msg=f"Subject: Birthday Message\n\n{new_letter}"
        )





