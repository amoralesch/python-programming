# Fortune Cookie

import random

print("What would the fortune have for you in store?")

choice = random.randint(1, 5)

if choice == 1:
    print("You will live a happy life.")
elif choice == 2:
    print("Life can be difficult sometimes.")
elif choice == 3:
    print("No-one can know the future!")
elif choice == 4:
    print("Prepare yourself for a nice surprise.")
else:
    print("You will die (just like everyone else).")

input("\nPress the enter key to exit.")
