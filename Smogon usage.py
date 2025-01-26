#Flaws: doesn't really account for species clause; treats games like 12 people on one team

import random

OUPokemon = []

def addPoke(Poke, amount):
    for i in range(amount):
        OUPokemon.append(Poke)

addPoke("Weavile", 77)
addPoke("Kingambit", 9923)

curPoke = []
WSpotted = 0
Yw = 0
Nw = 0
YwT = 0
NwT = 0

for i in range(100):
    for i in range(100):
        for i in range(15):
            for i in range(6):
                selectPoke = random.randint(0, 9999)
                curPoke.append(OUPokemon[selectPoke])
            if "Weavile" in curPoke:
                WSpotted += 1
            curPoke.clear()
        if WSpotted == 0:
            Nw += 1
        else:
            Yw += 1
        WSpotted = 0
    YwT += Yw
    NwT += Nw
    Nw = 0
    Yw = 0

NwT /= 100
YwT /= 100
#print(curPoke)
#print(WSpotted)
print(NwT)
print(YwT)
