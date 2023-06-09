# Hero's Inventory 2
# Demonstrates tuple

# create a tuple with some items and displays with a for loop
inventory = ("sword", "armor", "shield", "healing potion")
print("Your items:")
for item in inventory:
    print(item)

input("\nPress the enter key to continue.")

# get the length of a tuple
print("You have", len(inventory), "items in your possesion.")

input("\nPress the enter key to continue.")

# test for membership with in
if "healing potion" in inventory:
    print("You will live to fight another day.")

# display one item whrough an index
index = int(input("\nEnter the index number for an item in inventory: "))
print("At index", index, "is", inventory[index])

# display a slice
start = int(input("\nEnter the index number to begin a slice: "))
finish = int(input("Enter the index number to end the slice: "))
print("inventory[", start, ":", finish, "] is", inventory[start:finish])

input("\nPress the enter key to continue.")

# concatenate two tuples
chest = ("gold", "gems")
print("You find a chest. It contains:")
print(chest)

print("You add the contents of the chest to you inventory.")
inventory += chest
print("Your inventory is now:")
print(inventory)

input("\nPress the enter key to exit.")
