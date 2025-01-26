from random import randint
print("I have a number between 1 and 100, try and guess it.")
ans = randint(1, 100)
guess = None
guesses = 0
while guess != ans:
    guess = int(input("Guess the number. "))
    if guess > ans:
        print("Too high.")
    elif guess < ans:
        print("Too low.")
    guesses += 1
print("Correct!")
print(f"You took {guesses} tries.")