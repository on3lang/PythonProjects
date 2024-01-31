#The calculator is probably one of the most common project ideas that you will see in many youtube videos. And the reason for this is that it is
#very easy to make and it will clear your basic concepts regarding
#if-else statements and while loop.

#The calculator will start by asking what the user wants to do, like:

#Addition

#Subtraction

#Multiplication

#Division, and

#Exit

#Based on the option, the script will either add, subtract, multiply or
#divide the numbers that the user entered. Once the operation is
#complete, the script will again ask the user its choice. If the user
#chooses to exit, the program will stop.

def main():
    selectOperation()

def addition(n, m):
    return n+m

def subtraction(n, m):
    return n-m

def multiplication(n, m):
    return n*m

def division(n, m):
    return n/m

def selectOperation():
    print("Choose the operation you want to do: ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    c = int(input("Input the number of the operation: "))

    match c:
        case 1:
            n = int(input("Insert the first number: "))
            m = int(input("Insert the second number: "))
            result = addition(n, m)
            print(f"{n} + {m} = {result}")
            selectOperation()
        case 2:
            n = int(input("Insert the first number: "))
            m = int(input("Insert the second number: "))
            result = subtraction(n, m)
            print(f"{n} - {m} = {result}")
            selectOperation()
        case 3:
            n = int(input("Insert the first number: "))
            m = int(input("Insert the second number: "))
            result = multiplication(n, m)
            print(f"{n} * {m} = {result}")
            selectOperation()
        case 4:
            n = int(input("Insert the first number: "))
            m = int(input("Insert the second number: "))
            result = division(n, m)
            print(f"{n} / {m} = {result}")
            selectOperation()
        case 5:
            print("Exit")
        case _:
            print("Please insert a value in the list!")
            selectOperation()

if __name__ == "__main__":
    main()