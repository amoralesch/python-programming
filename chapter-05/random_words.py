# Random Words
# Print words in random order without repeating

import random

WORDS = ["one", "two", "three", "four", "five", "six", "seven"]
size = len(WORDS)

print("The original list is:")
print(WORDS)

WORDS.sort(key=lambda _: random.randint(0, size))

print("The list randomly sorted is:")
print(WORDS)

input("\nPress the enter key to exit.")
