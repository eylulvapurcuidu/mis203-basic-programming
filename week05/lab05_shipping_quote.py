def calculate_subtotal(prices):
    return sum(prices)


def get_discount_rate(subtotal):
    if subtotal >= 100:
        return 0.10
    elif subtotal >= 50:
        return 0.05
    else:
        return 0.0


def calculate_shipping_fee(subtotal):
    if subtotal >= 75:
        return 0
    else:
        return 8


def calculate_final_total(subtotal, discount_rate, shipping_fee):
    discount = subtotal * discount_rate
    return subtotal - discount + shipping_fee


# Sample Order 1
order1 = [30, 25, 20]

subtotal1 = calculate_subtotal(order1)
discount_rate1 = get_discount_rate(subtotal1)
shipping_fee1 = calculate_shipping_fee(subtotal1)
total1 = calculate_final_total(subtotal1, discount_rate1, shipping_fee1)

print("Order 1")
print("Subtotal:", subtotal1)
print("Discount rate:", discount_rate1)
print("Shipping fee:", shipping_fee1)
print("Final total:", total1)


# Sample Order 2
order2 = [60, 50, 30]

subtotal2 = calculate_subtotal(order2)
discount_rate2 = get_discount_rate(subtotal2)
shipping_fee2 = calculate_shipping_fee(subtotal2)
total2 = calculate_final_total(subtotal2, discount_rate2, shipping_fee2)

print("\nOrder 2")
print("Subtotal:", subtotal2)
print("Discount rate:", discount_rate2)
print("Shipping fee:", shipping_fee2)
print("Final total:", total2)