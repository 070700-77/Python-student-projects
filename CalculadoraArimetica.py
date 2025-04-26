var1 = float((input("ingresa el primer numero: ")))
var2 = float((input("ingresa el segundo numero: ")))
print ("Selecciona la operacion que quieras realizar")
print ("1). Suma")
print ("2). Resta")
print ("3). multiplicacion")
print ("4). Division")
seleccion = int(input ("ingresa la opcion que prefieras: "))
if seleccion in [1,2,3,4]: 
    if seleccion == 1: 
        suma = var1+var2
        print ("La respuesta es: ", suma)
    elif seleccion == 2: 
        resta = var1-var2
        print ("La respuesta es: ", resta)
    elif seleccion == 3:
        multiplicacion = var1*var2
        print ("La respuesta es: ", multiplicacion)
    elif seleccion == 4:
        if var1 == 0:
            print ("DEBE ESCOGER UN NUMERO DIFERENTE AL 0")
        elif var2 == 0:
            print ("DEBE ESCOGER UN NUMERO DIFERENTE AL 0")
        else:
            division = var1/var2
            print ("La respuesta es: ", division)
else: 
    print ("Has escogido un numero equivocado")
        
        
        