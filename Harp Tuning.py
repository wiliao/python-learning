ins = input("Instructions: ")
out = ""
newLine = False
for i in ins:
    if i >= "A" and i <= "Z":
        if newLine:
            out += f"\n{i}"
            newLine = False
        else:
            out += i
    elif i == "+":
        out += " tighten "
    elif i == "-":
        out += " loosen "
    elif i >= "1" and i <= "9":
        out += i
        newLine = True
print(out)