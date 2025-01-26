P = int(input("P: "))
N = int(input("N: "))
R = int(input("R: "))
day = 0
infc = N
while infc <= P:
    day += 1
    N *= R
    infc += N
print(day)