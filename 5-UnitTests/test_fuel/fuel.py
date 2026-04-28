def main():
    user_input = input("What fraction of fuel is in the tank? ")
    print(gauge(convert(user_input)))


def convert(fraction):
    try:
        x = int(fraction[0])
        y = int(fraction[2])
        if y == 0 or x > y:
            raise ValueError
        percentage = round((x / y) * 100)
    except (ValueError, ZeroDivisionError):
        print("Error, retry: ")
    return percentage


def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
