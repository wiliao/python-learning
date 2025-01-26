def gcd(x, y):   
   gcf = 1
   if x % y == 0:
       return y   
   for gcf in range(int(y / 2), 0, -1):
       if x % gcf == 0 and y % gcf == 0:
           break 
   return gcf
print("This prgram will determine the GCF of 2 numbers.")
a = int(input("What is the first number? "))
b = int(input("What is the second number? "))
print(f"The GCF is {gcd(a, b)}.")