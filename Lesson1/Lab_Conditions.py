## A lab on "Python Conditions" - writing a code that will allow the user to choose an option from a menu and execute it

from time import sleep

# Welcome message

print("\nWelcome to our program.")

# Building a menu
sleep(2)
print("\nPlease choose from one of the following options:\n")

sleep(2)

MENU = input (str ("1. Enter a number and display its calculation to the power of 3. \n" + "2. Enter and store 4 IP addresses and show them. \n" + "3. Add 4 entries to the DNS list and show them. \n" + "4. Check if a string is a Palindrome. \n"))

sleep(2)

# Executing the user's request using the "if" and "elif" conditions and implementing indentation.

# Calculating a number entered by the user to the power of 3 and printing the result on the screen
if( MENU == str("1") ):
    a=int(input("You chose the first option. Please type a number to calculate: "))
    print("The number you provided in the power of 3 is: " + str(a**3))

# Allowing the user to type in 4 IP addresses, storing them in a new list and then printing it
elif ( MENU == str("2") ):
    IP_list = []
    IP_list.append(input("You have chosen the 2nd option. Please enter the first IP address: "))
    IP_list.append(input("Please enter the second IP Address: "))
    IP_list.append(input("Please enter the third IP address: "))
    IP_list.append(input("Please enter the fourth IP Address: "))
    print("\nThe IP addresses are: " + str(IP_list))

# Creating a DNS dictionary and adding 4 entries, then printing it
elif ( MENU == str("3") ):
    DNS_dict = {}
    DNS_dict.update({input("\nPlease enter URL no. 1: "): input("Please enter the IP address: ")})
    DNS_dict.update({input("\nPlease enter URL no. 2: "): input("Please enter the IP address: ")})
    DNS_dict.update({input("\nPlease enter URL no. 3: "): input("Please enter the IP address: ")})
    DNS_dict.update({input("\nPlease enter URL no. 4: "): input("Please enter the IP address: ")})
    print("\nThe DNS entries were successfully stored as follows: ")
    print(DNS_dict)

# Checking if a string entered by the user is a Palindrome
elif ( MENU == str("4") ):
    WORD1 = input("\nPlease type a word to check if it is a Palindrome: ")
    sleep(2)
    print("The word you typed - reversed, is: " + (WORD1 [::-1]))
    if (WORD1 [::-1] == WORD1):
        print("\nThe word you have entered indeed is a Palindrome.")
    else:
        print("\nUnfortunately the word you have entered is NOT a Palindrome.")

# Alerting the user of choosing an invalid option
else:
    print("The option you chose is not Valid. Please choose an option from 1 to 4.")

# Exiting the Program
sleep(2)
print("\nThank you for using our program!")
