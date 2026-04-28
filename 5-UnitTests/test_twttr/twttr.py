def main():
    user_input = input("Enter text: ")
    print(shorten(user_input))


def shorten(n):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    result = ""
    for character in n:
        if character not in vowels:
            result += character

    return result


if __name__ == "__main__":
    main()
