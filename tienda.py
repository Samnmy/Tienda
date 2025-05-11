# inventory_management.py

# Preload the inventory with 5 products
def preload_inventory():
    # List of products (each product is a dictionary)
    inventory = [
        {"name": "Laptop", "category": "Electronics", "supplier": "Supplier A", "quantity": 10, "unit_price": 1200},
        {"name": "Smartphone", "category": "Electronics", "supplier": "Supplier B", "quantity": 5, "unit_price": 700},
        {"name": "Shirt", "category": "Clothing", "supplier": "Supplier C", "quantity": 15, "unit_price": 30},
        {"name": "Shoes", "category": "Clothing", "supplier": "Supplier D", "quantity": 3, "unit_price": 50},
        {"name": "Coffee Maker", "category": "Appliances", "supplier": "Supplier E", "quantity": 0, "unit_price": 80}
    ]
    return inventory

# Function to add a product to the inventory
def add_product(inventory, name, category, supplier, quantity, unit_price):
    # Validate that quantity and unit price are positive
    if quantity < 0 or unit_price < 0:
        print("Error: Quantity and price must be positive values.")
        return
    # Create the product as a dictionary and append it to the inventory
    product = {"name": name, "category": category, "supplier": supplier, "quantity": quantity, "unit_price": unit_price}
    inventory.append(product)
    print(f"Product {name} added successfully.")

# Function to search for products by name or category (case insensitive)
def search_product(inventory, query):
    # Initialize an empty list to store matching products
    results = []
    # Loop through all products and check if the query is in either name or category
    for product in inventory:
        if query.lower() in product["name"].lower() or query.lower() in product["category"].lower():
            results.append(product)
    return results

# Function to update product quantity or unit price
def update_product(inventory, product_name, new_quantity=None, new_price=None):
    # Loop through the inventory to find the product by name
    for product in inventory:
        if product["name"].lower() == product_name.lower():
            # If a new quantity is provided, update it (ensure it's positive)
            if new_quantity is not None and new_quantity >= 0:
                product["quantity"] = new_quantity
            # If a new price is provided, update it (ensure it's positive)
            if new_price is not None and new_price >= 0:
                product["unit_price"] = new_price
            print(f"Product {product_name} updated successfully.")
            return
    print(f"Product {product_name} not found.")

# Function to delete a product if its stock is 0
def delete_product(inventory, product_name):
    # Loop through the inventory to find the product by name
    for product in inventory:
        if product["name"].lower() == product_name.lower():
            # If the product has zero stock, remove it from the inventory
            if product["quantity"] == 0:
                inventory.remove(product)
                print(f"Product {product_name} deleted successfully.")
                return
            else:
                print("Error: Cannot delete product with non-zero stock.")
                return
    print(f"Product {product_name} not found.")

# Function to generate reports
def generate_reports(inventory):
    # Report for total value by category
    category_values = {}
    for product in inventory:
        if product["category"] not in category_values:
            category_values[product["category"]] = 0
        category_values[product["category"]] += product["unit_price"] * product["quantity"]
    
    # Print the total value by category
    print("\nTotal value by category:")
    for category, value in category_values.items():
        print(f"{category}: ${value}")

    # Report for products with minimum stock (threshold = 5)
    print("\nProducts with stock below minimum (threshold = 5):")
    for product in inventory:
        if product["quantity"] < 5:
            print(f"{product['name']} (Stock: {product['quantity']})")

# Main interactive menu function
def menu():
    # Preload the inventory with 5 products
    inventory = preload_inventory()

    while True:
        # Display the menu
        print("\n--- Inventory Management System ---")
        print("1. Add Product")
        print("2. Search Product")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Generate Reports")
        print("6. Exit")
        
        # Get user choice
        choice = input("Enter your choice: ")
        
        if choice == '1':
            # Prompt for product details and add the product
            name = input("Enter product name: ")
            category = input("Enter product category: ")
            supplier = input("Enter product supplier: ")
            quantity = int(input("Enter product quantity: "))
            unit_price = float(input("Enter product unit price: "))
            add_product(inventory, name, category, supplier, quantity, unit_price)

        elif choice == '2':
            # Prompt for a search query and display matching products
            query = input("Enter product name or category to search: ")
            results = search_product(inventory, query)
            if results:
                for result in results:
                    print(f"Product: {result['name']}, Category: {result['category']}, Supplier: {result['supplier']}, Quantity: {result['quantity']}, Price: ${result['unit_price']}")
            else:
                print("No products found.")

        elif choice == '3':
            # Prompt for the product name to update and new values for quantity or price
            product_name = input("Enter product name to update: ")
            new_quantity = int(input("Enter new quantity (or leave blank to skip): ") or -1)
            new_price = float(input("Enter new price (or leave blank to skip): ") or -1)
            update_product(inventory, product_name, new_quantity if new_quantity >= 0 else None, new_price if new_price >= 0 else None)

        elif choice == '4':
            # Prompt for the product name to delete and confirm the deletion
            product_name = input("Enter product name to delete: ")
            confirm = input(f"Are you sure you want to delete {product_name}? (yes/no): ")
            if confirm.lower() == 'yes':
                delete_product(inventory, product_name)

        elif choice == '5':
            # Generate reports
            generate_reports(inventory)

        elif choice == '6':
            # Exit the system
            print("Exiting the inventory management system.")
            break

        else:
            # Handle invalid menu choice
            print("Invalid choice. Please try again.")

# Entry point for the program
if __name__ == "__main__":
    menu()
