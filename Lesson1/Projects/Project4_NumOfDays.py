#Calculating the number of days between two given dates

from datetime import date
from time import sleep

f_date = date(2020, 5, 10)
l_date = date(2020, 5, 20)
delta = l_date - f_date
sleep(2)
print("Calculating...")
sleep(2)
print("The number of days between both dates is: ", delta.days)