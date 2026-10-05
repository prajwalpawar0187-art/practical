buying_price=int(input("Enter buying amount:"))
selling_price=int(input("Enter selling amount:"))
if(buying_price>selling_price):
    print("Loss!! of:",buying_price-selling_price)
else:
    print("Profit of:",selling_price-buying_price)