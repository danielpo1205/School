##Exercising Conditions during the lesson

# if("idan"=="idan"):
#     print("Correct")
# else:
#     print("Not good")
#
# print("-------------")
#
# NAME=input("Enter a name: ")
# if(NAME=="daniel"):
#     print("Welcome back Daniel!\n")
#     AGE = input("How old are you? ")
#     if (AGE == "23"):
#         print("Wow, you are 23 years old\n")
#     else:
#         print("You are too young...\n")
# else:
#     print("You aren't from around here, ha?\n")

#####################################
#
# number=int(input("Enter a number: \n"))
# if(number>6):
#     print(number*2)
# else:
#     print(number-1)

#####################################

NAME=input("Enter your name: \n")
AGE=int(input("How old are you? \n"))
if((NAME=="idan" or NAME=="Idan") and (AGE>=18)):
    print("You are welcome to enter the club!")
else:
    print("You are not allowed to enter. Please leave the premises...")