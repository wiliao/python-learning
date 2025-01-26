def lcm(x, y):
    lcm = 1
    for lcm in range(1, x * y):
        if lcm % x == 0 and lcm % y == 0:
            break
    if x % y and y % x != 0:
        lcm += 1
    return lcm
print("This prgram will determine the LCM of 2 numbers.")
a = int(input("What is the first number? "))
b = int(input("What is the second number? "))
print(f"The LCM is {lcm(a, b)}.")