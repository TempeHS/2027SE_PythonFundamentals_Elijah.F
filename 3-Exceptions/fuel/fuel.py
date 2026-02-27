def main():
    while True:
        user_input = input("What fraction of fuel is in the tank? ")

        try:
            x = int(user_input[0])
            y = int(user_input[2])
            result = round((x / y) * 100)
            if y == 0 or x > y:
                raise ValueError
        except (ValueError, ZeroDivisionError):
            print("Error, retry: ")
            continue
        if result >= 99:
            print("F")
            break
        elif result <= 1:
            print("E")
            break
        else:
            print(f"{result}%")
            break


main()
