class Bike:
    def __init__(self, name="", price=0):
        self.name = name
        self.price = price

# by Rahul Rimal

name = input("Enter bike name: ")
price = int(input("Enter bike price: "))

bike1 = Bike(name, price)

print("\nBike Details")
print("Bike Name:", bike1.name)
print("Bike Price: Rs.", bike1.price)
