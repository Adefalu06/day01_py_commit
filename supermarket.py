print("==SUPERMARKET CHECKOUT==")

price = float(input("Enter price per item: UGX "))

quantity = int(input("Enter Quantity: "))

if price <=0 or quantity<=0:
    print("Invalid price or quantity")

total = price * quantity

print("Total bill: UGX", total)
paid_amount = float(input("Enter amount paid: UGX "))

if paid_amount < total:
    print("Insufficient amount")
    print ("Still needed: UGX ", total -paid_amount)
else:
    print("Change: UGX", paid_amount - total)
    print("Thank you for shopping with us.")