# A program to calculate the sum of a shopping cart at the grocery store, including 17 percent VAT.

print("Enter the weight \ amount of each item in your cart: ")

# Program suspension for 2 seconds
import time
time.sleep(2)

# User input of quantity
tomato = int(input("Tomato: "))
cucumber = int(input("Cucumber: "))
cola = int(input("Coca cola: "))
chicken = int(input("Chicken: "))

time.sleep(2)
print("\nHere is a summary of your order:\nTomatos (Kg): " + str(tomato) + "\nCucumbers (Kg): " + str(cucumber) + "\nCoca cola (bottles): " + str(cola) + "\nChicken (Kg): " + str(chicken))

# Calculation
a=((tomato) * 3) + ((cucumber) * 2) + ((cola) * 5) + ((chicken) * 20)

# Program suspension for 2 seconds
time.sleep(2)

# Printing the result
time.sleep(1)
print("\nThe total sum before VAT is: " + str(a) + " NIS" )
print("\nThe total amount to pay including VAT is:" + str("%.2f" % (a*1.17)) + " NIS" )
time.sleep(1)
print("\nThank you for using our program!")
