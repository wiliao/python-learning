print("This program will determine the file type of your file.")
a = input("What is the file name? ")
f = a.split(".")
print(f"The file type is {repr(f[-1])}.")