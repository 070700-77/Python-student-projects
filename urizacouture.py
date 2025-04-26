print("-----------------------------------------------------------------------------")
print("")
print (" Welcome to Uriza Couture Dubai's Boutique accounting & wharehousing system.")
print("")
print("-----------------------------------------------------------------------------")
inventario = {}
total_ventas = 0.0
def registrar_invenatrio ():
    while True:
        try:
            nombre = (str(input("Enter the product name of reference: ")))
            break
        except:
            print ("You enter an invalid name. Try again")  
    while True:
        try:
            categoria = (str(input("Enter the product category of reference (EXAMPLE: Tsirht, pants, socks, ext): ")))
            break
        except:
            print ("You enter an invalid category. Try again")  
    while True:
        try:
            precio = (float(input("Enter the product price per unit: ")))
            break
        except:
            print ("You enter an invalid price. Try again") 
    while True:
        try:
            cantidad = (int(input("Enter the product available quantity of units in stock: ")))
            break
        except:
            print ("You enter an invalid vlue for Q in stock. Try again")
    clave_producto = (nombre, categoria)
    if clave_producto in inventario:
        print ("The product already exist.")
        while True:
            try:
                actualizar = (str(input("Do you wnat to update the available stock for this product?> (yes/no): "))).lower()
                break
            except:
                print("You entered an invalid answer. Please type yes or no as your answer")
        if actualizar == "yes":
            inventario[clave_producto]['cantidad'] += cantidad
        print(f"Stock actualizado para {nombre}, producto de la categoria {categoria}, con {cantidad} unidades.")
    else:
        inventario[clave_producto] = {'precio': precio, 'cantidad':cantidad}
        print(f"The product {nombre} has been aggregated to the category of {categoria} at a unit price of ${precio}. The selected numeber of units added to stock is {cantidad}")
def actualizar_stock():
    while True:
        try:
            nombre = (str(input("Enter the product name of the reference you want to update: ")))
            break
        except:
            print("Yoy have entered an invalid product name. Try again")
    while True:
        try:
            categoria = (str(input("Enter the product category of the reference you want to update (EXAMPLE: Tsirht, pants, socks, ext): ")))
            break
        except:
            print ("You enter an invalid category. Try again")  
    clave_producto = (nombre, categoria)
    if clave_producto in inventario:
        while True:
            try:
                cantidad= (int(input("Enter the product quantity of units in stock to upload on the actual stock: ")))
                break
            except:
                print("You entered a invalid value. Try again")
        inventario[clave_producto]['cantidad'] += cantidad
    else:
        print("Product not found")
def realizar_venta():
    global total_ventas
    while True:
        try:
            nombre = (str(input("Enter the product name of the reference purchased: ")))
            break
        except:
            print("Yoy have entered an invalid product name. Try again")
    while True:
        try:
            categoria = (str(input("Enter the product category of the reference purchased (EXAMPLE: Tsirht, pants, socks, ext): ")))
            break
        except:
            print ("You enter an invalid category. Try again") 
    clave_producto = (nombre, categoria)
    if clave_producto in inventario:
        while True:
            try:
                cantidad= (int(input("Enter the product quantity of units purchased: ")))
                break
            except:
                print("You entered a invalid value. Try again")
        if inventario[clave_producto]['cantidad'] >= cantidad:
            inventario[clave_producto]['cantidad'] -= cantidad
            total = cantidad*inventario[clave_producto]['precio']
            total_ventas += total
            print(f"The sale has been recorded. The final price of the sale is: ${'precio'}")
def consultar_inventario():
    print("")
    print("Actual Stock per product")
    for (nombre, categoria), detalles in inventario.items():
        print (f"Product:{nombre}, Categoria:{categoria}, Precio: {detalles['precio']:.2f}, Unidades en stock:{detalles['cantidad']}")
def mostrar_total_ventas ():
      print(f"The ammount of today's dialy sales is: ${total_ventas}:.2f")
def salir_programa():
    print("")
    print("GOODBYE.")
    exit()
def menu():
    while True:
        print("")
        print("Select the number of the correct option")
        print("")
        print("1). Register new stock")
        print("2). Update available stock")
        print("3). Register a sale")    
        print("4). Print available stock")
        print("5). Print today's dialy sales")
        print("0). Main Menu")
        print("9). Exit program")
        while True:
            try:
                opcion = (int(input("Select an option: ")))
                break
            except:
                print("Invalid option. Try again")
        if opcion == 1:
            registrar_invenatrio()
        elif opcion == 2:
            actualizar_stock()
        elif opcion == 3:
            realizar_venta()
        elif opcion == 4:
            consultar_inventario()
        elif opcion == 5:
            mostrar_total_ventas()
        elif opcion == 9:
            salir_programa()
        elif opcion == 0:
             menu()
        else:
            print("Opción no válida. Intente de nuevo.")
menu()