discount_rate = 0.10


def calculate_discount(price):

    discount_rate = 0.10

    def change_discount():
        nonlocal discount_rate
        discount_rate = 0.15

    change_discount()

    discounted_price = price - (price * discount_rate)

    print("Original Price: NPR", price)
    print("Discount Rate:", int(discount_rate * 100), "%")
    print("Discount Amount: NPR", round(price * discount_rate, 2))
    print("Final Price: NPR", round(discounted_price, 2))


calculate_discount(4000)

print("Global Discount Rate:", int(discount_rate * 100), "%")
