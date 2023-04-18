# Word Jumble - Harder version
#
# The computer picks a random word and then "jumbles" it
# The player has to guess the original word
# Gives prize if player guesses it in one try
# Provides hint if player is stuck

import random

WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")
HINTS = ("snake", "this game", "facil", "opposite of easy", "given to a question", "musical instrument")

i = random.randint(0, len(WORDS))
word = WORDS[i]
hint = HINTS[i]

first_try = True
correct = word

# create a jumbled version of the word
jumble = ""

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

# start the game
print(
    """
        Welcome to Word Jumble!

    Unscramble the letters to make a word.
    (Press the enter key at the prompt to quit.)
    """
)
print("The jumble is:", jumble)

tries = 1
guess = input("\nYour guess: ")
while guess and guess != correct:
    print("Sorry, that's not it.")
    first_try = False

    if tries >= 3:
        print("Small hint:", hint)

    tries += 1
    guess = input("Your guess: ")

if guess == correct:
    print("That's it! You guessed it!\n")

    if first_try:
        print("And you did it on your first try! You are smart!")

print("Thanks for playing.")

input("\nPress the enter key to exit.")
