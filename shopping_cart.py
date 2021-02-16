# shopping_cart.py

import os
import sys
import datetime as dt
from dotenv import load_dotenv
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

load_dotenv()

file_name = "receipts/{date:%Y-%m-%d_%H-%M-%S-%f}.txt".format(date=dt.datetime.now())
# print(file_name)

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name("google-credentials.json", scope)
client = gspread.authorize(credentials)

spreadsheet = client.open_by_key(os.getenv("GOOGLE_SHEET_ID"))
sheet = spreadsheet.worksheet(os.getenv("SHEET_NAME", default="products"))

df = pd.DataFrame(sheet.get_all_records())
# df = pd.read_csv("data/products.csv")
# print(df)

products = df.to_dict('records')
[item.update({"price_per":"item"}) for item in products]
products.append({"id":99, "name": "Organic Bananas", "department": "fruit", "aisle": "fruits", "price": 0.79, "price_per": "pound"})
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
            product = dict(next(item for item in products if item["id"] == int(user_input_id)))
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