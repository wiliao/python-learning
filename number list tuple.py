print("This program will take a sequence of numbers (seperated by commas) and make a list and tuple out of it")
s = input("List the sequence of numbers. ")
ln = s.split(",")
print("List:", ln)
tn = tuple(ln)
print("Tuple:", tn)