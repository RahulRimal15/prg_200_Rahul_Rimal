salary = float(input("Enter monthly basic salary (Rs): "))
deduction_percent = float(input("Enter deduction percentage: "))

bonus = salary

deduction = bonus * deduction_percent / 100

take_home_bonus = bonus - deduction

print(f"Dashain Bonus: Rs {bonus:.2f}")
print(f"Deduction: Rs {deduction:.2f}")
print(f"Take Home Bonus: Rs {take_home_bonus:.2f}")