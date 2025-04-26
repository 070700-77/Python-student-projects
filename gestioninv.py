print("Bienvenido.")
try:
    Cacao_polvo = (int(input("Ingrese el numero de stock inicial de cacao en polvo:")))
    Barras_chocolate = (int(input("Ingrese el numero de stock inicial de tabletas de chocolate:")))
    Nibs_cacao = (int(input("Ingrese el numero de stock inicial de nibs de cacao:")))
except:
    print ("Debes ingresar un valor numerico valido")
    quit()
print("Escoja una opcion:")
print("1.) Ingresar unds de inventario al sistema")
print("2.) Registar la rotacion de uns por venta")
print("0.) Salir del programa")
opt = (int(input("Digite el numero de la opcion a seleccionar:")))
#Ingresar nuevo inventario
if opt == 1:
    try:
        cacao_polvo = (int(input("Ingrese el numero de unidades de cacao en polvo:")))
        barras_chocolate = (int(input("Ingrese el numero de unidades de tabletas de chocolate:")))
        nibs_cacao = (int(input("Ingrese el numero de unidades de nibs de cacao:")))
    except:
        print ("Debes ingresar un valor numerico valido")
        quit()
    Total_productos = Cacao_polvo + Barras_chocolate + Nibs_cacao + cacao_polvo + barras_chocolate + nibs_cacao
    #Alerta de bajo nivel de inventario
    if Cacao_polvo < 40:
        cacao_polvo = Cacao_polvo+cacao_polvo
        print ("Reabastecer inventario de cacao en polvo, #unds:",  cacao_polvo)
    elif Barras_chocolate < 40:
        barras_chocolate = Barras_chocolate+barras_chocolate
        print ("Reabastecer inventario de barras de chocolate, #unds:",  barras_chocolate)
    elif Nibs_cacao < 40:
        nibs_cacao = Nibs_cacao+nibs_cacao
        print ("Reabastecer inventario de nibs de cacao, #unds:",  nibs_cacao)
    else:
        print("Total de unidades en inventario:", Total_productos) 
#Venta y rotacion de inventario
elif opt == 2:
    def off (unts, price):
        off = unts*price*0.9
        return("El saldo final con descuento aplicado es de: $", off)
    def fprice(price,unts):
        fprice = price*unts
        return("Precio final: $", fprice)
    def stk(desn, unts):
        stk = desn-unts
        return("El saldo de inventario es:", stk)
    #Seleccion de tipo de producto
    print("Seleccione el producto a rotar:")
    print("1) Barras de chocolate")
    print("2) Cacao en polvo")
    print("3) Nibs de cacao")
    try:
        desn = int(input("Su respuesta: "))
        if desn > 0:
            desn = desn
    except:
        print("No proporcionaste un valor correcto. por favor vuelve a ingresarlos.")
        quit()
    try:
        unts = float(input("Digite el numero de unidades: "))
        price = float(input("Digite el precio unitario: "))
    except:
        print("No proporcionaste un valor correcto. por favor vuelve a ingresarlos.")
        quit()
#Pago y descuento de inventario
    if desn in (1,2,3):
        if desn == 1:
            desn = Barras_chocolate
            barras_chocolate = (int(unts))
            if barras_chocolate > 0:
                print(fprice(price, barras_chocolate))
                if unts > 10:
                    print(off (barras_chocolate, price))
                print(stk(desn, barras_chocolate))
        elif desn == 2: 
            desn = Cacao_polvo
            cacao_polvo = (int(unts))
            if cacao_polvo > 0:
                print(fprice(price, cacao_polvo))
                if unts > 10:
                    print(off (cacao_polvo, price))
                print(stk(desn, cacao_polvo))
        elif desn == 3:
            desn = Nibs_cacao
            nibs_cacao = (int(unts))
            if nibs_cacao > 0:
                print (fprice(price, nibs_cacao))
                if unts > 10:
                    print (off (price, nibs_cacao))
                print (stk(desn, nibs_cacao))
    else:
        print("No ingreso un valor correcto.")
else:
    ("Digita una opcion valida")
    
    


    
    
