# Guess My Number - Harder Edition
#
# The computer picks a random number between 1 and 100
# The player tries to guess it in less than 5 guesses,
# and the computer lets the player know if the guess
# is too high, too low or right on the money

import random

print("\tWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.\n")

# set the initial values
the_number = random.randint(1, 100)
guess = int(input("Take a guess: "))
tries = 1

# guessing loop
while guess != the_number and tries < 5:
    if guess > the_number:
        print("Lower ...")
    else:
        print("Higher ...")

    guess = int(input("Take a guess: "))
    tries += 1

if guess == the_number:
    print("You guessed it! The number was", the_number)
    print("And it only took you", tries, "tries!")
else:
    print("You failed, the number was", the_number)

input("\nPress the enter key to exit.")
