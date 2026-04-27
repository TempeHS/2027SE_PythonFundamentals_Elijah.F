import sys
from PIL import Image, ImageOps

if len(sys.argv) != 3:
    sys.exit("Too few command-line arguments")
if sys.argv[1].endswith(".jpg", ".jpeg", ".png") is False:
    sys.exit("Invalid input")
if sys.argv[2].endswith(".jpg", ".jpeg", ".png") is False:
    sys.exit("Invalid input")

input = sys.argv[1]
output = sys.argv[2]

shirt = Image.open("shirt.png")
photo = Image.open(input)
resized = ImageOps.fit(photo, shirt.size)
