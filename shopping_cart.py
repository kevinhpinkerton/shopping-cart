# shopping_cart.py

import os
from dotenv import load_dotenv
import datetime as dt
import sys
import pandas as pd

file_name = "receipts/{date:%Y-%m-%d_%H-%M-%S-%f}.txt".format(date=dt.datetime.now())
# print(file_name)

df = pd.read_csv("data/products.csv")
products = df.to_dict('records')

[item.update({"price_per":"item"}) for item in products]
products.append({"id":21, "name": "Organic Bananas", "department": "fruit", "aisle": "fruits", "price": 0.79, "price_per": "pound"})
# print(products)

def to_usd(my_price):
    return f"${my_price:,.2f}" 

user_input_id = str()
user_input_pounds = float()
user_products = []
while True:
    user_input_id = input("Please input a product identifier: ").lower()
    if user_input_id != 'done':
        try:
            product = next(item for item in products if item["id"] == int(user_input_id))
            if product["price_per"] == "pound":
                user_input_pounds = input("Please input the number of pounds: ")
                product["price"] = product["price"] * float(user_input_pounds)
            user_products.append(product)
        except:
            print("Invalid integer: Type \"Done\" to finish checking out.") 
    else:
        break
# print(user_products)

# stdoutOrigin=sys.stdout 
# sys.stdout = open(file_name, "w")

print("---------------------------------")

print("GREEN FOODS GROCERY")
print("WWW.GREEN-FOODS-GROCERY.COM")

print("---------------------------------")

print("CHECKOUT AT: {date:%Y-%m-%d %I:%M %p}".format(date=dt.datetime.now()))

print("---------------------------------")

print("SELECTED PRODUCTS: ")
for product in user_products:
    print(" ... " + product["name"] + " (" + to_usd(product["price"]) + ")")

print("---------------------------------")

subtotal = sum([item["price"] for item in user_products])
print("SUBTOTAL: " + to_usd(subtotal))

load_dotenv()
tax = subtotal * float(os.getenv("TAX_RATE", default=.0875))
print("TAX: " + to_usd(tax))

total = subtotal + tax
print("TOTAL: " + to_usd(total))

print("---------------------------------")

print("THANKS, SEE YOU AGAIN SOON!")

print("---------------------------------")

# sys.stdout.close()
# sys.stdout=stdoutOrigin

# print(open(file_name, "r").read())