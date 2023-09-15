from player import Player
from startingZone import startingZone
from mainTown import mainTown
from enemies import Enemies


def main():
    print("welcome to Matrone")
    player_name = input("What is your name traveler?: ")
    # this creates a new value for the variable player_name
    # it is then passed as a parameter to the Player class and we reassign that
    # entire value as 'player' for ease of use when calling
    player = Player(player_name)
    visited_starting_area = False  # flag to track starting area visit

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
            # saying if visited_starting_area = false then execute code chunk
            if not visited_starting_area:
                print("A wise choice...")
                # send player to starting zone
                player = startingZone(player)
                # set visited_starting_area to True to disable access to startingZone
                visited_starting_area = True
            else:
                print("you have already visited the starting area...")
                player = mainTown(player)
        else:
            print("That's not a choice...")


if __name__ == "__main__":
    main()
