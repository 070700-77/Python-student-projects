print("------------------------------------------------------")
print("Welcome to Santiago's burger shop management system.")
print("------------------------------------------------------")
print("")
print("Please enter the product prices")
cheeseb = float(input("Enter the Deluxe cheese burger meal price: "))
chikenb = float(input("Enter the Chicken wings burger meal price: "))
biggieb = float(input("Enter the Notorious B.I.G burger meal price: "))
icecrm = float(input("Enter the CISF Ice cream cup price: "))

# Variables para almacenar las ventas totales
total_sales = 0
total_cheeseb = 0
total_chikenb = 0
total_biggieb = 0
total_icecrm = 0

def apply_discount(total):
    if total >= 120:
        return total * 0.85
    return total

def main_menu():
    print("")
    print("MAIN MENU")
    print("Please select the number of an option")
    print("")
    print("1). Register a sale")
    print("2). Check daily sales")
    print("3). Turn off the program")
    print("0). Main menu")

def register_sale():
    global total_sales, total_cheeseb, total_chikenb, total_biggieb, total_icecrm
    current_sale = 0
    
    while True:
        print("")
        print("Select the product sold")
        print("1). Deluxe cheese burger meal")
        print("2). Chicken wings burger meal")
        print("3). Notorious B.I.G burger meal")
        print("4). CISF Ice cream cup")
        print("0). Finish sale")
        
        try:
            ans = int(input("Select the number of the correct option: "))
            if ans == 0:
                break
            elif ans not in (1, 2, 3, 4):
                print("Invalid option. Please try again.")
                continue
            
            qitem = int(input("Enter the number of units sold: "))
            
            if ans == 1:
                current_sale += cheeseb * qitem
                total_cheeseb += cheeseb * qitem
            elif ans == 2:
                current_sale += chikenb * qitem
                total_chikenb += chikenb * qitem
            elif ans == 3:
                current_sale += biggieb * qitem
                total_biggieb += biggieb * qitem
            elif ans == 4:
                current_sale += icecrm * qitem
                total_icecrm += icecrm * qitem
            
            print(f"Current sale total: ${current_sale:.2f}")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    final_sale = apply_discount(current_sale)
    total_sales += final_sale
    print(f"Final sale amount (after discount): ${final_sale:.2f}")

def show_daily_sales():
    print("\nDaily Sales Summary:")
    print(f"Total sales: ${total_sales:.2f}")
    print(f"Deluxe cheese burger meal sales: ${total_cheeseb:.2f}")
    print(f"Chicken wings burger meal sales: ${total_chikenb:.2f}")
    print(f"Notorious B.I.G burger meal sales: ${total_biggieb:.2f}")
    print(f"CISF Ice cream cup sales: ${total_icecrm:.2f}")

while True:
    main_menu()
    try:
        opt = int(input("Select the number of the option: "))
        if opt == 1:
            register_sale()
        elif opt == 2:
            show_daily_sales()
        elif opt == 3:
            print("You entered option 3 (TURN OFF THE PROGRAM). Goodbye.")
            break
        elif opt == 0:
            continue
        else:
            print("Invalid option. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")

print("Thank you for using Santiago's burger shop management system.")
