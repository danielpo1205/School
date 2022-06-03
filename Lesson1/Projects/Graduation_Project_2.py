# This is a graduation project from the basic Python coding course. The program is a lottery game
# that allows the player to choose 6 numbers to compare and make earnings, until the user decides to quite the game
# - at which point the program will sum the total amount of winnings and inform the player of the amount he "earned".


from time import sleep
from random import randint


# Setting definitions
from typing import List


def choose_numbers(run1=0):
    sleep(2)
    print("\nBe ready to choose 6 numbers and prepare to type them in according to the sequence that will be presented shortly.")
    sleep(2)
    user_list = []
    while run1 < 6:
        chosen_num = (int(input("Please enter a number. \nThe number must be between 1 and 37:")))
        if chosen_num not in user_list:
                user_list.append(chosen_num)
        run1 += 1
    print("\nThe numbers you chose are:", user_list)
    sleep(3)

def roll_numbers(run2=0, run_num=0, total_prize=0, winnings=0, turns=0):
    sleep(3)
    print("Stand by, choosing random numbers....")
    lottery_list: list[str] = []
    while run2 < int(6):
        lottery_list = lottery_list.randint(1, 37)
        if run_num not in lottery_list:
            if lottery_list in user_list:
                lottery_list.append('+' + str(number))
                total_prize = total_prize + 1
                break
            run2 += 1
            turns += 1
    print("The numbers that were chosen randomly by the lottery program are:", lottery_list)
    sleep(2)
    if total_prize == 1:
        print("Sorry bro, no winnings this time.")
    elif total_prize == 2:
        print("Sorry bro, no winnings this time.")
    elif total_prize == 3:
        print("You've earned yourself 10 NIS!")
        winnings = winnings + 10
    elif total_prize == 4:
        print("You've earned yourself 100 NIS!")
        winnings = winnings + 100
    elif total_prize == 5:
        print("You've earned yourself 5000 NIS!")
        winnings = winnings + 5000
    elif total_prize == 6:
        print("You've won the GRAND PRIZE OF 1 MILLION NIS!!!")
        winnings = winnings + 1000000
    sleep(3)


# "Welcome" and input questions aimed at the user.
print("\nHi there!\nWelcome to the lottery game!")
sleep(2)
print("Each round costs 3 NIS.")
sleep(3)
print("\nIf you guess 6 numbers right - you win 1 million NIS.\nGuess 5 numbers, win 5000 NIS.\n4 numbers = 100 NIS.\n3 numbers = 10 NIS.")
sleep(3)
print("\nAre you ready to play?")
sleep(4)
BUDGET = int(input("\nHow much money are you willing to spend?"))
TURNS = BUDGET/3
TURNS = int(TURNS)
sleep(3)
print("Processing...")
sleep(4)
print("\nThe amount of", BUDGET, "NIS will allow you to play", int(TURNS), "turns.")
sleep(3)


# Set variables
TOTAL_PRIZE = 0
RANDOM = 0


# Main code
for i in range(TURNS):
    choose_numbers()
    roll_numbers()


# Finishing the game
sleep(3)
print("Your winnings are:", TOTAL_PRIZE)
sleep(3)
print("Thank you for playing!")