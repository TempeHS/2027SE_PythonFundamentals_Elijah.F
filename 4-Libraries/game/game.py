import random


while True:
    try:
        user_level = int(input("Level: "))
        if user_level < 1:
            raise ValueError
        else:
            break
    except (ValueError, TypeError):
        continue

correct_number = random.randint(1, user_level)

while True:
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
        continue
