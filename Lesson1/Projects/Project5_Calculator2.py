# Calculating the sum of 3 given numbers.

from time import sleep

print("Hello and welcome.\n")
sleep(1)
N1 = int(input("What is the 1st number? "))
sleep(1)
N2 = int(input("What is the 2nd number? "))
sleep(1)
N3 = int(input("What is the 3rd number? "))
if (N1 != N2 or N2 != N3):
    SUM = N1+N2+N3
    sleep(2)
    print("\nThe result is: ", SUM)

# If the given numbers are equal, the script will return  three times of their sum
elif N1 == N2 and N2 == N3:
    SUM = (N1*3)*3
    sleep(2)
    print("\nThe 3 numbers are equal. The result is: ", SUM)