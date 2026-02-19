def main():
    time = input("Enter a time: ")
    if 19 >= convert(time) >= 18:
        print("Dinner time")
    elif 13 >= convert(time) >= 12:
        print("Lunch time")
    elif 8 >= convert(time) >= 7:
        print("Breakfast time")
    else:
        print("nothing")


def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)
    return hours + minutes / 60


main()
