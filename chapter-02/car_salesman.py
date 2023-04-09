# Car Salesman
# Tells the the final price for a new car

msrp = int(input("What is the MSRP of the car? "))

tax = msrp * 0.088
lic = msrp * 0.05
dealer = 200
dest = 1000

print("\nBase price", msrp)
print(" Tax:", tax)
print(" License:", lic)
print(" Dealer prep:", dealer)
print(" Destination charge:", dest)
print("------------------")
print("Total:", str(msrp + tax + lic + dealer + dest))

input("\nPress the enter key to exit.")
