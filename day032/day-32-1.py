import smtplib
import datetime as dt
import random

MY_EMAIL = "raja.mookala450@gmail.com"
MY_PASSWORD = "dhakshil@18"
now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
  with open("quotes.txt") as quote_file:
    all_quotes = quote_file.readlines()
    quote = random.choice(all_quotes)
  print(quote)
  with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)
    connection.sendmail(from_adrs=MY_EMAIL,to_addrs=MY_EMAIL, msg=f"Subject:Monday motivation\n\n{quote}")








#import smtplib

#my_email = "raja.mookala450@gmail.com"
#password = "******"

#connection = smtplib.SMTP("smtp.gmail.com")
##connection.starttls()
#connection.login(user=my_email, password=password)
#connection.sendmail(from_addrs=my_email, to_addrs="my_mail", msg="hello")
#connection.colse()






#import datetime as dt

#now = dt.datetime.now()
#year = now.year
#month = now.month
#day_of_the_week = now.weekday()
#print(day_of_the_week)

#date_of_birth = dt.datetime(year=2000, month=5, day=5)
#print(date_of_birth)