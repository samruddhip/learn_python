import random

target = random.randint(1, 100)

# print("Random number between 1 and 100 is: ", randNum)

while True:
    userChoice = input("Guess the target or Q for quiet:")
    if(userChoice == 'Q'):
        print("You have chosen to quit the game.")
        break
    userChoice = int(userChoice)
    if(userChoice == target):
        print("Congratulations! You guessed the correct number.")
        break
    elif(userChoice > target):
        print("Your guess is greater than the target number.")
    else:
        print("Your guess is less than the target number.") 
