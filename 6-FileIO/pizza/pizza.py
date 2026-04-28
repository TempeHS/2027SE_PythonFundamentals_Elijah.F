import sys
from tabulate import tabulate
import csv

try:
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1].endswith(".csv") is False:
        sys.exit("Not a CSV file")
except IndexError:
    sys.exit("Too few command-line arguments")

try:
    with open(sys.argv[1], "r") as file:
        reader = csv.DictReader(file)
        rows = []
        for row in reader:
            rows.append(row.values())
        print(tabulate(rows, headers=reader.fieldnames, tablefmt="grid"))
except FileNotFoundError:
    sys.exit("File not found")
