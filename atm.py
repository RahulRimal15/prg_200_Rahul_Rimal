correct_pin = 2396

for attempt in range(3):
    pin = int(input("Enter your PIN: "))

    if pin == correct_pin:
        print("PIN accepted!")

        instruction = input("Cash transfer or withdrawal?: ").lower()

        if instruction == "cash transfer":
            amount = int(input("Enter the amount to transfer: "))
            print(f"Rs.{amount} transferred successfully.")

        elif instruction == "withdrawal":
            amount = int(input("Enter the amount to withdraw: "))
            print(f"Please collect your Rs.{amount}.")

        else:
            print("Please enter a valid instruction.")

        break   # Exit the loop because the PIN was correct

    else:
        remaining = 2 - attempt
        if remaining > 0:
            print(f"Incorrect PIN. You have {remaining} attempt(s) left.")
        else:
            print("Incorrect PIN. Your account has been locked.")