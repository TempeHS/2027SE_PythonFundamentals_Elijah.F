import sys
import csv

students = []


if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

try:
    file_1 = open(sys.argv[1], "r")
    reader = csv.DictReader(file_1)
    for row in reader:
        last, first = row["name"].replace('"', "").split(", ")
        students.append(
            {
                "last": last,
                "first": first,
                "house": row["house"],
            }
        )
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")

try:
    with open(sys.argv[2], "w") as file_2:
        writer = csv.DictWriter(file_2, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for student in students:
            writer.writerow(
                {
                    "first": student["first"],
                    "last": student["last"],
                    "house": student["house"],
                }
            )
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[2]}")

file_1.close()
