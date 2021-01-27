# Computing the sum of two given numbers. If the sum is between 15-20 it will return 20

N1 = int(input("Please type the first number: "))
N2 = int(input("Please type the second number: "))

if (N1+N2) in range(15, 20):
    print("The sum is 20!")
else:
    print("The sum is: ", int(N1+N2))