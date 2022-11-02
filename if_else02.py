# Write a Program to Check Whether a Character is Vowel or Consonant
alpha = input("Enter The Alphabet :\n")
alpha = alpha.upper()
if alpha in ("A" , "E" , "I" , "O" , "U"):
    print(f"{alpha} is an vowel")
else:
    print(f"{alpha} is a consonant")