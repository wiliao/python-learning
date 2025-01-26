def substring_copy(str, n):
  flen = 2
  if flen > len(str):
    flen = len(str)
  substr = str[:flen]
  result = ""
  for i in range(n):
    result = result + substr
  return result
print("This program will do something.")
word = input("a word please. ")
t = int(input("number. "))
print(substring_copy(word, t))