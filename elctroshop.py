print("---------------------------------------------------------------------")
print("")
print("Welcome to UrizaTech's wharehouse and accountability managing system.")
print("")
print("---------------------------------------------------------------------")
#Select the initial ammount of Q
while True:
    try: 
        asuszenbk = (int(input("Provide the initial quantity of Asus Zenbook 16inch  units aviable: ")))
        break
    except:
         print("Please select a valid value")
while True:
    try: 
        iphone16 = (int(input("Provide the initial quantity of Iphone 16 Pro Max 1Tb units aviable: ")))
        break
    except:
        print("Please select a valid value")
while True:
    try: 
        apple_w = (int(input("Provide the initial quantity of Apple AirPods units aviable: ")))
        break
    except:
        print("Please select a valid value")
while True:
    try:
        airpods = (int(input("Provide the initial quantity of units aviable: ")))
        break
    except:
        print("Please select a valid value")
while True:
    try:
        ipadpro = (int(input("Provide the initial quantity of Apple Ipad Pro 1Tb units aviable: ")))
        break
    except:
        print("Please select a valid value")    
print("")
#Main select pannel
print("Select the number of an option.")
print("1). Request intventory and Register a sale.")
print("2). See the total units of inventory sold and delivered. ")
print("3). Go back menu.")
print("0). Turn off the system.")
while True:
    try:
        ans = (int(input("Select an option: ")))
        if ans in [0,1,2,3]:
            break
    except:
        print("Please select a valid option")
print("")
#Define function of sale
def sale (ans3, prompt):
    prompt -= ans3
    sale = prompt
    return sale
total = 0
totalp1 = 0
totalp2 = 0
totalp3 = 0
totalp4 = 0
totalp5 = 0
while ans != 0:
    #Filter answer into options
    if ans == 1:
        print("")
        print("1). Asus Zenbook 16inch")
        print("2). Iphone 16 Pro Max 1Tb")
        print("3). Apple Watch last gen")
        print("4). Apple AirPods")
        print("5). Apple Ipad Pro 1Tb")
        #search for inventory and execute the sale
        while True:
            try:
                ans2 = (int(input("Select the product requested to sale: ")))
                if ans2 in [1,2,3,4,5]:
                    break
                else:
                    print ("Try again and select a valid option")
            except:
                print("Try again and select a valid option")
        while True:
            try:
                ans3 = (int(input("Select the number of units to sale: ")))
                break
            except:
                print("Try again and select a valid option")
        print("")
        if ans2 == 1:
            if ans3 > asuszenbk:
                print("insuficient number of units aviable")
            else:
                asuszenbk = sale (ans3, asuszenbk)
                totalp1 += ans3
                total += ans3
                print("")
                print ("The sale has been registered")
        elif ans2 == 2:
            if ans3 > iphone16:
                print("")
                print("insuficient number of units aviable")
            else:
                iphone16 = sale (ans3, iphone16)
                totalp2 += ans3
                total += ans3
                print("                             ")
                print ("The sale has been registered")
        elif ans2 == 3:
            if ans3 > apple_w:
                print("")
                print("insuficient number of units aviable")
            else:
                apple_w = sale (ans3, apple_w)
                totalp3 += ans3
                total += ans3
                print ("The sale has been registered")
        elif ans2 == 4:
            if ans3 > airpods:
                print("insuficient number of units aviable")
            else:
                airpods = sale (ans3, airpods)
                totalp4 += ans3
                total += ans3
                print("")
                print ("The sale has been registered")
        elif ans2 == 5:
            if ans3 > ipadpro:
                print("insuficient number of units aviable")
            else:
                ipadpro = sale (ans3, ipadpro)
                totalp5 += ans3
                total += ans3
                print("")
                print ("The sale has been registered")
        #Recall option to  buy another product
        print("")
        print("Do you want to add another product to the purchase?: ")
        print("1). Yes")
        print("3). No")
        while True:
            try:
                rebuy = (int(input("Select a numeric option: ")))
                if rebuy == 1:
                    ans = rebuy
                    break
                elif rebuy == 3:
                    ans = rebuy
                    break
                else:
                    print ("The number doesn't represent any product. Please try again.")
            except:
                print ("Please select a valid numeric option and try again.")
    #Dialy sales report
    elif ans == 2:
        print ("----------------------------------------------------------")
        print ("")
        print ("The daily number of today's products units sold is:",total)
        print ("")
        print ("The number of today's Asus Zenbook 16inch units sold is:", totalp1)
        print ("The actual number of units in stock is", asuszenbk)
        if asuszenbk < 20:
            print ("The quantity of units in stock is too low (below 20). Please contact supplyer and restock product.")
        print ("")
        print ("The number of today's Iphone 16 Pro Max 1Tb units sold is:", totalp2)
        print ("The actual number of units in stock is", iphone16)
        if iphone16 < 20:
            print ("The quantity of units in stock is too low (below 20). Please contact supplyer and restock product.")
        print ("")
        print ("The number of today's Apple Watch last gen units sold is:", totalp3)
        print ("The actual number of units in stock is", apple_w)
        if apple_w < 20:
            print ("The quantity of units in stock is too low (below 20). Please contact supplyer and restock product.")
        print ("")
        print ("The number of today's Apple AirPods last gen units sold is:", totalp4)
        print ("The actual number of units in stock is", airpods)
        if airpods < 20:
            print ("The quantity of units in stock is too low (below 20). Please contact supplyer and restock product.")
        print ("")
        print ("The number of today's Apple Ipad Pro 1Tb units sold is:", totalp5)
        print ("The actual number of units in stock is", ipadpro)
        if ipadpro < 20:
            print ("The quantity of units in stock is too low (below 20). Please contact supplyer and restock product.")
        print ("")
        print ("----------------------------------------------------------")
        print("")
        print("Do you want to create a new purchase?: ")
        print("1). Yes")
        print("3). No")
        while True:
            try:
                recall = (int(input("Select a numeric option: ")))
                if recall == 1:
                    ans = recall
                    break
                elif recall == 3:
                    ans = recall
                    break
                else:
                    print ("The number doesn't represent any product. Please try again.")
            except:
                print ("Please select a valid numeric option and try again.")
    #Return option to main select pannel
    elif ans == 3:
        print("")
        print("Select the number of an option.")
        print("1). Request intventory and Register a sale.")
        print("2). See the total units of inventory sold and delivered. ")
        print("3). Go back menu.")
        print("0). Turn off the system.")
        while True:
            try:
                recall = (int(input("Select a numeric option: ")))
                if recall in [0,1,2,3]:
                    ans = recall
                    break
                else:
                    print ("The number doesn't represent any product. Please try again.")
            except:
                print ("Please select a valid numeric option and try again.")
    else:
        print ("please try again and select a valid option")
        ans = 3
#Exit program option
print ("")
print ("You selected option number 0 (Turn off the program). Goodbye")