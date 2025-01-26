print("Welcome to the factorial program. Enter a number to find its factorial.")
inp = int(input("Enter the number you want to factorial. "))

n = inp
ans = 1
while n != 0:
    ans *= n
    n -= 1

print(f"The factorial of {inp} is {ans}.")