shop = []
units_list = []
bill_list = []

for i in range(10):
    print(f"\nShop {i+1}")

    name = input("Enter shop name: ")
    units = int(input("Enter units: "))

    while units <= 0:
        print("Invalid units! Try again.")
        units = int(input("Enter units: "))

    shop.append(name)
    units_list.append(units)

    if units <= 50:
        bill = units * 5
    else:
        bill = (50 * 5) + (units - 50) * 10

    bill_list.append(bill)

print("BILL REPORT")

for i in range(10):
    print(shop[i], "-", units_list[i], "units -", bill_list[i], "rupees")