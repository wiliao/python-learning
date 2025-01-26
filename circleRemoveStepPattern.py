T = int(input("T:"))
circleList = []
for i in range(1, T + 1):
    circleList.append(i)
selectNum = 0
while len(circleList) >= 2:
    circleList.pop(selectNum)
    T -= 1
    selectNum += 1
    if selectNum >= (T):
        selectNum %= T

print(circleList)
for i in range(0, 10):
    print(i)