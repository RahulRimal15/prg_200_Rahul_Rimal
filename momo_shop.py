cost_price_per_plate = int(input("Enter the cost price of momo per plate: "))
selling_price_per_plate = int(input("Enter the selling price of momo per plate: "))
number_of_plates_sold = int(input("Enter the number of plates sold of momo: "))

total_revenue = selling_price_per_plate * number_of_plates_sold
total_cost = cost_price_per_plate * number_of_plates_sold
total_profit = total_revenue - total_cost

profit_margin_percentage = (total_profit / total_revenue) * 100

print(f"Total Revenue: Rs. {total_revenue}")
print(f"Total Cost: Rs. {total_cost}")
print(f"Total Profit: Rs. {total_profit}")
print(f"Profit Margin: {profit_margin_percentage:.2f}%")