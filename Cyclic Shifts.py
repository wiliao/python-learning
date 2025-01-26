T = input()
S = input()

shifts = len(S)
SList = []
N = 0
sep = ""
inT = False
for i in S:
    SList.append(i)

while shifts > 0:
    if S in T:
        inT = True
        break
    else:
        N = SList[0]
        SList.pop(0)
        SList.append(N)
        S = sep.join(SList)
    shifts -= 1

if inT == True:
    print("Yes")
else:
    print("No")