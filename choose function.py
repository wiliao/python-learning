import numpy as n
print("Welcome to the 'choose' function program!")
print("The choose function is when you want to see all the combinations using some types of things using the amount of things in a combination without caring about order.")
types = input("What is the amount of types of things? ")
amount = input("What is the amount of things in a combination? ")
top = n.math.factorial(int(types))
bottomBracketsTwo = int(types) - int(amount)
bottomTwo = n.math.factorial(bottomBracketsTwo)
bottomOne = n.math.factorial(int(amount))
bottom = bottomTwo * bottomOne
answer = top / bottom
print(f"The amount of combinations is {str(int(answer))}.")