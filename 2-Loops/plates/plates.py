def main():
    plate = input("Enter plate: ")
    if (
        character_range(plate)
        and first_two_letters(plate)
        and no_punctuation(plate)
        and numbers_at_end(plate)
    ):
        print("Valid")
    else:
        print("Invalid")


def character_range(plate):
    if len(plate) >= 2 and len(plate) <= 6:
        print("Character requirement met")
        return True
    else:
        print("Character requirement has not been met")
        return False


def first_two_letters(plate):
    if plate[0].isalpha() and plate[1].isalpha():
        print("First two characters are letters")
        return True
    else:
        print("First two characters must be letters, try again")
        return False


def no_punctuation(plate):
    if plate.isalnum():
        print("No punctuation requirement met")
        return True
    else:
        print("No punctuation is allowed")
        return False


def numbers_at_end(plate):
    number_started = False
    for character in plate:
        if character.isdigit():
            if not number_started:
                if character == "0":
                    print("0 cannot be inputted first, retry")
                    return False
                number_started = True
        else:
            if number_started:
                print("Once numbers can begin, only numbers can follow")
                return False
    print("Requirement met, numbers follow numbers")
    return True


main()
