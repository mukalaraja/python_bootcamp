##################### Normal Starting Project ######################
from datetime import datetime
import pandas
import random
import smtplib

my_email = "mahesh@gmail.com"
password = "rambabu12"
# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Create a tuple from today's month and day using datetime. e.g.
today = datetime.now()
today_tuple = (today.month, today.day)
# HINT 2: Use pandas to read the birthdays.csv
data = pandas.read_csv("birthdays.csv")
# HINT 3: Use dictionary comprehension to create a dictionary from birthday.csv that is formated like this:
#Dictionary comprehension template for pandas DataFrame looks like this:
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
  birthday_person = birthdays_dict[today_tuple]
  file_path = f"letters/letter_{random.randint(1,3)}.txt"
  with open(file_path) as letter_file:
    contents = letter_file.read()
    contents = contents.replace("[NAME]", birthday_person["name"])

  with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(my_email, password)
    connection.sendmail(from_addrs=my_email, to_addrs=birthday_person["email"], msg=f"subject:Happy Birthday!!\n\n{contents}")



