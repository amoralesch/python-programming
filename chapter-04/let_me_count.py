# Let Me Count
# Count using info from the user

start = int(input("Where should I start? "))
finish = int(input("Where should I finish? "))
step = int(input("How long should I increase each time? "))

number = start
while number < finish:
    print(number)

    number += step

input("\nPress the enter key to exit.")
