vowels = ["a", 'o', 'u', 'e', 'i']
word = input()

no_vowels_word = []

for char in word:
    if char not in vowels:
        no_vowels_word.append(char)

print("".join(no_vowels_word))

