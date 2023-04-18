# Guess My Word
#
# The computer picks a random word and then asks the player to guess it
# It tells the player how many letters it has, and then allows the player
# to ask 4 times if a letter is part of the word

import random

WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")

word = random.choice(WORDS)

print("I'm thinking of a word, try to guess it!")
print("My word has", len(word), "letters")

for i in range(5):
    letter = input("Which letter do you want to test? ")

    if letter in word:
        print("Yes, that letter is in my word.")
    else:
        print("No, that letter is in NOT my word.")

guess = input("What word am I thinking? ")

if guess == word:
    print("Correct! You are very smart!")
else:
    print("Nope, you did not guess my word. It was", word)

print("Thanks for playing.")

input("\nPress the enter key to exit.")
