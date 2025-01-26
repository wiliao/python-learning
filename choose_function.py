import numpy 
print("Welcome to the 'choose' function program!")
print("The choose function is when you want to see all the combinations using some types of things using the amount of things in a combination without caring about order.")
a = input("What is the amount of types of things? ")
b = input("What is the amount of things in a combination? ")
c = numpy.math.factorial(int(a))
d = int(a) - int(b)
e = numpy.math.factorial(d)
f = numpy.math.factorial(int(b))
g = e * f
h = c / g
print("The amount of combinations is", str(int(h)) + ".")
