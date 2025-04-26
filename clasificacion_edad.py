def clasification_ages(lang):
    if lang >= 0 and lang <= 2:
        return "Baby"
    elif lang >= 3 and  lang<= 12:
        return "kid"
    elif lang >= 13 and lang <= 17:
        return "teeneager"
    elif lang >= 18 and lang <= 64:
        return "adult"
    elif lang >= 65:
        return ("Grown adult")
dte = (int(input("Insert your age in numbers:")))
category = clasification_ages(dte)
print ("your age clasification is:", category)
