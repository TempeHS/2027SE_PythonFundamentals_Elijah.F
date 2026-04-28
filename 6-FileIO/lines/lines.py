import sys

count = 0
try:
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1].endswith(".py") is False:
        sys.exit("Not a python file")
except IndexError:
    sys.exit("Too few command-line arguments")

try:
    with open(sys.argv[1], "r") as file:
        for line in file:
            if line.lstrip().startswith("#") is True:
                continue
            if line.strip() == "":
                continue
            else:
                count += 1
except FileNotFoundError:
    sys.exit("File not found")

print(f"Number of lines: {count}")
