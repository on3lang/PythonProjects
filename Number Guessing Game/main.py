from random import randint

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

def main():
    print(color.BOLD + color.GREEN + "Welcome to the Number Guessing Game: " + color.END)
    navigator()
    
def navigator():
    print("")
    print("Please choose a difficulty level: ")
    print("1. Easy (0-10)")
    print("2. Medium (0-100)")
    print("3. Difficult (0-1000)")
    print("4. Exit")
    c = int(input("Choose: "))

    tries = 1

    match c:
        case 1:
            value = generateRandomNumberEasy()
            guessing(value, tries)
        case 2:
            value = generateRandomNumberMedium()
            guessing(value, tries)
        case 3:
            value = generateRandomNumberDifficult()
            guessing(value, tries)
        case 4:
            print("")
            print(color.BOLD + color.GREEN + "Exiting" + color.END)
        case _:
            print(color.BOLD + color.GREEN + "Please choose a value from the list!" + color.END)
            navigator()

def guessing(v, t):
    g = int(input("Try guessing the number: "))

    if g < v:
        print("")
        print(color.BOLD + color.GREEN + "Wrong! The secret number is GREATER than your try." + color.END)
        t += 1
        guessing(v, t)
    elif g > v:
        print("")
        print(color.BOLD + color.GREEN + "Wrong! The secret number is LOWER than your try." + color.END)
        t += 1
        guessing(v, t)
    elif g == v:
        print("")
        print(color.BOLD + color.GREEN + f"GUESSED! Nice Job! You did it in {t} tries" + color.END)
        navigator()

def generateRandomNumberEasy():
    value = randint(1,10)
    return value

def generateRandomNumberMedium():
    value = randint(1,100)
    return value

def generateRandomNumberDifficult():
    value = randint(1,1000)
    return value

if __name__ == "__main__":
    main()