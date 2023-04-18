# Backwards
# Print a message backwards

msg = input("Give me a message: ")

i = len(msg)
while i > 0:
    i -= 1
    print(msg[i], end="")

input("\n\nPress the enter key to exit.")
