# Practicing "while loops" - printing Fibonacci numbers.
#
# from time import sleep
#
# while(True):
#     # Asking the user for the number of terms
#     NTERMS=int(input("How many terms to run? "))
#
#     # Seting the variables
#     N1, N2 = 0, 1
#     COUNT=0
#     sleep(2)
#
#     # Popping an error message for an input of 0
#     if NTERMS <= 0:
#         print("Please enter a positive number.")
#         sleep(2)
#         continue
#
#     print("\nWorking...")
#     sleep(4)
#
#     # Printing the Fibonacci sequence
#     print("\nFibonacci sequence:")
#     while COUNT < NTERMS:
#         print(N1)
#
#         # Updating the variables
#         NXTHP = N1 + N2
#         N1=N2
#         N2=NXTHP
#         COUNT+=1
#
# print("\nBye bye!")

#############################

# Another sample for a Fibonacci sequence

# fibo=[1,2,3,5,8,13,21]
#
# boolean="True"
# for i in range(2,len(fibo)):
#     print(fibo[i])
#     print(fibo[i-1])
#     print(fibo[i-2])
#     print("\n")
#     if fibo[i]==(fibo[i-1]+fibo[i-2]):
#         continue
#     else:
#         boolean="False"
#         break
#
# if boolean=="True":
#     print("It is a fibo series")
# else:
#     print("It isn't a fibo series")

##############################

# Writing a code that will print a menu and run 3 options related to numbers
from time import sleep
from random import randint

# Building a menu
while(True):
    CHOISE=int(input('''\n
    Please choose an option from the following menu:
    -------------
    1. Print 100 numbers to the screen.
    2. Creat a list and check if it is equal to a Fibonacci sequence.
    3. The program will choose random numbers until it reaches 12 or drafts 10 numbers.\n'''))

# Running the chosen command
    if (CHOISE==1):
        print("\nYou chose option 1. Printing the numbers: ")
        sleep(3)
        for i in range(1,101):
            print(i)
        print("\nDone.")

    elif (CHOISE==2):
        print("You chose option 2. Creating a list.")
        fibo=[]
        for i in range(8):
            fibo.append(input("Pleas enter a number:"))
        boolean = "True"
        for i in range(2,len(fibo)):
            print(fibo[i])
            print(fibo[i-1])
            print(fibo[i-2])
            print("\n")
            if fibo[i]==(fibo[i-1]+fibo[i-2]):
                continue
            else:
                boolean="False"
                break

        if boolean=="True":
            print("It is a Fibonacci sequence.")
        else:
            print("It isn't a Fibonacci sequence.")

    elif (CHOISE==3):
        print("You chose option 3. Drafting numbers...:")
        for i in range(10):
            DRAFT = randint(1,12)
            if (DRAFT<=12):
                print("The drafted number is: ", DRAFT," in round ", i, ".")
            else:
                print("Drafted a number greater then 12 or maxed out 10 turns.", "The drafted number is: ", DRAFT," in round ", i, ".")
                break
# Alerting the user about an invalid option
    else:
        print("\nOption not valid. Please choose between 1 and 3.")
        sleep(2)
        continue

# Allowing the user to terminate the program
    EXIT=input("\nWould you like to stop? yes/no ")
    if (EXIT=="yes" or EXIT=="y"):
         break
    else:
         continue

print("\nBye bye")