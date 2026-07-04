before_units= int(input("Enter how many units used before:"))
after_units= int(input("Enter how many unites used after:"))

per_unit= 11
units_consumed= after_units - before_units
commission= 0.05
price= per_unit * units_consumed
total_price = price + (price * commission)
print(f" The total price for electricity bill: {total_price}")