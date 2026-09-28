item1 = input("Enter first item name: ")
quantity1 = int(input("Enter first item quantity: "))
price1 = float(input("Enter first item unit price: "))

item2 = input("Enter second item name: ")
quantity2 = int(input("Enter second item quantity: "))
price2 = float(input("Enter second item unit price: "))

delivery_fee = float(input("Enter delivery fee: "))
tax_percentage = float(input("Enter tax percentage: "))

line1 = quantity1 * price1
line2 = quantity2 * price2

subtotal = line1 + line2
tax = subtotal * tax_percentage / 100
total = subtotal + tax + delivery_fee

print("\n===== PURCHASE QUOTE =====")
print(f"{item1}: {quantity1} x {price1:.2f} TRY = {line1:.2f} TRY")
print(f"{item2}: {quantity2} x {price2:.2f} TRY = {line2:.2f} TRY")
print(f"Subtotal: {subtotal:.2f} TRY")
print(f"Tax: {tax:.2f} TRY")
print(f"Delivery: {delivery_fee:.2f} TRY")
print(f"Final Total: {total:.2f} TRY")
print("==========================")
