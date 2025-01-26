print("This program will add 'if' to the start of your sentence if there isn't already one.")
sen = input("What is your sentence? ")
def ifStr(str):
    if len(str) >= 2 and str[:2] == "Is":
        return str
    return "Is " + str
print(ifStr(sen))