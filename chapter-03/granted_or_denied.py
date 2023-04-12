# Granted or Denied
# Demonstrates an else clause

print("Welcome to System Security Inc.")
print("-- where security is our middle name\n")

password = input("Enter your password: ")

if password == "secret":
    print("Access Granted")
    print("Welcome! You must be someone very important.")
else:
    print("Access Denied")
    print("Shoo, go away")

input("\nPress the enter key to exit.")
