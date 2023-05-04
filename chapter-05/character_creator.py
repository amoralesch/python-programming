# Character Creator
#
# Gives the user X amount of points to distribute in 4 attributes.
# User can add or remove points as needed.

MAX_POINTS = 30
attributes = {
    "Strength": 0,
    "Health": 0,
    "Wisdom": 0,
    "Dexterity": 0
}

choice = None
free_points = MAX_POINTS
while choice != "0":
    print(
        """
Character Creator

0 - Exit
1 - See Attributes
2 - Assign Attribute Points
3 - Remove Attribute Points
        """
    )
    choice = input("\nWhat do you want to do? ")

    if choice == "1":
        print("You have", free_points, "points to assign.")
        print("Your character have the following attributes:")
        print(attributes)

    elif choice == "2":
        if free_points <= 0:
            print("You have no more points to assign.")
            continue

        attr = None
        while attr not in attributes:
            attr = input("\nWhich attribute do you want to assign points to? ")

            if attr not in attributes:
                print("Invalid attribute.")

        points = free_points + 1
        while points > free_points:
            points = int(input("How many points do you want to assign? "))

            if points > free_points:
                print("You only have", free_points, "free points to assign.")

        attributes[attr] = attributes[attr] + points
        free_points -= points

    elif choice == "3":
        if free_points == MAX_POINTS:
            print("There are no points assigned to any attribute.")
            continue

        attr = None
        while attr not in attributes:
            attr = input("\nWhich attribute do you want to remove from? ")

            if attr not in attributes:
                print("Invalid attribute.")

        points = attributes[attr] + 1
        while points > attributes[attr]:
            points = int(input("How many points do you want to remove? "))

            if points > attributes[attr]:
                print("There are only", attributes[attr], "points to remove.")

        attributes[attr] = attributes[attr] - points
        free_points += points

input("\nPress the enter key to exit.")
