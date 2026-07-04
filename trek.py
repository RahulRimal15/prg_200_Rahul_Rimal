trekkers = int(input("Enter number of trekkers: "))
tims_fee = float(input("Enter TIMS fee per person (Rs): "))
acap_fee = float(input("Enter ACAP fee per person (Rs): "))

permit_cost = tims_fee + acap_fee
total_cost = trekkers * permit_cost

service_charge = total_cost * 0.05
final_cost = total_cost + service_charge

average_cost = final_cost / trekkers

print(f"Total Permit Cost: Rs{total_cost:.2f}")
print(f"Agency Service Charge: Rs{service_charge:.2f}")
print(f"Final Group Cost: Rs{final_cost:.2f}")
print(f"Average Cost per Person: Rs{average_cost:.2f}")