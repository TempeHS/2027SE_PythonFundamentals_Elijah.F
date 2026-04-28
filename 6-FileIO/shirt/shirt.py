import sys
import os
from PIL import Image, ImageOps

if len(sys.argv) != 3:
    sys.exit("Too few command-line arguments")

input = sys.argv[1]
output = sys.argv[2]
valid_extensions = (".jpg", ".jpeg", ".png")

if not input.lower().endswith(valid_extensions):
    sys.exit("Invalid input")
if not output.lower().endswith(valid_extensions):
    sys.exit("Invalid output")

if os.path.splitext(input)[1].lower() != os.path.splitext(output)[1].lower():
    sys.exit("File extensions must be the same")

try:
    shirt = Image.open("shirt.png")
    photo = Image.open(input)
except FileNotFoundError:
    sys.exit("File not found")

resized = ImageOps.fit(photo, shirt.size)
pasted_shirt = resized.paste(shirt, shirt)
saved_image = resized.save(output)
