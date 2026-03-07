months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

while True:
    try:
        user_input = input("Enter a date: ")
        if "/" in user_input:
            parts = user_input.split("/")
            month = int(parts[0])
            day = int(parts[1])
            year = int(parts[2])
            if 1 <= day <= 31 and 1 <= month <= 12:
                print(f"{year}-{month:02}-{day:02}")
                break

            else:
                raise ValueError
        elif "," in user_input:
            parts_2 = user_input.replace(",", "").split()
            month_2 = parts_2[0]
            month_2_int = months.index(month_2) + 1
            day_2 = int(parts_2[1])
            year_2 = int(parts_2[2])
            if 1 <= day_2 <= 31 and 1 <= month_2_int <= 12:
                print(f"{year_2}-{month_2_int:02}-{day_2:02}")
                break
        else:
            raise ValueError
    except ValueError:
        print("Invalid date, retry: ")
