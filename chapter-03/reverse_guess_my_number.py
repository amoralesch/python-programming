# Reverase Guess My Number
#
# The player picks a random number between 1 and 100
# The computer tries to guess it and the players lets
# the computer know if the guess is too high, too low
# or right on the money

import random

print("\tWelcome to 'Guess Your Number'!")
print("\nPlease think of a number between 1 and 100.")
print("Tell me if my guess was `high`, `low`, or `correct`.\n")

# set the initial values
min = 1
max = 100
tries = 1
guess = (min + max) // 2

while True:
    print("My guess is", guess)
    correct = input("Is it correct? ")

    if correct == "high":
        max = guess
    elif correct == "low":
        min = guess
    elif correct == "correct":
        break
    else:
        print("Please answer `high`, `low`, or `correct`")
        continue

    tries += 1
    guess = (min + max) // 2

print("I guessed it! The number was", guess)
print("And it only took me", tries, "tries!")

input("\nPress the enter key to exit.")
