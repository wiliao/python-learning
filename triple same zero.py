print("This program will get the sum of 3 numbers, but if 2 are the same it will give 0.")
x = int(input("What is x? "))
y = int(input("What is y? "))
z = int(input("What is z? "))
if x == y or x == z or y == z:
    ans = 0
else:
    ans = x + y + z
print(ans)