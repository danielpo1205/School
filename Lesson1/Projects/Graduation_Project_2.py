# This is a graduation project from the basic Python coding course. The program is a lottery game
# that allows the player to choose 6 numbers to compare and make earnings, until the user decides to quite the game
# - at which point the program will sum the total amount of winnings and inform the player of the amount he "earned".


from time import sleep
from random import randint


# Setting definitions
def choose_numbers(run=0):
    sleep(2)
    print("\nBe ready to choose 6 numbers and prepare to type them in according to the sequence that will be presented shortly.")
    sleep(2)
    #UserList = UserList.append[int(input("Please enter the first number. \nThe number must be between 1 and 37:"))]
    UserList = []
    while run < 6:
        chosen_num = (int(input("Please enter a number. \nThe number must be between 1 and 37:")))
        if chosen_num not in UserList:
                UserList.append(chosen_num)
        run += 1
    print("\nThe numbers you chose are:", UserList)
    sleep(3)

def roll_numbers():
    sleep(3)
    print("Stand by, choosing random numbers....")
    RandList, run = [], 0
    number = 0
    while run < 6:
        number = number.randint(str(1, 37))
        if number not in RandList:
            if run == 6:
                RandList.append('+' + str(number))
                TOTAL_PRIZE = TOTAL_PRIZE + 1
                break
            run += 1
            TURNS += 1
    print(RandList)
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