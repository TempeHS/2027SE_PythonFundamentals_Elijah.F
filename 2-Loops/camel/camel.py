variable_name = input("Enter a variable name in camel case: ")

snake_case = ""

for i, char in enumerate(variable_name):
    if char.isupper() and i > 0:
        snake_case += "_"
    snake_case += char.lower()

print(snake_case)
