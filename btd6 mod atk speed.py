tAtkSpe = 0.2597
simTime = 0
tAtks = 0

while simTime <= 45:
    simTime += tAtkSpe
    tAtks += 1
    tAtkSpe *= 20 / 19

print(tAtks)