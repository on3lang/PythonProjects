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

def main():
    InitRollingSimulator()

def RollD6():
    value = randint(1, 6)
    print("")
    print(f"Ho tirato il dado ed è uscito {value}")

def InitRollingSimulator():
    print("")
    print("Choose one option below:")
    print("1. Roll a D6")
    print("6. Exit")
    c = int(input("Insert the number of action you want to do: "))

    match c:
        case 1:
            RollD6()
            InitRollingSimulator()
        case 6:
            print("")
            print("Exiting")
        case _:
            print("")
            print("Please choose a value from the list!")
            InitRollingSimulator()

if __name__ == "__main__":
    main()