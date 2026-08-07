name = input("What is your name? : ")
vowels = "aeiou"
has_vowels = 0
for word in name.lower():
    if word in vowels:
        has_vowels += 1
print(f"You have {has_vowels} vowels in your text.")        
