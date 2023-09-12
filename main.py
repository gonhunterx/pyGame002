from player import Player
from startingZone import startingZone


def main():
    print("welcome to Matrone")
    player_name = input("What is your name traveler?: ")
    # this creates a new value for the variable player_name
    # it is then passed as a parameter to the Player class and we reassign that
    # entire value as 'player' for ease of use when calling
    player = Player(player_name)

    while player.health > 0:
        print("\nOptions:")
        print("1. Display Player Stats")
        print("2. Quit")
        print(
            f"================\n[🛡️  {player.name}]\n ❤️  : {player.health}\n Exp: {player.totalExp}\n================"
        )
        print("3. Continue...")
        choice = input("Enter your choice: ")

        if choice == "1":
            player.displayStats()
        elif choice == "2":
            print("Goodbye")
            break
        elif choice == "3":
            print("A wise choice...")
            player = startingZone(player)
        else:
            print("That's not a choice...")


if __name__ == "__main__":
    main()
