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
            if day <= 31 and month <= 12:
                print(f"{year}-{month:02}-{day:02}")
                break
            else:
                raise ValueError
    except ValueError:
        print("Invalid date, retry: ")
	try:
        