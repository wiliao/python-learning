print("This program will will determine if your number is odd or even.")
n = int(input("What is your number? "))
n = n % 2
if n == 0:
    print("Your number is even.")
elif n == 1:
    print("Your number is odd.")