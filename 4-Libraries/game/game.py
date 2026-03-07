import random

user_level = int(input("Level: "))
correct_number = random.randrange(1, int(user_level))

while True:
    try:
        if user_level < 1:
            raise ValueError
    except (ValueError, TypeError):
        print("Level: ")

    try:
        user_guess = int(input("Guess: "))
        if user_guess < 1:
            raise ValueError
        if user_guess > correct_number:
            print("Too large!")
        elif user_guess < correct_number:
            print("Too small!")
        else:
            print("Just right!")
            break
    except ValueError:
        print("Invalid guess, retry: ")
