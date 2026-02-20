user_input = input("Enter a coin: ")
amount_due = 50 - int(user_input)

while 0 < amount_due <= 50:
    if user_input != 25 or user_input != 10 or user_input != 5:
        input("Error, invalid amount: Retry ")
    elif user_input == 25 or user_input == 10 or user_input == 5:
        input("Amount due: " + str(amount_due), "\n")

while 0 >= amount_due:
    print("Change owed: " + str(amount_due))
