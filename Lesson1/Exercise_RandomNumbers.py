## Practicing random numbers

from random import randint
from time import sleep
#print(randint(1,37))
print("Welcome to the lottery game!\n")

sleep(3)

print("Choosing random numbers....")
num1=randint(1,37)
num2=randint(1,37)
sleep(2)
print("\nThe 1st number is: " + str(num1) + "\nThe 2nd number is: " + str(num2))
sleep(2)
if (num1==num2):
    print("You won 100$\n")
else:
    print("You lost\n")

sleep(2)
print("Bye bye\n")