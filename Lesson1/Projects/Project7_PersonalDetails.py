# Printing my personal details on 3 different lines

from time import sleep

# Reading the details
NAME = input("What is your name? ")
sleep(1)
HOME = input("Where do you live? ")
sleep(1)
TELL = input("What is your phone number? ")
sleep(2)

# Printing the details on the screen
print("Hello ", NAME, "!")
sleep(1)
print("You live on ", HOME, ". Sounds like a nice place.")
sleep(1)
print("Your phone number is ", TELL)