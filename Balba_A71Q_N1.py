#1. PAYMENT METHOD CHECKER
valid_payment = ["GCash, Cash, PayPal"]
payment = input("Enter your mode of payment: ")
if payment in valid_payment:
    print("Valid payment method.")
else:
    print("Invalid payment method.")