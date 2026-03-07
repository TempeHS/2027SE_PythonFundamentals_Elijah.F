import sys
from pyfiglet import Figlet
import random

figlet = Figlet()

if len(sys.argv) not in [1, 3]:
    sys.exit("Invalid usage")

if len(sys.argv) == 3:
    if sys.argv[1] not in ["-f", "--font"]:
        sys.exit("Invalid usage")

    font = sys.argv[2]

    if font not in figlet.getFonts():
        sys.exit("Invalid usage")

else:
    figlet.setFont(font=random.choice(figlet.getFonts()))

user_input = input("Input: ")
print(figlet.renderText(user_input))
