items_list = {}


while True:
    try:
        items = input("What do you want to buy? ").upper()
        items_list[items] = items_list.get(items, 0) + 1
    except EOFError:
        break

print("\nShopping list: ")
for items in sorted(items_list):
    print(f"{items_list[items]} {items}")
