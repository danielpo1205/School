# Refer to the program's Readme file for description.

from time import sleep
from Lesson1.FinalLab.defim import *
from os import path
from Lesson1.FinalLab.defim import dns_dict

# A welcome message greeting the user.
print("\nWelcome!")
sleep(2)
print("\nPlease wait while the program boots up...")
sleep(3)

''' # Checking in a specific directory if a database file already exists . If not, the program will create a new storage
file for the IP list. '''
print("\nSearching for an IP database.")
f = path.exists("C:/Users/danie/Documents/לימודים/אבטחת סייבר/Python/IP_database.txt")
sleep(3)
if not f:
    f = open("C:/Users/danie/Documents/לימודים/אבטחת סייבר/Python/IP_database.txt", "x")
    f.close()
    print("\nDatabase created.")
    sleep(2)
elif f:
    print("Database found. Please wait for the menu to show up on the screen.")
    sleep(3)

# Running the main code.
while (True):
    menu()

    # Allowing the user to terminate the program.
    sleep(2)
    EXIT = input("\nWould you like to stop? yes/no ")
    if EXIT == "yes" or EXIT == "y" or EXIT == "Y":
        break
    else:
        continue

sleep(2)
print("\nThank you for using our program!")
