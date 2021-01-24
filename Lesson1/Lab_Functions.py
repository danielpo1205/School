# A code practicing the use of functions.

from time import sleep
from math import factorial

# def menu():

def dog_det():
    DNAME = input("\nWhat is the dog's name? ")
    sleep(1)
    DAGE = int(input("How old is the dog? (in dogs years) "))
    DHAGE = (DAGE * 7)
    sleep(3)
    print("\nYour dog's name is: ", str(DNAME), "and his age is equal to a human age of ", int(DHAGE), " years.")


def friends():
    FRIEND = input("\nPlease enter your friend's name :")
    sleep(3)
    if FRIEND in FRIEND_LIST:
        print("%s is found in the list of friends." %(FRIEND))
    else:
        print("%s was not found in the friends list and was now added." %(FRIEND))
        FRIEND_LIST.append(FRIEND)


# The main code
while(True):
    CHOICE = int(input('''
    Please choose an option from the following menu:
    1. Storing the details of your dog.
    2. Making a list of friends.
    3. Running a factorial number.\n'''))

    sleep(2)
    print("\nWorking...")
    sleep(3)

    if (CHOICE == 1):
        sleep(2)
        print("\nYou chose the first option on the menu. Stand by to enter the dog's name: ")
        sleep(2)
        dog_det()
        sleep(2)

    elif (CHOICE == 2):
        sleep(2)
        print("\nYou chose the second option. You will be asked to enter  your friends names momentarily.")
        sleep(2)
        FRIEND_LIST = []
        for i in range(5):
            friends()
        sleep(2)

    elif (CHOICE == 3):
        sleep(2)
        FACT = int(input("\nPlease type a number to compute it's factorial: "))
        sleep(3)
        print("The factorial of ", FACT, " is: ", factorial(FACT))

# Allowing the user to terminate the program
    sleep(2)
    EXIT=input("\nWould you like to stop? yes/no ")
    if (EXIT=="yes" or EXIT=="y"):
        break
    else:
        continue

print("BYE!")
