aliens = 2
password = "ALIENS"
print("Quickly! Aliens are invading the planet!")
print("You need to activate the global defence platforms.")
print("Hope you know the password, :O")
print()
print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("                                                                               WELCOME TO THE GLOBAL DEFENCE NETWORK                                                                              ")
print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print()
guess = input("Please enter the password.").upper()
while guess != password:
    print()
    print("INCORRECT PASSWORD.")
    print()
    aliens = aliens**2
    print("There are", aliens, "aliens on Earth now. Please try again")
    if aliens > 77000000000:
        break
    print()
    print("Password hint: the things that are attacking us.")
    print()
    guess = input("Quick! Please enter the password").upper()
if aliens > 77000000000:
    print("Noooooooooooo! The aliens have outnumbered us. All is lost.")
else:
    print("Hooray! We won the fight and the world is saved!")
