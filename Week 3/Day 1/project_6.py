def sort_orders(orders):
    orders.sort(key=lambda order: order[1])

    # by Rahul Rimal

    return orders


orders = [
    ("ORD101", 25),
    ("ORD102", 12),
    ("ORD103", 40),
    ("ORD104", 18)
]

sorted_orders = sort_orders(orders)

print("Orders sorted by delivery time:\n")

for order_id, time in sorted_orders:
    print("Order ID:", order_id, "- Delivery Time:", time, "minutes")