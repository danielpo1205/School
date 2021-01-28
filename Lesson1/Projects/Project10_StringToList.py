# Coverting a byte string to a list of integers

from time import sleep

A = input("Please type in your phone number: ")
A = A.encode('ASCII')
sleep(2)
print("Phone number was encoded.")
sleep(2)
B = A.decode('ASCII')
print("Phone number was decoded.")
sleep(2)
DECO_list = list(B)
print(DECO_list)
