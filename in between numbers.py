print("This program will tell you if your number is within a hundred of 1000 or 2000.")
n = int(input("What is your number? "))
a = abs(1000 - n)
if a <= 100:
    print("Your number is within 100 of 1000")
elif abs(a - 1000) <= 100:
    print("Your number is within 100 of 2000")
else:
    print("Your number is not within 100 of 1000 or 2000")