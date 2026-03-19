import random


def main():
    level = get_level()

    if level == 1:
        random_int = random.randint(0, 9)
    elif level == 2:
        random_int = random.randint(10, 99)
    elif level == 3:
        random_int = random.randint(100, 999)

    for _ in range(10):
        while True:
            try:
                equation = input(f"{random_int} + {random_int}")
                if equation != random_int + random_int:
                    print("EEE")
                    raise ValueError
                else:
                    score = score + 1
                    break
            except ValueError:
                continue


def get_level():
    while True:
        try:
            level = int(input("Enter a level between 1, 2 or 3: "))
            if level != 1 or level != 2 or level != 3:
                raise ValueError
            else:
                break
        except ValueError:
            continue


if __name__ == "__main__":
    main()
