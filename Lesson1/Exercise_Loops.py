## Practicing For loops
#
# fruit = ["apple","banana","cherry"]
# for X in fruit:
#     print(X)
#     print("wow")

# for x in "banana":
#     print(x)
#
# print("---------------")
#
# fruit1 = ["app",'ban','chair']
# for X in fruit1:
#     print(X)
#     if x=="ban":
#         break
#
# print("---------------")
#
# for x in range(10):
#     print(x)
#     print("wow")
#
# print("XXXXXXXXXXXXXXX")
#
# for X in range(5,10):
#     print(x)
#
# print("---------------")
#
# fruit2 = ["apple", "banana", "cherry"]
# for X in fruit2:
#     if x=="banana":
#         continue
#     print(X)
#
# for x in range(2,30,3):
#     print(x)

#############################
#
# list_dad=["banana","apple","mango"]
# for x in range(len(list_dad)):
#     print(list_dad[x])

###############################

from time import sleep
print("Now we will get all the names of your classmates. \n---------------------------------")
for i in range(4):
    NAME=input("Enter a student's name: ")
    AGE=str(input("Enter the student's age: "))
    PHONE=input("Enter the student's phone number: ")
    print("The student's number is: " +str(i+1) + ". \nHere are his details...\n")
    sleep(3)
    print("Name: " + NAME + "\nAge: " + str(AGE) + "\nPhone:" + PHONE + "\n--------------")

print("Bye bye")

#############################

