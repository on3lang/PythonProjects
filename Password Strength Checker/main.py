#Whenever you create an account on a site by entering your username and
#password, the site ensures that the password you are trying to save is
#strong, so that hackers cannot guess your passwords easily.

#In this project, we are gonna mimic the site, functionality into a
#console-based python project, This script will check the strength of the
#password that the user will enter. The script will show the number of
#alphabets, numbers, special characters, and whitespace characters
#present within the password and will accordingly mark the password’s
#strength.

#The best password will be the one containing at least one uppercase
#letter, one lowercase letter, one digit, one special character, and one
#whitespace. So it’s time you change your Gmail password.

#special characters
special_characters = "!@#$%^&*()-+?_=,<>/"

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

#Main Function
def main():
    password = input("Enter a password: ")
    checker(password)

def checker(p):
    checking = {
        'digit' : False,
        'lower' : False,
        'upper' : False,
        'whitespace' : False,
        'special' : False
    }
    
    for c in p:
        if not(checking['digit']): 
            if c.isdigit():
                checking['digit'] = True
        if not(checking['lower']):
            if c.islower():
                checking['lower'] = True
        if not(checking['upper']):
            if c.isupper():
                checking['upper'] = True
        if not(checking['whitespace']):
            if c == " ":
                checking['whitespace'] = True
        if not(checking['special']):
            if c in special_characters:
                checking['special'] = True

    for check in checking.keys():
        if checking[check]:
            print(color.BOLD + "{}: ".format(check) + color.GREEN + "OK" + color.END)
        else:
            print(color.BOLD + "{}: ".format(check) + color.RED + "X" + color.END)
            
    

#Start application main
if __name__ == "__main__":
    main() #Start main