print ("")
print("------------------------------------------------------")
print ("Welcome to Santiago's burguer shop management system.")
print("------------------------------------------------------")
print ("")
print ("Please enter the product prices")
#Variables para almacenar precio unitario
while True: 
    try: 
        cheeseb = (float(input("Enter the Deluxe cheese burger meal price: ")))
        break
    except:
        print("Please enter a valid value")
while True:
    try:
        chikenb = (float(input("Enter the Chiken wings burger meal price: ")))
        break
    except:
        print("Please enter a valid value")
while True:
    try: 
        biggieb = (float(input("Enter the Notorious B.I.G burguer meal price: ")))
        break
    except:
        print("Please enter a valid value")
while True:
    try:
        icecrm = (float(input("Enter the CISF Ice cream cup price: ")))
        break
    except:
        print("Please enter a valid value")
#Variables para almacenar las ventas totales diarias
total_ammount = 0
sales_by_product = {"cheeseb" : 0,"chikenb" : 0,"biggieb" : 0,"icecrm" : 0}
#definicion de funciones
def main_menu ():
    print("")
    print("MAIN MENU")
    print("Please select the number of an option")
    print("")
    print("1). Check discount & register a sale")
    print("2). Check dialy sales")
    print("3). Turn off the program")
    print("0). Main menu")
def discount (total_purchase):
    if total_purchase >= 120:
        return total_purchase * 0.85
    return total_purchase
def calculate_price (qitem, price):
    return qitem * price

main_menu()    
while True:
    try:
        opt = (int(input("Select the number of the option: ")))
        if opt in (0,1,2,3):
            break
        else:
            print("You have selected a wrong option number. Please Try again.")
            print("")
    except:
        print("You have enter an invalid value. Please try again and write the number of the desired option.")
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
            print("2). Chiken wings burger meal")
            print("3). Notorious B.I.G burguer meal")
            print("4). CISF Ice cream cup")
            print("0). Finish purchase")
            
            try:        
                ans = (int(input("Select the number of the correct option: ")))
                if ans == 0:
                    break
                elif ans in (1,2,3,4):
                    while True:
                        try:
                            qitem = (int(input("Enter the number of units sold: ")))
                            break
                        except:
                            print("You entered an invalid value. please try again.") 
            except:
                print("You have enter an invalid value. Please try again and write the number of the desired option.")
                print("")
            if ans == 1:
                sale_ammount = calculate_price (qitem, cheeseb)
                total_purchase += sale_ammount
                sales_by_product ["cheeseb"] += sale_ammount
                print("Sale registered.")
            elif ans == 2:
                sale_ammount = calculate_price (qitem, chikenb)
                total_purchase += sale_ammount
                sales_by_product ["chikenb"] += sale_ammount
                print("Sale registered.")
            elif ans == 3:
                sale_ammount = calculate_price (qitem, biggieb)
                total_purchase += sale_ammount
                sales_by_product ["biggieb"] += sale_ammount
                print("Sale registered.")
            elif ans == 4:
                sale_ammount = calculate_price (qitem, icecrm)
                total_purchase += sale_ammount
                sales_by_product ["icecrm"] += sale_ammount
                print("Sale registered.")
            else:
                print("You have selected a wrong option number. Please Try again.")
                print("") 
        total_purchase = discount (total_purchase)
        total_ammount += total_purchase 
        print("The total ammount of the sale is:", total_purchase)
        opt = 0
    elif opt == 2 :
        print("")
        print("The final consolidated ammount of dialy sales is:", total_ammount)
        print ("")
        print ("The dialy ammount of Deluxe cheese burguer meal sales is:", sales_by_product ["cheeseb"])
        print ("The dialy ammount of Chiken wings burger meal sales is:", sales_by_product ["chikenb"])
        print ("The dialy ammount of Notorious B.I.G burguer meal sales is:", sales_by_product ["biggieb"])
        print ("The dialy ammount of CISF Ice cream cup sales is:", sales_by_product ["icecrm"])
        print("")
        print ("Do you want to register a new sale?")
        print ("1). YES")
        print ("0). NO")
        while True:
            try:
                opt = (int(input("Select the number of the option: ")))
                if opt in (0,1):
                    break
                else:
                    print("You have selected a wrong option number. Please Try again.")
                    print("")
            except:
                print("You have enter an invalid value. Please try again and write the number of the desired option.")
                print("")
    elif opt == 0:
        main_menu() 
        while True:
            try:
                opt = (int(input("Select the number of the option: ")))
                if opt in (0,1,2,3):
                    break
                else:
                    print("You have selected a wrong option number. Please Try again.")
                    print("")
            except:
                print("You have enter an invalid value. Please try again and write the number of the desired option.")
                print("")
    else:
        ("You have selected a wrong option number. Please Try again.")
print ("You enter the option 3 (TURN OFF THE PROGRAM). Good bye.")