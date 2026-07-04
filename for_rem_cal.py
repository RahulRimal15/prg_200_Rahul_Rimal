USD_amount_sent = float(input("Enter the USD amount sent: "))

current_exchange_rate = 41.41
service_fee = 0.05

NPR_amount = USD_amount_sent * current_exchange_rate
fee = NPR_amount * service_fee
final_amount = NPR_amount - fee

print(f"The final amount received after fee charged is {final_amount:.2f} NPR.")