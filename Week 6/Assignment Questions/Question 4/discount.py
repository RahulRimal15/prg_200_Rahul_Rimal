TAX_RATE = 0.13


def apply_discount(price, percent):
    discount_value = price * percent / 100
    return price - discount_value


def apply_tax(price):
    tax_amount = price * TAX_RATE
    return price + tax_amount


def final_price(price, discount_pct):
    discounted_price = apply_discount(price, discount_pct)
    total_price = apply_tax(discounted_price)

    return total_price