# Using and building modules

from time import sleep
from Lesson1.Lesson_Modules.defim import menu, calculating, dogs_age

menu()
sleep(3)
print("\nWow!\n")
sleep(2)
calculating(3,6)
sleep(2)
print("\nNext..")
sleep(2)
dogs_age(int(input("\nEnter dog's age: ")))