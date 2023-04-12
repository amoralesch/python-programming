# Head and Tail Counter

import random

print("After a 100 throws of a coin, what will happen?")

tail = 0
head = 0
counter = 0

while counter < 100:
    counter += 1
    coin = random.randint(0, 1)

    if coin:
        tail += 1
    else:
        head += 1

print("Total number of tail is", tail)
print("Total number of head is", head)

input("\nPress the enter key to exit.")
