# This is a graduation project from the basic Python coding course. The program checks your marketing budget
# with the cost of a campaign on Facebook or Instagram and will tell you if either is within your budget or how
# much you have to add to meet the cost.

from time import sleep

# Welcome and input questions aimed at the user.
print("\nWelcome.\nPlease read our disclaimer very carefully, which is... nothing.")
sleep(2)
print("Please note that a Facebook campaign costs 100 NIS per day and an Instagram campaign costs 50 NIS per day.\n")
sleep(4)
BUDGET = int(input("What is your marketing budget?"))
sleep(3)
FCAMPAIGN = int(input("How many days would you like the campaign to run on Facebook?"))
sleep(4)
print("\nProcessing...\n")
sleep(4)
ICAMPAIGN = int(input("Now, how many days would you like the campaign to run on Instagram?"))
sleep(3)
print("\nPlease wait while we run a few calculations...\n")
sleep(4)

#Calculating the values received from the user
vat = 1.17
F_COST = FCAMPAIGN * 100
I_COST = ICAMPAIGN * 50
TOTAL_COST = F_COST + I_COST
T_COST_VAT = TOTAL_COST * vat
DIFFERENCE = T_COST_VAT - BUDGET

#Printing the results to the screen
print("The total cost of your campaign including 17% VAT is:",  T_COST_VAT, "NIS." )
sleep(4)

if (T_COST_VAT == BUDGET) or (T_COST_VAT < BUDGET):
    print("Successful!")
else:
    print("\nYour budget doesn't cover the campaign's cost. \nYou must add:", DIFFERENCE, "NIS.")

sleep(4)
print("\nThank you for using our program! :-)")
