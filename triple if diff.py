print("This program will add the sum of three numbers but if they are the same will triple the sum.")
a = int(input("What is a? "))
b = int(input("What is b? "))
c = int(input("What is c? "))
if a == b and b == c:
    an = a + b + c
    ans = 3 * an
else:
    ans = a + b + c
print(f"The result is {ans}.")