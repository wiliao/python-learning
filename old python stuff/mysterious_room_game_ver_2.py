import random
print("You are in a dark room in a mysterious castle")
print("In front of you are 4 doors. You must choose one.")
playerChoice = input("Choose door 1, 2, 3 or 4.")
if playerChoice == "1":
    print("You find a room of coins!! You're super rich!")
    print("GAME OVER. Congragulations, you won!")
elif playerChoice == "2":
    print("An angry SMG4 comes out of his room and shoots you with a gun.")
    print("GAME OVER. You lose, motherf*cker.")
elif playerChoice == "3":
    print("You go into the room and find a sleeping SMG4 Mario.")
    print("You can either:")
    print("1) Try to steal some of Mario's spaghetti.")
    print("2) Try to sneak around Mario to the exit.")
    dragonChoice = input("Type 1 or 2.")
    if dragonChoice == "1":
        print("Mario wakes up and rapes you.")
        print("GAME OVER. You lose, bitch.")
    elif dragonChoice == "2":
        print("You sneak around Mario and escape the castle, disappearing over the horizon.")
        print("GAME OVER. Congragulations, you won!")

    else:
        print("The room collapsed and you died.")
        print("GAME OVER. You lose, idiot.")
elif playerChoice == "4":
    print("You enter a room with a Teletubbie.")
    print("He asks you to guess what number it is thinking of, between 1 and 10.")
    number = int(input("What number do you choose?"))
    if number == random.randint(1,10):
        print("The Teletubbie decides to be nice and lets you go.")
        print("GAME OVER. Congragulations, you won!")
    else:
        print("He tells you you're wrong.")
        print("He kills you because of that.")
        print("GAME OVER. You lose, dumbo.")
else:
    print("The castle collapsed and you died.")
    print("GAME OVER. You lose, idiot.")
print("Run again to play again.")
