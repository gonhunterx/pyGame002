def mainTown(player):
    # enemy_health = 15
    # enemy_attack_power = 2
    print("You enter the main town...")
    while player.health > 0:
        print("welcome to the main town")

        print(f"Player Health: {player.health}")
        decisionOne = input("Where do you want to go traveler?: Bar, Woods, Shop")
        if decisionOne.lower() == "bar":
            print("You walk into the bar...")

        # print(f"Enemy Health: {enemy.health}")
