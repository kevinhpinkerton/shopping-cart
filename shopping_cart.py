# shopping_cart.py

import os
from dotenv import load_dotenv
import datetime
import sys
import csv

file_name = "receipts/{date:%Y-%m-%d_%H-%M-%S-%f}.txt".format(date=datetime.datetime.now())
# print(file_name)

with open("data/products.csv", "r") as f:
        reader = csv.DictReader(f)
        products = list(reader)

[item.update({"price_per":"item"}) for item in products]
products.append({"id":21, "name": "Organic Bananas", "department": "fruit", "aisle": "fruits", "price": 0.79, "price_per": "pound"})
# print(products)

def to_usd(my_price):
    return f"${my_price:,.2f}" 

user_input = str()
user_input_extra = float()
user_products = []
while True:
    user_input = input("Please input a product identifier: ").lower()
    if user_input != 'done':
        try:
            product = next(item for item in products if item["id"] == int(user_input))
            if product["price_per"] == "pound":
                user_input_extra = input("Please input the number of pounds: ")
                product["price"] = product["price"] * float(user_input_extra)
            user_products.append(product)
        except:
            print("Invalid integer: Type \"Done\" to finish checking out.") 
    else:
        break
# print(user_products)

# stdoutOrigin=sys.stdout 
# sys.stdout = open(file_name, "w")

subtotal = sum([item["price"] for item in user_products])
print(to_usd(subtotal))

load_dotenv()
tax = subtotal * float(os.getenv("TAX_RATE", default=.0875))
print(to_usd(tax))

total = subtotal + tax
print(to_usd(total))

# sys.stdout.close()
# sys.stdout=stdoutOrigin

# print(open(file_name, "r").read())