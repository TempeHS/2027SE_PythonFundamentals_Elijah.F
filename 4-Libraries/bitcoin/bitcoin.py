import requests
import sys

try:
    n = float(sys.argv[1])
except (ValueError, IndexError):
    sys.exit("Invalid number")

try:
    response = requests.get(
        "https://api.coindesk.com/v1/bpi/currentprice.json", timeout=10
    )
    o = response.json()
    amount = o["bpi"]["USD"]["rate_float"]
except requests.RequestException:
    sys.exit("Error occurred.")

total = amount * n
print(f"{total:,.4f}")
