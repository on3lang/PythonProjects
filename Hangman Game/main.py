
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

def main():
    print("")
    print(color.BOLD + color.PURPLE + "HANGMAN GAME" + color.END)
    print("")
    words = preparation()
    w = randomWord(words)
    

def preparation():
    # opening the file in read mode 
    my_file = open("words.txt", "r") 
    
    # reading the file 
    data = my_file.read() 
    
    # splitting by \n
    data_into_list = data.split("\n") 
    
    #close file
    my_file.close() 

    print(color.BOLD + "Ready!" + color.END)

    return data_into_list

def randomWord(l):
    i = randint(0, len(l))
    return l[i]

if __name__ == "__main__":
    main()