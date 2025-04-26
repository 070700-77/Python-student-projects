print("Bienvenido al sistema de gestion de ventas de la libreria Santiago's Books")
#Declarar variables
libro1 = (float(input("Ingrese el valor del libro 1 (Titulo: Mide lo que importa): ")))
libro2 = (float(input("Ingrese el valor del libro 2 (Titulo: La psicologia del dinero): ")))
libro3 = (float(input("Ingrese el valor del libro 3 (Titulo: Padre rico, padre pobre): ")))
libro4 = (float(input("Ingrese el valor del libro 4 (Titulo: Algebra de Baldor): ")))
libro5 = (float(input("Ingrese el valor del libro 5 (Titulo: Habitos atomicos): ")))
#Definir funcion de descuento
def off(fprice):
    if fprice > 150000:
        off = fprice * 0.8
    else:
        return fprice
#Registrar ventas
print ("Seleccione una opcion valida")
print("1). Registrar una venta")
print("2). Ver el valor total por ventas del dia")
print("3). Salir del programa")
while True:
    try:
        ans = (int(input("Seleccionar la opcion deseada: ")))
        if ans in (1,3):
            break
        else:
            print ("Seleccione una opcion valida")
    except:
        print("Ha seleccionado un valor invalido. Digite nuevamente la opcion deseada")
ventas_dia = 0
fprice = 0
while ans != 3:
    if ans == 1:
        print("Porductos disponibles para vender")
        print("1).Titulo: Mide lo que importa")
        print("2).Titulo: La psicologia del dinero")
        print("3).Titulo: Padre rico, padre pobre")
        print("4).Titulo: Algebra de Baldor")
        print("5).Titulo: Habitos atomicos")
        while True:
            try:
                opcn =(int(input("Seleccione el producto a registrar en la venta: ")))
                if ans in (1,5):
                    break
                else:
                    print ("Seleccione una opcion valida dentro de la lista")
            except:
                print ("Seleccione una opcion valida")
        if opcn == 1:
            Q = (int(input("Cuantas unidades han sido vendidas?: ")))
            fprice += libro1 * Q
            ventas_dia += fprice
        elif opcn == 2:
            Q = (int(input("Cuantas unidades han sido vendidas?: ")))
            fprice += libro2 * Q
            ventas_dia += fprice
        elif opcn == 3:
            Q = (int(input("Cuantas unidades han sido vendidas?: ")))
            fprice += libro3 * Q
            ventas_dia += fprice
        elif opcn == 4:
            Q = (int(input("Cuantas unidades han sido vendidas?: ")))
            fprice += libro4 * Q
            ventas_dia += fprice
        elif opcn == 5:
            Q = (int(input("Cuantas unidades han sido vendidas?: ")))
            fprice += libro5 * Q
            ventas_dia += fprice
        while True:
            try:
                rebuy = (str(input("Quiere agregar otro producto? (si o no): ")))
                break
            except:
                print ("Respuesta invalida. Responda con un si o no (sin mayusculas)")
        if rebuy == "si":
            print("Porductos disponibles para vender")
            print("1).Titulo: Mide lo que importa")
            print("2).Titulo: La psicologia del dinero")
            print("3).Titulo: Padre rico, padre pobre")
            print("4).Titulo: Algebra de Baldor")
            print("5).Titulo: Habitos atomicos")
            while True:
                try:
                    opcn =(int(input("Escoja que otro producto quiere agregar a la venta: ")))
                    if ans in (1,5):
                        break
                    else:
                        print ("Seleccione una opcion valida dentro de la lista")
                except:
                    print ("Seleccione una opcion valida")
        elif rebuy == "no":
            print("el valor final es:", fprice)
            off(fprice)
            print("el valor final con descuento es:", fprice)
            ans = 4
    elif ans == 2:
        print ("El valor de las ventas totales del dia es", ventas_dia)
        print("Escoja una opcion.")
        print("1). Registrar una venta")
        print ("3). Salir del programa")
        while True:
            try:
                ans = (int(input("Seleccionar la opcion deseada: ")))
                if ans in [1,3]:
                    break
                else:
                    print ("Seleccione una opcion valida")
            except:
                print("Ha seleccionado un valor invalido. Digite nuevamente la opcion deseada")
    elif ans == 4:
        print ("Seleccione una opcion valida")
        print("1). Registrar una venta")
        print("2). Ver el valor total por ventas del dia")
        print("3). Salir del programa")
        while True:
            try:
                ans = (int(input("Seleccionar la opcion deseada: ")))
                if ans in (1,3):
                    break
                else:
                    print ("Seleccione una opcion valida")
            except:
                print("Ha seleccionado un valor invalido. Digite nuevamente la opcion deseada")
    else:
        print("has seleccionado una opcion incorrecta. Por favor intentalo de nuevo.")
        try:
            ans = (int(input("Seleccionar la opcion deseada: ")))
            if ans in (1,3):
                break
            else:
                print ("Seleccione una opcion valida")
        except:
            print("Ha seleccionado un valor invalido. Digite nuevamente la opcion deseada")
print("Ha seleccionado la opcion 3 (SALIR DEL PROGRAMA). Hasta luego.")