def multiStr(str, n):
    out = ''
    for i in range(n):
        out = out + str
    return out
print("This program will take a string and copy it n amount of times.")
str = input("What is the sentence you want to copy? ")
n = int(input("What is the number of times you want to copy it? "))
print(multiStr(str, n))