products = []

def list_products():
    if not products:
        print("No products added yet.")
    else:
        print("List of Products:")
        for i, product in enumerate(products, 1):
            print(f"{i}. {product}")

def add_product():
    product_name = input("Enter product name: ")
    products.append(product_name)
    print(f"Product '{product_name}' added successfully.")

def delete_product_by_name():
    if not products:
        print("No products added yet.")
    else:
        product_name = input("Enter the name of the product to delete: ")
        if product_name in products:
            products.remove(product_name)
            print(f"Product '{product_name}' deleted successfully.")
        else:
            print("Product not found.")
            
def delete_by_id():
    if not products:
        print("No products added yet.")
    else:
        product_id = int(input("Enter the ID of the product to delete: "))
        if 0 < product_id <= len(products):
            deleted_product = products.pop(product_id - 1)
            print(f"Product '{deleted_product}' deleted successfully.")
        else:
            print("Invalid ID.")

def main():
    while True:
        print("\nMenu:")
        print("1. List products")
        print("2. Add product")
        print("3. Delete name of product")
        print("4. Delete by ID")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            list_products()
        elif choice == '2':
            add_product()
        elif choice == '3':
            delete_product_by_name()
        elif choice == '4':
            delete_by_id()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
