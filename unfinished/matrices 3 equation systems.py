def matTwoSolve(tl, tr, bl, br):
    a = tl * br - tr * bl
    return a
print("This program will solve three equation systems.")
tl = int(input("What is the coefficent of x in the first equation? "))
tm = int(input("What is the coefficent of y in the first equation? "))
tr = int(input("What is the coefficent of z in the first equation? "))
ml = int(input("What is the coefficent of x in the second equation? "))
mm = int(input("What is the coefficent of y in the second equation? "))
mr = int(input("What is the coefficent of z in the second equation? "))
bl = int(input("What is the coefficent of x in the third equation? "))
bm = int(input("What is the coefficent of y in the thrid equation? "))
br = int(input("What is the coefficent of z in the thrid equation? "))
c1 = int(input("What is the constant in the first equation? "))
c2 = int(input("What is the constant in the second equation? "))
c3 = int(input("What is the constant in the second equation? "))
d = tl * matTwoSolve(mm, mr, bm, br) - tm * matTwoSolve(ml, mr, bl, br) + tr * matTwoSolve(ml, mm, bl, bm)
dx = c1 * matTwoSolve(mm, mr, bm, br) - tm * matTwoSolve(c2, mr, c3, br) + tr * matTwoSolve(c2, mm, c3, bm)
dy = tl * matTwoSolve(c2, mr, c3, br) - c1 * matTwoSolve(ml, mr, bl, br) + tr * matTwoSolve(ml, c2, bl, c3)
dz = tl * matTwoSolve(mm, mr, bm, br) - tm * matTwoSolve(c2, mr, c3, br) + c1 * matTwoSolve(c2, mm, c3, bm)
if d == 0:
    print("There is no solution to this system.")
else:
    x = str(dx / d)
    y = str(dy / d)
    z = str(dz / d)
    print("X is equal to", x + ", Y is equal to", y + ", and Z is equal to", z + ".")