amount_due = 50

while 0 < amount_due:
    user_input = int(input("Enter a coin: "))

    if user_input in [5, 10, 25]:
        amount_due = amount_due - user_input
        print("Amount due: " + str(amount_due))

    if user_input not in [5, 10, 25]:
        print("Error, only input 25, 10 or 5. Retry: ")

if 0 >= amount_due:
    print(f"Change owed: {abs(amount_due)}")
