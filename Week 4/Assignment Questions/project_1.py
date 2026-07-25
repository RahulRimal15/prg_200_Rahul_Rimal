inventory = {
    "rice": {"price": 120, "stock": 20},
    "milk": {"price": 90, "stock": 10},
    "bread": {"price": 60, "stock": 15},
    "eggs": {"price": 15, "stock": 30}
}

cart = {
    "rice": 2,
    "milk": 3,
    "eggs": 12
}


def process_order(inventory, cart):

    total_bill = 0
    purchased_items = {}

    for item in cart:

        quantity = cart[item]

        if item in inventory:

            if inventory[item]["stock"] >= quantity:

                cost = inventory[item]["price"] * quantity
                total_bill += cost

                purchased_items[item] = {
                    "quantity": quantity,
                    "cost": cost
                }

                inventory[item]["stock"] -= quantity

            else:
                print("Sorry, not enough stock for", item)

    # by Rahul Rimal

    print("\n------ Bill ------")

    for item in purchased_items:
        print(item, "x" + str(purchased_items[item]["quantity"]),
              "= NPR", purchased_items[item]["cost"])

    print("------------------")
    print("Grand Total: NPR", total_bill)

    print("\nUpdated Inventory")

    for item in inventory:
        print(item, "= Stock:", inventory[item]["stock"])


process_order(inventory, cart)