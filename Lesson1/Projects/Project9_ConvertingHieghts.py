# Converting heights

from time import sleep

while (True):
    HEIGHT = int(input("Please enter your height: "))
    sleep(1)
    UNIT = input("Please select the unit of measure: (f for feet / i for inches) ")
    sleep(1)
    if UNIT == ("f" or"F"):
        CENT = HEIGHT*30.48
        print("\nour height in centimeters is: ", CENT)
        break
    elif UNIT == ("i" or "I"):
        CENT = HEIGHT*2.54
        print("\nYour height in centimeters is: ", CENT)
        break
    else:
        print("\nYour choice is not valid. Please choose either f or i.")
        continue