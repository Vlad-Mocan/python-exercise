word = input("Please enter a word: ")
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
found_vowels = []

for letter in word:
    if letter in vowels and letter not in found_vowels:
        found_vowels.append(letter)

print(
    f"Your word ({word}) contains {len(found_vowels)} vowels. The vowels found are: {found_vowels}"
)
