print("Welcome to the Mario Kart 8 Deluxe Track list.")
mushroomCup = ["Mario Kart Stadium", "Water Park", "Sweet Sweet Canyon", "Thwomp Ruins"]
shellCup = ["Moo Moo Meadows", "Mario Circuit", "Cheep Cheep Beach", "Toad Turnpike"]
flowerCup = ["Mario Circuit", "Toad Harbor", "Twisted Mansion", "Shy Guy Falls"]
inpCup = input("What cup is your track in? ")
inpTrackNum = int(input("What number is the track in the cup? "))
if inpCup == "mushroom":
    if inpTrackNum == 1:
        print(mushroomCup[0])
