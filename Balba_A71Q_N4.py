#4. PIN VALIDATOR
pin = input("Enter your 6-digit PIN: ")
if len(pin) == 6 and pin.isdigit():
    print("Valid PIN.")
else:
    print("Invalid PIN. Enter exactly 6 digits.")