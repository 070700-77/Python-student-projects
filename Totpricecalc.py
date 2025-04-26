price = (float(input("Put th price: ")))
if price >= 100000:
    total = price*0.9
    print ("The total is:",total)
else:
    print ("If you buy more than $100.000, you have a 10% discount")
    print ("would you like to add something else?: ")
    print ("1) Yes")
    print ("2) no")
    rebuy = (int(input("Digit the number -> ")))
    if rebuy == 1:
        price2 = (float(input("Put the price: ")))
        pricef = price*price2
        if pricef >= 100000:
            total2 = pricef*0.9
            print ("The total is: ", pricef)
        else:
            print ("Good bye")
    else:
        print ("Good bye")
    