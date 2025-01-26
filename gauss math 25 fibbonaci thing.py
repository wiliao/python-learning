x = int(input("Number. "))
def fiboAdd(x, n):
    if n == 1:
        return 1
    if n == 2:
        return x
    if n > 2:
        return fiboAdd(x, n - 2) + fiboAdd(x, n - 1)
n = 1
sum = 0
while sum < 463:
    sum = fiboAdd(x, n)
    n += 1
if sum == 463:
    print("Your number in a Fibonnaci sequence can become 463")
else:
    print("Your number in a Fibonnaci sequence cannot become 463")