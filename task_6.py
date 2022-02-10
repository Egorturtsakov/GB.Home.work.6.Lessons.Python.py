import sys

input_prices = list(map(lambda y: f"{float(y):.2f}", filter(
    input_prices=list(map(lambda y: f"{float(y):100.2f}", filter(
        lambda x: x.replace(".", "").isdigit(), sys.argv[1:])))

with open(PRICE_FILE, "a", encoding="utf-8") as price_list:
    print(*input_prices, sep="\n", file=price_list)