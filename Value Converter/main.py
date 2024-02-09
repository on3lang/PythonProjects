import numpy as np

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
    print(color.BOLD + color.BLUE + "Welcome to the Value Converter" + color.END)
    startConverter()

def startConverter():
    print("")
    print("1. C to F")
    print("2. F to C")
    print("3. EUR to USD")
    print("4. USD to EUR")
    print("5. Radius to circumference")
    print("6. Exit")
    print("")
    c = int(input("Please choose an option: "))

    match c:
        case 1:
            print("")
            CtoF(int(input("Enter a temperature in Celsius: ")))
            startConverter()
        case 2:
            print("")
            FtoC(int(input("Enter a temperature in Fahrenheit: ")))
            startConverter()
        case 3:
            print("")
            EURtoUSD(int(input("Enter an amount in EUR: ")))
            startConverter()
        case 4:
            print("")
            USDtoEUR(int(input("Enter an amount in USD: ")))
            startConverter()
        case 5:
            print("")
            calcCircunference(int(input("Enter a radius: ")))
            startConverter()
        case 6:
            print("")
            print(color.GREEN + "Exiting" + color.END)
        case _:
            print("")
            print(color.BOLD + color.GREEN + "Please choose a value from the list!" + color.END)
            startConverter()

def CtoF(c):
    f = (c * 9/5) + 32
    print(color.GREEN + f"{c}C is {f}F" + color.END)

def FtoC(f):
    c = (f - 32) * 5/9
    print(color.GREEN + f"{f}F is {c}C" + color.END)

def EURtoUSD(e):
    u = e * 1.13
    print(color.GREEN + f"{e}EUR is {u}USD" + color.END)

def USDtoEUR(u):
    e = u / 1.13
    print(color.GREEN + f"{u}USD is {e}EUR" + color.END)

def calcCircunference(r):
    c = r * np.pi
    print(color.GREEN + f"Given the radius {r}, the circuference is {c}" + color.END)

if __name__ == "__main__":
    main()