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
    print("1. Easy")
    print("2. Medium")
    print("3. Difficult")
    print("4. Exit")
    c = int(input("Choose: "))

    match c:
        case 1:
            v = generateRandomNumberEasy()
            print("value: "+ color.RED + f"{v}" + color.END)
            navigator()
        case 2:
            v = generateRandomNumberMedium()
            print("value: "+ color.RED + f"{v}" + color.END)
            navigator()
        case 3:
            v = generateRandomNumberDifficult()
            print("value: "+ color.RED + f"{v}" + color.END)
            navigator()
        case 4:
            print(color.BOLD + color.GREEN + "Exiting" + color.END)
        case _:
            print(color.BOLD + color.GREEN + "Please choose a value from the list!" + color.END)
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