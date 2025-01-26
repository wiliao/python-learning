paintDropNum = int(input("N: "))
borderL = 50
borderB = 50
borderT = 50
borderR = 50
coords = []
for i in range(paintDropNum):
    coords.append(input("Coordinate: "))

while paintDropNum > 0:
    currentCoord = (coords[0])
    xCoord = int(currentCoord[0] + currentCoord[1])
    if xCoord < borderL:
        borderL = xCoord
    if xCoord > borderR:
        borderR = xCoord
    yCoord = int(currentCoord[3] + currentCoord[4])
    if yCoord < borderB:
        borderB = yCoord
    if yCoord > borderT:
        borderT = yCoord
    paintDropNum -= 1
    coords.pop(0)

print(f"{borderL},{borderB}")
print(f"{borderR},{borderT}")