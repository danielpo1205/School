# This is a graduation project from the basic Python coding course. The program is a lottery game
# that allows the player to choose 6 numbers to compare and make earnings, until the user decides to quite the game
# - at which point the program will sum the total amount of winnings and inform the player of the amount he "earned".

import random
from time import sleep


# Setting definitions
def game(chosen_num=0):
    sleep(2)
    print("\nBe ready to choose 6 numbers and prepare to type them in according to the sequence that will be presented shortly.")
    sleep(2)
    user_list = []
    user_list.clear()
    for num in range(0,6):
        chosen_num = (input("Please enter a number. \nThe number must be between 1 and 37:"))
        if chosen_num not in user_list:
                user_list.append(chosen_num)
        else:
            print("You have already chosen this number. Please choose a new one.")
    print("\nThe numbers you chose are:", user_list)
    sleep(3)
    lottery_list.clear()
    print("\nStand by, choosing random numbers....")
    for num in range(0,6):
        turn_num = random.randint(1, 37)
        lottery_list.append(turn_num)
        for lottery_num in lottery_list:
            for chosen_num in user_list:
                if chosen_num == lottery_num:
                    global correct_numbers
                    correct_numbers = correct_numbers + 1
                    break
    print("\nThe numbers that were chosen randomly by the lottery program are:", lottery_list)


# "Welcome" and input questions aimed at the user.
print("\nHi there!\nWelcome to the lottery game!")
sleep(2)
print("Each round costs 3 NIS.")
sleep(3)
print("\nIf you guess 6 numbers right - you win 1 million NIS.\nGuess 5 numbers, win 5000 NIS.\n4 numbers = 100 NIS.\n3 numbers = 10 NIS.")
sleep(3)
BUDGET = int(input("\nHow much money are you willing to spend?"))
TURNS = BUDGET/3
TURNS = int(TURNS)
sleep(3)
print("Processing...")
sleep(4)
print("\nThe amount of", BUDGET, "NIS will allow you to play", int(TURNS), "turns.")
sleep(3)


# Set variables
RANDOM = 0
TURNS = TURNS
winnings = 0
correct_numbers = 0


# Define a list
lottery_list = []


# Main code
for i in range(TURNS):
    game()


# Check the amount of prizes and finish the game
sleep(3)
print(f'You got {correct_numbers} correct numbers')
sleep(2)
if correct_numbers <= 2:
    print("Sorry bro, no winnings this time.")
elif correct_numbers == 3:
    print("You've earned yourself 10 NIS!")
    winnings = winnings + 10
elif correct_numbers == 4:
    print("You've earned yourself 100 NIS!")
    winnings = winnings + 100
elif correct_numbers == 5:
    print("You've earned yourself 5000 NIS!")
    winnings = winnings + 5000
elif correct_numbers >= 6:
    print("You've won the GRAND PRIZE OF 1 MILLION NIS!!!")
    winnings = winnings + 1000000
sleep(3)
print("Thank you for playing!")