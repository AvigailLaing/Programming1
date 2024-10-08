price = float(input("Enter the price of the item: "))
tax = float(input("Enter the sales tax percentage: "))
percentage = tax * 0.01
newPrice = (percentage * price) + price
print(f"Your total is ${newPrice:.2f}")