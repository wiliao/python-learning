print("This program will check if a letter is a vowel or a consonant.")
n = input("Letter. ")
def isVowel(let):
    vowels = 'aeiou'
    return let in vowels
ans = isVowel(n)
if ans == True:
    print(f"{n} is a vowel.")
else:
    print(f"{n} is a consonant.")