import random


def main():
    score = 0
    level = get_level()

    for _ in range(10):
        x = generate_number(level)
        y = generate_number(level)
        attempts = 0

        while attempts < 3:
            try:
                equation = int(input(f"{x} + {y}"))
                if equation != x + y:
                    print("EEE")
                    attempts = attempts + 1
                else:
                    score = score + 1
                    break
            except ValueError:
                continue


def generate_number(level):
    if level == 1:
        random_int = random.randint(0, 9)
    elif level == 2:
        random_int = random.randint(10, 99)
    elif level == 3:
        random_int = random.randint(100, 999)
    return random_int


def get_level():
    while True:
        try:
            level = int(input("Enter a level between 1, 2 or 3: "))
            if level not in [1, 2, 3]:
                raise ValueError
            else:
                return level
        except ValueError:
            pass


if __name__ == "__main__":
    main()
