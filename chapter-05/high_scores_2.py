# High Scores 2.0
# Demonstrates nested sequences

scores = []
choice = None

while choice != "0":
    print(
        """
High Scores 2.0

0 - Quit
1 - List Scores
2 - Add a Score
        """
    )

    choice = input("Choice: ")
    print()

    # exit
    if choice == "0":
        print("Good-bye.")

    # list high-score table
    elif choice == "1":
        print("High Scores")
        for entry in scores:
            score, name = entry
            print(name, "\t", score)

    # add a score
    elif choice == "2":
        name = input("What is the player's name? ")
        score = int(input("What score did the player get? "))
        entry = (score, name)
        scores.append(entry)
        scores.sort(reverse=True)
        scores[:5]  # keep only top 5 scores

    else:
        print("Sorry, but", choice, "isn't a valid choice.")

input("\nPress the enter key to exit.")
