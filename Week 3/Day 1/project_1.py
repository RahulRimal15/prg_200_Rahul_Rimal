def ticket_price(seat_type, count):
    if seat_type.lower() == "regular":
        price = 400
    elif seat_type.lower() == "recliner":
        price = 700
    else:
        return -1

    total = price * count

    # by Rahul Rimal

    return total


seat = input("Enter seat type (Regular/Recliner): ")
tickets = int(input("Enter number of tickets: "))

amount = ticket_price(seat, tickets)

if amount == -1:
    print("Invalid seat type.")
else:
    print("Total Ticket Price: Rs.", amount)