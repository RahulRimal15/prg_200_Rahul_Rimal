from discount import final_price, TAX_RATE


products = [
    ("Laptop", 85000, 10),
    ("Headphones", 4500, 15),
    ("Phone Case", 800, 5),
    ("USB Cable", 600, 0)
]

#By Rahul Rimal

print("===== SHOPPING BILL =====")
print("Tax Rate:", int(TAX_RATE * 100), "%")
print()

grand_total = 0

for product, price, discount in products:
    total = final_price(price, discount)
    grand_total += total

    print("Product:", product)
    print("Price: NPR", price)
    print("Discount:", discount, "%")
    print("Final Price: NPR", round(total, 2))
    print("------------------------")

print("Grand Total: NPR", round(grand_total, 2))




