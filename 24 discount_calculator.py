# Final Price Calculator

price = int(input("Enter the product price: "))
discount_percentage = float(input("Enter discount percentage: "))

final_price = price - (price * discount_percentage) / 100

print("Final price =", final_price)