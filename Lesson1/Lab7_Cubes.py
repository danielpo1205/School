''' Lab7- Cube project
נקבל כקלט כמה כסף יש לנו לשחק
עלות משחק 3 ש"ח
אם יש עודף נחזיר אותו ללקוח
בכל תור נגריל 2 קוביות , אם הן זהות זכינו ב- 100 ש"ח, אם הן זהות אבל שוות גם ל-6, זכינו ב- 1000 ש"ח
אם הן לא זהות, אבל קוביה 2 שווה ל-2 זכינו ב- 40 ש"ח
אם הן לא זהות אבל קוביה 1 שווה ל-1 זכינו ב- 20 ש"ח
לבסוף נדפיס למסך בכמה כסף זכינו
לציין כמה עודף נשאר להחזיר ללקוח
'''
###########

from time import sleep
from random import randint

# Welcome and instructions
print("\nWelcome to the Dice Gambling Game!")
sleep(2)
print('''\nPlease read the instructions carefully:\n 
1. Each gambling turn costs 3 NIS. 
2. Change will be returned to you. 
3. In every turn we will digitally role 2 dices. If the numbers on them are identical - you will win 100 NIS. If both dices present 6 - you win 1000 NIS. 
   If the dices aren't identical but one of them presents 2 - you win 40 NIS and if the one presents 1 - you win 10 NIS.''')
sleep(4)
print("\nHere we go... GOOD LUCK!")
sleep(3)

# Calculating the number of turns, according to the amount of money the user wants to spend
MONEY=int(input("How much money do you want to spend? "))
TURNS=int(MONEY/3)
sleep(3)
print("The amount of money you entered is: ", (MONEY))
sleep(3)
print("\nWorking...")
sleep(3)
print("\nThe number of turns you are entitled to is: ", str(int(TURNS)), " turns.")
sleep(4)
print("Your change is: ", str(MONEY % 3), " NIS")
sleep(4)
print("\n\nReady to gamble?")
sleep(2)

# Rolling the dices
WINNINGS = 0
for i in range(TURNS):

    sleep(2)
    print("\n\nRound number: ", str(i+1), "\n----------------------")

    DICE1 = randint(1, 6)
    DICE2 = randint(1, 6)

    sleep(2)
    print("Rolling dices...")
    sleep(5)
    print("The first dice shows: ", DICE1)
    sleep(2)
    print("The second dice shows:", DICE2)
    sleep(4)

    if (DICE1==DICE2):
        print("CONGRATULATIONS! You win 100 NIS!")
        WINNINGS = WINNINGS+100

    elif (DICE1==DICE2 and DICE1==6):
        print("CONGRATULATIONS! You win the JACKPOT - 1000 NIS!")
        WINNINGS = WINNINGS+1000

    elif (DICE1!=DICE2 and DICE2==2):
        print("You win 40 NIS.")
        WINNINGS = WINNINGS+40

    elif (DICE1!=DICE2 and DICE1==1):
        print("You win 10 NIS.")
        WINNINGS = WINNINGS+10

    else:
        print("Sorry, you did not win this time.")

# Chashing out
sleep(3)
print("\nCalculating your winnings...")
sleep(3)
print("\nYour winnings total: " + str(WINNINGS) + " NIS.")
sleep(3)
print("\nThank you for playing with us. Hope to see you again soon!")