#Its name is pretty self-explanatory. Within this project, we will create
#a script that will have the ability to start a countdown timer for a
#certain amount of time. The user will first enter the number of seconds
#that the countdown should count, Once the amount is entered, the script
#will start the countdown and the script will wait for the entered amount
#of seconds to complete.

#It will work just like a countdown that you can find on your watch or
#smartphone.

#The code for the countdown timer is given below:
import time

#Main function to start the program
def main():
    print("Welcome to the Countdown Timer")

    #Ask the user for the time
    countdown2(int(input("Enter the time in seconds: ")))

#Function to start the countdown (Copilot)
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r") #Print on the same line
        time.sleep(1)
        t -= 1
    print("Fire in the hole!!")

#This is the function I would made :P
def countdown2(t):
    while t:
        print('{:02d}'.format(t), end="\r")
        time.sleep(1)
        t -=1
    print("Finished!")

#Function to start the countdown
if __name__ == "__main__":
    main()  # Call the main function