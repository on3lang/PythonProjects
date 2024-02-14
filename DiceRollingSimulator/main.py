""" This project is, again, an easy one, but at the same time, a very
crucial one as it will introduce beginner python programmers to the
random library. Random library is used to generate pseudo-random
results. We call its output pseudo-random as the output we get is not
100% random, but still is, pretty much random.

This script will ask the user whether to roll the dice or exit the game.
If the user chooses to roll the dice, the script will use the random
module, to get a random number between 1 and 6 and display it to the
user. If the user chooses to exit, the program will simply exit. """

from random import seed
from random import randint

#Color class to make the output more readable
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

#Main function to start the program
def main():
    InitRollingSimulator()

#Function to roll a D4
def RollD4():
    value = randint(1, 4)
    print("")
    print(color.BOLD + "The Dice result is " +color.RED + f"{value}" + color.END)

#Function to roll a D6
def RollD6():
    value = randint(1, 6)
    print("")
    print(color.BOLD + "The Dice result is " +color.RED + f"{value}" + color.END)

#Function to roll a D8
def RollD8():
    value = randint(1, 8)
    print("")
    print(color.BOLD + "The Dice result is " +color.RED + f"{value}" + color.END)

#Function to roll a D10
def RollD10():
    value = randint(1, 10)
    print("")
    print(color.BOLD + "The Dice result is " +color.RED + f"{value}" + color.END)

#Function to roll a D12
def RollD12():
    value = randint(1, 12)
    print("")
    print(color.BOLD + "The Dice result is " +color.RED + f"{value}" + color.END)

#Function to roll a D20
def RollD20():
    value = randint(1, 20)
    print("")
    print(color.BOLD + "The Dice result is " +color.RED + f"{value}" + color.END)

#Function to start the rolling simulator
def InitRollingSimulator():
    print("")
    print(color.BOLD + color.GREEN + "Choose one option below:" + color.END)
    print("1. Roll a D4     4. Roll a D10")
    print("2. Roll a D6     5. Roll a D12")
    print("3. Roll a D8     6. Roll a D20")
    print("0. Exit")
    c = int(input("Insert the number of action you want to do: "))

    match c:
        case 1:
            RollD4()
            InitRollingSimulator()
        case 2:
            RollD6()
            InitRollingSimulator()
        case 3:
            RollD8()
            InitRollingSimulator()
        case 4:
            RollD10()
            InitRollingSimulator()
        case 5:
            RollD12()
            InitRollingSimulator()
        case 6:
            RollD20()
            InitRollingSimulator()
        case 0:
            print("")
            print(color.BOLD + color.GREEN + "Exiting" + color.END)
            print("")
        case _:
            print("")
            print(color.BOLD + "Please choose a value from the list!" + color.END)
            InitRollingSimulator()

#Call the main function
if __name__ == "__main__":
    main()