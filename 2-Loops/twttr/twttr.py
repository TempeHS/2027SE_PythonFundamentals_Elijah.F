user_input = input("Enter text: ")
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

for character in user_input:
    if character not in vowels:
        print(character, end="")

print("")
