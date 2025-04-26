print ("")
print("------------------------------------------------------")
print ("Welcome to Santiago's burger shop management system.")
print("------------------------------------------------------")
print ("")
print ("Please enter the product prices")
# Variables para almacenar precio unitario
while True: 
    try: 
        cheeseb = float(input("Enter the Deluxe cheese burger meal price: "))
        break
    except:
        print("Please enter a valid value")
while True:
    try:
        chikenb = float(input("Enter the Chicken wings burger meal price: "))
        break
    except:
        print("Please enter a valid value")
while True:
    try: 
        biggieb = float(input("Enter the Notorious B.I.G burger meal price: "))
        break
    except:
        print("Please enter a valid value")
while True:
    try:
        icecrm = float(input("Enter the CISF Ice cream cup price: "))
        break
    except:
        print("Please enter a valid value")

# Variables para almacenar las ventas totales diarias
total_sales = 0
sales_by_product = {"cheeseb": 0, "chikenb": 0, "biggieb": 0, "icecrm": 0}

# Definición de funciones
def main_menu():
    print("")
    print("MAIN MENU")
    print("Please select the number of an option")
    print("")
    print("1). Check discount & register a sale")
    print("2). Check daily sales")
    print("3). Turn off the program")
    print("0). Main menu")

def discount(total):
    if total >= 120:
        return total * 0.85
    return total

def calculate_price(qitem, price):
    return qitem * price

main_menu()

while True:
    try:
        opt = int(input("Select the number of the option: "))
        if opt in (0, 1, 2, 3):
            break
        else:
            print("You have selected a wrong option number. Please try again.")
            print("")
    except:
        print("You have entered an invalid value. Please try again and write the number of the desired option.")
        print("")

# Ciclo principal
while opt != 3:
    if opt == 1:
        total_purchase = 0
        while True:
            print("")
            print("Select the product sold")
            print("")
            print("1). Deluxe cheese burger meal")
            print("2). Chicken wings burger meal")
            print("3). Notorious B.I.G burger meal")
            print("4). CISF Ice cream cup")
            print("0). Finish purchase")
            
            try:
                ans = int(input("Select the number of the correct option: "))
                if ans == 0:
                    break
                elif ans in (1, 2, 3, 4):
                    qitem = int(input("Enter the number of units sold: "))
                    if ans == 1:
                        sale_amount = calculate_price(qitem, cheeseb)
                        total_purchase += sale_amount
                        sales_by_product["cheeseb"] += sale_amount
                    elif ans == 2:
                        sale_amount = calculate_price(qitem, chikenb)
                        total_purchase += sale_amount
                        sales_by_product["chikenb"] += sale_amount
                    elif ans == 3:
                        sale_amount = calculate_price(qitem, biggieb)
                        total_purchase += sale_amount
                        sales_by_product["biggieb"] += sale_amount
                    elif ans == 4:
                        sale_amount = calculate_price(qitem, icecrm)
                        total_purchase += sale_amount
                        sales_by_product["icecrm"] += sale_amount
                else:
                    print("You have selected a wrong option number. Please try again.")
            except:
                print("You have entered an invalid value. Please try again.")

        # Aplicar descuento y actualizar las ventas diarias
        total_purchase = discount(total_purchase)
        total_sales += total_purchase
        print(f"The final amount of the purchase is: {total_purchase}")

    elif opt == 2:
        print("")
        print(f"The final consolidated amount of daily sales is: {total_sales}")
        print(f"The daily amount of Deluxe cheese burger meal sales is: {sales_by_product['cheeseb']}")
        print(f"The daily amount of Chicken wings burger meal sales is: {sales_by_product['chikenb']}")
        print(f"The daily amount of Notorious B.I.G burger meal sales is: {sales_by_product['biggieb']}")
        print(f"The daily amount of CISF Ice cream cup sales is: {sales_by_product['icecrm']}")
        print("")

    elif opt == 0:
        main_menu()

    try:
        opt = int(input("Select the number of the option: "))
        if opt not in (0, 1, 2, 3):
            print("You have selected a wrong option number. Please try again.")
            print("")
    except:
        print("You have entered an invalid value. Please try again and write the number of the desired option.")

print("You entered the option 3 (TURN OFF THE PROGRAM). Goodbye.")
