purchase = float(input("Enter total purchase amount (NPR): "))
member = input("Are you a loyalty member? (yes/no): ")

discount = 0

if purchase < 1000:
    discount = 0
elif purchase < 5000:
    discount = 5
elif purchase < 15000:
    discount = 10
else:
    discount = 20

discount_amount = purchase * discount / 100
final_amount = purchase - discount_amount

# by Rahul Rimal

if member.lower() == "yes":
    extra_discount = final_amount * 5 / 100
    final_amount = final_amount - extra_discount

print("Original Amount: NPR", purchase)
print("Final Payable Amount: NPR", round(final_amount, 2))