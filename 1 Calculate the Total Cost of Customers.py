item_prices = [2.5, 1.0, 3.5, 4.0]
quantities = [3, 2, 1, 4]
discount_rate = 10
tax_rate = 8

subtotal = sum(price * quantity for price, quantity in zip(item_prices, quantities))

discount_amount = (discount_rate / 100) * subtotal

total_after_discount = subtotal - discount_amount

tax_amount = (tax_rate / 100) * total_after_discount

final_total = total_after_discount + tax_amount

print(f"Subtotal:",subtotal)
print("Discount:",discount_amount)
print("total_after_discount:",total_after_discount)
print("Tax:",tax_amount)
print("Final Total:",final_total)
