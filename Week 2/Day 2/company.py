company = []
buying = []
selling = []

for i in range(10):
    name = input("Enter company name: ")
    company.append(name)

    buy = int(input("Enter buying price: "))
    buying.append(buy)

    sell = int(input("Enter selling price: "))
    selling.append(sell)

print("\nResult")

for i in range(10):
    print("\nCompany:", company[i])
    print("Buying Price:", buying[i])
    print("Selling Price:", selling[i])

    profit = selling[i] - buying[i]

    if profit > 0:
        print("Profit =", profit)
    elif profit < 0:
        print("Loss =", -profit)
    else:
        print("No Profit No Loss")