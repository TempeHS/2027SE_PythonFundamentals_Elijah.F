import inflect

names_list = []
while True:
    try:
        user_input = input("Enter a name: \n")
        names_list.append(user_input)
    except EOFError:
        break

p = inflect.engine()

print("Adieu, adieu, to", p.join(names_list))
