userInput = input("Enter a math equation: ")
x, y, z = userInput.split(" ")
x = float(x)
z = float(z)

match y:
    case "+":
        print(x + z)
    case "-":
        print(x - z)
    case "*":
        print(x * z)
    case "/":
        print(x / z)
