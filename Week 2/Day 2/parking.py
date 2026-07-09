vehicle_no = []
vehicle_type = []
hours = []
fee = []

n=int(input("Enter number of vehicles: "))

total= 0

for i in range(n):
    vehicle_no.append(input("Enter vehicle number: "))
    vehicle_type.append(input("Enter vehicle type (motorcycle/car): "))
    hours.append(int(input("Enter parking hours: ")))

    if hours[i] <= 2:
        charge = 50
    elif hours[i] <= 5:
        charge = 50 + (hours[i] - 2) * 30
    else:
        charge = 50 + (hours[i] - 2) * 90

    if vehicle_type[i].lower() == "motorcycle":
        charge = charge * 0.8

    if charge > 500:
        charge = charge + 50

    fee.append(charge)
    total = total + charge

print("\nVehicle Details")

for i in range(n):
    print("Vehicle No:", vehicle_no[i])
    print("Type:", vehicle_type[i])
    print("Hours:", hours[i])
    print("Fee: Rs.", fee[i])
    print()

print("Total Revenue = Rs.", total)