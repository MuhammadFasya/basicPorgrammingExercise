#Items name, price, and stock
items = {
    "Lipstick": {"price": 60000, "stock":5},
    "Powder": {"price":50000, "stock": 10},
    "Foundation": {"price":70000, "stock":6}
}

#Display available items
def show_items():
    print("-" * 30)
    print("Available Items:")
    print("-" * 30)
    for item, details in items.items():
        print(f"Name: {item}")
        print(f"Price: ${details['price']}")
        print(f"Stock: {details['stock']}")
        print("-" * 15)

# Function to perform a transaction
def purchase_item(item_name, quantity):
    if item_name in items:
        item_details = items[item_name]
        if item_details["stock"] >= quantity:
            # Update stock and calculate total price
            item_details["stock"] -= quantity
            total_price = item_details["price"] * quantity
            profit = item_details["price"] * 0.1 * quantity  # Calculate profit (10% of original price)
            print(f"Successfully purchased {quantity} {item_name}(s) for a total of Rp{total_price}.")
            print(f"Profit: Rp{profit}")
        else:
            print(f"Insufficient stock for {item_name}. Only {item_details['stock']} remaining.")
    else:
        print(f"Item '{item_name}' not found.")

# Function to calculate total transactions and profit
def show_summary():
    total_transactions = 0
    total_profit = 0
    for item_name, details in items.items():
        total_transactions += (items[item_name]["price"] * (items[item_name]["stock"] - details["stock"]))
        total_profit += (items[item_name]["price"] * 0.1 * (items[item_name]["stock"] - details["stock"]))  # Update total profit calculation
    print("-" * 30)
    print("Summary:")
    print("-" * 30)
    print(f"Total Transactions: Rp{total_transactions}")
    print(f"Total Profit: Rp{total_profit}")

# Main program loop
while True:
    print("-" * 30)
    print("Inventory Management System")
    print("-" * 30)
    print("1. Show Available Items")
    print("2. Purchase Item")
    print("3. Show Summary")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        show_items()
    elif choice == '2':
        item_name = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        purchase_item(item_name.capitalize(), quantity)
    elif choice == '3':
        show_summary()
    elif choice == '4':
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please try again.")

print("-" * 30)
print("Program Terminated")