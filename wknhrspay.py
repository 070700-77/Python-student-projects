def computepay(hrs, rte):
    if hrs > 40:
        extra_hours = hrs - 40
        return (40 * rte) + (extra_hours * rte * 1.5)
    else:
        return hrs * rte
try:
    hrs = (float(input("Enter hours: ")))
    rte = (float(input("Enter rate: ")))
except:
    print("Error. Please enter only numeric values: ")
pay = computepay(hrs,rte)
print ("Pay", pay)
    
    