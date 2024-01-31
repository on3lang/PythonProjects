from random import seed
from random import randint

def main():
    print(f"Ho tirato il dado ed è uscito {RollD6()}")

def RollD6():
    value = randint(1, 6)
    return value

if __name__ == "__main__":
    main()