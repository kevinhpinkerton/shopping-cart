# shopping_cart.py

import os
from dotenv import load_dotenv
import datetime
import sys

file_name = "receipts/{date:%Y-%m-%d_%H-%M-%S-%f}.txt".format(date=datetime.datetime.now())
# print(file_name)

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

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