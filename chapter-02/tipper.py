# Tipper
# Tells the user the bill total including tips

bill = int(input("How much was the bill? "))

tip1 = bill * 0.15
tip2 = bill * 0.20

option1 = bill + tip1
option2 = bill + tip2

tip1 = str(tip1)
tip2 = str(tip2)

print("\nIf you tip 15% (" + tip1 + ") the total will be", option1)
print("If you tip 20% (" + tip2 + ") the total will be", option2)

input("\nPress the enter key to exit.")
