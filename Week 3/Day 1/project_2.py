def recharge_cost(gb, validity_days=30):
    if gb == 1:
        price = 150
    elif gb == 5:
        price = 500
    elif gb == 10:
        price = 900
    else:
        return -1

    # by Rahul Rimal

    return price


data = int(input("Enter data pack (1, 5 or 10 GB): "))

cost = recharge_cost(data)

if cost == -1:
    print("Invalid data pack.")
else:
    print("Recharge Cost: Rs.", cost)
    print("Validity:", 30, "days")