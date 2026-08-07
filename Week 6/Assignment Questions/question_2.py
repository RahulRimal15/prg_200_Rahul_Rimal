bill_amount = 2500


def split_bill(people):
    global bill_amount

    bill_amount = bill_amount + 100

    tip_rate = 0.10

    def add_tip():
        nonlocal tip_rate
        tip_rate = tip_rate + 0.05

        #By Rahul Rimal

    add_tip()

    total_bill = bill_amount + (bill_amount * tip_rate)
    amount_per_person = total_bill / people

    print("Number of People:", people)
    print("Bill Amount: NPR", bill_amount)
    print("Tip Rate:", int(tip_rate * 100), "%")
    print("Total Bill: NPR", round(total_bill, 2))
    print("Amount Per Person: NPR", round(amount_per_person, 2))


split_bill(5)

print("Updated Global Bill Amount: NPR", bill_amount)

