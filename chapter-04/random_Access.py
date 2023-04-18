# Random Access
# Demonstrates string indexing

import random

word = "index"
print("The word is:", word, "\n")

high = len(word)
low = -high

for i in range(10):
    position = random.randrange(low, high)
    print("word[", position, "]\t", word[position])

input("\nPress the enter key to exit.")
