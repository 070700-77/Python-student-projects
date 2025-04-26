def get_initial_inventory(product_name):
    while True:
        try:
            return int(input(f"Provide the initial quantity of {product_name} units available: "))
        except ValueError:
            print("Please select a valid value")

def process_sale(product_name, current_stock, total_sales):
    while True:
        try:
            units_sold = int(input(f"Enter the number of units sold for {product_name}: "))
            if units_sold > current_stock:
                print("Insufficient stock available.")
            else:
                current_stock -= units_sold
                total_sales += units_sold
                return current_stock, total_sales
        except ValueError:
            print("Please select a valid number")

def menu():
    options = {
        1: "Request inventory and Register a sale",
        2: "See the total units of inventory sold and delivered",
        3: "Go back menu",
        0: "Turn off the system"
    }
    
    for key, value in options.items():
        print(f"{key}). {value}")
    
    while True:
        try:
            choice = int(input("Select a numeric option: "))
            if choice in options:
                return choice
            else:
                print("Please select a valid option")
        except ValueError:
            print("Please select a valid numeric option")

def print_inventory_report(products):
    print("\n--- Today's Inventory Report ---")
    for product, details in products.items():
        print(f"{product}: Sold {details['sales']} | Stock Left: {details['stock']}")
    print("-------------------------------\n")

def main():
    products = {
        "Asus Zenbook 16inch": {"stock": 0, "sales": 0},
        "Iphone 16 Pro Max 1Tb": {"stock": 0, "sales": 0},
        "Apple Watch": {"stock": 0, "sales": 0},
        "Apple AirPods": {"stock": 0, "sales": 0},
        "Apple Ipad Pro 1Tb": {"stock": 0, "sales": 0}
    }

    for product in products:
        products[product]["stock"] = get_initial_inventory(product)
    
    while True:
        choice = menu()
        if choice == 1:
            for product in products:
                products[product]["stock"], products[product]["sales"] = process_sale(product, products[product]["stock"], products[product]["sales"])
        elif choice == 2:
            print_inventory_report(products)
        elif choice == 3:
            continue
        elif choice == 0:
            print("Shutting down the system...")
            break

if __name__ == "__main__":
    main()