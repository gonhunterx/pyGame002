def startingZone(player):
    while True:
        # just using true and going to make it so you can not die in the
        # starting zone
        print(
            "Hello there traveler, do you desire greatness? fortune? no? I didnt think so... come over here.. "
        )
        firstChoice = input("Walk over or leave")
        if firstChoice.lower() == "walk over":
            print("Have you heard of this place before?")
            secondChoice = input("yes or no?: ")
            if secondChoice.lower() == "yes":
                print(
                    f"Well {player.name}, it was right? you need to head to the tavern to meet my friend you look tough enough for the job."
                )
            else:
                print(
                    f"Well {player.name}, was it? you're in for a treat. Id say head to the tavern and meet my pal there. He could use a hand and you look like you could use a good bounty..."
                )
        else:
            print("you walk out of the building...")
