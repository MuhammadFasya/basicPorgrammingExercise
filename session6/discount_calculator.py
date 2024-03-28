# Discount Calculator: Create a program that calculates the total cost after applying a discount based on the following conditions:

# If the purchase amount is greater than $100, apply a 10% discount.

# If the purchase amount is greater than $50 but less than or equal to $100, apply a 5% discount.

# If the purchase amount is less than or equal to $50, apply no discount.

price =  int(input("Enter Price: "))

if (price > 100): 
    
    discount = int(price * 0.1)
    total_cost = price - discount
    print("Cost grather than $100")
    print("Discount 10% of the total cost $", discount )
    print(f"Total cost after discount: ${total_cost}")
elif(price > 50 and price <= 100):
    discount = int(price * 0.05)
    total_cost = price - discount
    print("Cost grather than $50 but less than or equal to $100")
    print("Discount 5% of the total cost $", discount )
    print(f"Total cost after discount: ${total_cost}")
else: 
    print("Cost grather than $50, Not Discount")