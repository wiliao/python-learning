print("This program will solve 2 equation systems for you.")
tl = int(input("What is the coefficent of x in the first equation? "))
tr = int(input("What is the coefficent of y in the first equation? "))
bl = int(input("What is the coefficent of x in the second equation? "))
br = int(input("What is the coefficent of x in the second equation? "))
a1 = int(input("What is the constant in the first equation? "))
a2 = int(input("What is the constant in the second equation? "))
d = tl * br - tr * bl
if d == 0:
    print("This system either has no solution or the solution is 0.")
else:
    dx = a1 * br - a2 * tr
    dy = tl * a2 - bl * a1
    x = (dx / d)
    y = dy / d
    print(f"X equals {x}. Y equals {y}.")