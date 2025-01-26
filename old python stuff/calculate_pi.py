import math
from decimal import *
getcontext().prec = 50
pi = 0
polySides = 6
sideLen = 1
perim = 6
dia = 2
while polySides < 1000000000000000000000000000000:
    sideLen2 = Decimal(sideLen) / Decimal(2)
    radius_a = Decimal(((1**2)-(sideLen/2)**2)).sqrt()
    radius_b = Decimal(1) - Decimal(radius_a)
    sideLenNew = Decimal((radius_b**2)+(sideLen2**2)).sqrt()
    polyCircum = Decimal(polySides * sideLen)
    pi = polyCircum / dia
    print("Polygon Sides:", polySides, " Pi=", format(pi,"0.50"))
    sideLen = sideLenNew
    polySides = polySides * 2
