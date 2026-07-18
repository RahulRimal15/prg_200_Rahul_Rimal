def estimate_fare(distance_km, vehicle_type, surge=1.0):
    if vehicle_type.lower() == "bike":
        rate = 25
    elif vehicle_type.lower() == "car":
        rate = 50
    else:
        return -1

    fare = distance_km * rate * surge

    # by Rahul Rimal

    return fare


distance = float(input("Enter distance (km): "))
vehicle = input("Enter vehicle type (Bike/Car): ")

fare = estimate_fare(distance, vehicle)

if fare == -1:
    print("Invalid vehicle type.")
else:
    print("Estimated Fare: Rs.", fare)