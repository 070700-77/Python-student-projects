# test10.txt
# Bucle para solicitar el nombre del archivo hasta que sea válido
while True:
    fname = input("Enter file name: ") # Solicita al usuario el nombre del archivo
    try:
        fh = open(fname, encoding='utf-8') # Intenta abrir el archivo con codificación UTF-8
        break  # Si el archivo se abre correctamente, sale del bucle
    except FileNotFoundError:
        print(f"The file {fname} hasn't been found. Try again.")  # Informa al usuario y repite el bucle
        
# Inicialización de variables
rank = 0  # Contador para el ranking de proveedores
highest_profit_name = None  # Nombre del producto más rentable
highest_profit_q = 0  # Margen de ganancia más alto
lowest_profit = None  # Nombre del producto menos rentable
lowest_profit_q = None  # Margen de ganancia más bajo
name = None  # Nombre temporal del producto
names_list = []  # Lista para almacenar códigos y nombres de productos       
profitability_dict = {}  # Diccionario para almacenar rentabilidad de productos
suppliers_dict = {}  # Diccionario para almacenar datos de proveedores
found00 = False  # Bandera para indicar si se encontró la sección de productos y proveedores
found0 = False  # Bandera para indicar si se encontró la sección de historial de ventas
found1 = False  # Bandera para indicar si se encontró la sección de métricas de proveedores

# Bandera para indicar si se encontró la sección de métricas de proveedores
for line in fh:
    
    # Sección para extraer códigos y nombres de productos
    if "Costo Unitario (USD),Margen de Ganancia (%),Proveedor" in line:
        found00 = True # Activa la bandera para indicar que estamos en la sección relevante
        continue  # Pasa a la siguiente iteración
    elif found00 is True:
        if "## Historial de Ventas Anuales por Producto (2023)" in line:
            found00 =False  # Desactiva la bandera al encontrar el fin de la sección
            continue
        line = line.strip()  # Elimina espacios en blanco al inicio y final
        parts = line.split(",")  # Divide la línea en partes separadas por coma
        if len(parts) > 7:
            code = parts[2]  # Obtiene el código del producto (tercer elemento)
            product = parts[1]  # Obtiene el nombre del producto (segundo elemento)
            names_list.append((code, product))  # Agrega una tupla con el código y nombre a la lista
    
    # Sección para extraer datos de rentabilidad de productos
    elif "Código de Producto,Año,Unidades Vendidas,Ingresos Totales (USD),Costo Total (USD),Ganancia Bruta (USD)" in line:
        found0 = True  # Activa la bandera para indicar que estamos en la sección relevante
        continue  # Pasa a la siguiente iteració
    elif found0 is True:
        if "## Rentabilidad por Categoría de Producto" in line:
            found0 = False  # Desactiva la bandera al encontrar el fin de la sección
            continue
        line = line.strip()
        parts = line.split(",")
        if len(parts) > 5:
            code = parts[0]  # Obtiene el código del producto (primer elemento)
            # Busca el nombre del producto en names_list utilizando el código
            for item in names_list:
                if item[0] == code:
                    name = item[1]  # Asigna el nombre correspondiente al código
                    break # Sale del bucle una vez encontrado
            if name:
                units_sold = int(parts[2])  # Convierte las unidades vendidas a entero
                gross_profit = int(parts[5])  # Convierte la ganancia bruta a entero
                total_cost = int(parts[4])  # Convierte el costo total a entero
                # Calcula el margen de ganancia como un porcentaje
                if total_cost != 0:
                    profit_margin = (gross_profit / total_cost) * 100
                else:
                    profit_margin = 0  # Evita división por cero
                profit_tuple = (units_sold, gross_profit, profit_margin)  # Crea una tupla con los datos
                # Agrega los datos al diccionario de rentabilidad
                profitability_dict[name] = profitability_dict.get(name, profit_tuple)
                
    
    
    
    # Sección para extraer datos de proveedores    
    elif "Tasa de Retrasos (%),Costo Total de Productos (USD)" in line:
        found1 = True  # Activa la bandera para indicar que estamos en la sección relevante
        continue  # Pasa a la siguiente iteración
    elif found1 is True:
        if "## Observaciones Finales" in line:
            found1 = False  # Desactiva la bandera al encontrar el fin de la sección
            continue
        line = line.strip()
        parts = line.split(",")
        if len(parts) > 4:
            supplier = parts[0]  # Nombre del proveedor (primer elemento)
            satisfaction_score = float(parts[2])  # Convierte la puntuación a float
            delay_rate = float(parts[3])  # Convierte la tasa de retrasos a float
            total_product_cost = int(parts[4])  # Convierte el costo total a entero
            supplier_tuple = (satisfaction_score, delay_rate, total_product_cost)  # Crea una tupla con los datos
            # Agrega los datos al diccionario de proveedores
            suppliers_dict[supplier] = suppliers_dict.get(supplier, supplier_tuple)    

# Cierra el archivo después de procesarlo            
fh.close()

# Ordena los proveedores por puntuación en orden descendente
suppliers_list = list(suppliers_dict.items())  # Convierte el diccionario en una lista de tuplas
sorted_list = sorted(suppliers_list, key=lambda item: item[1][0], reverse=True)
sorted_suppliers_dict = dict(sorted_list)  # Convierte la lista ordenada de nuevo a un diccionario

# Imprime los proveedores ordenados por puntuación
print("Proveedores ordenados por puntuación:")
print("")
rank = 0 # Reinicia el contador de ranking
for key, value in sorted_suppliers_dict.items():
    rank += 1  # Incrementa el ranking
    print(f"{rank}. {key}: Puntuación = {value[0]:.1f}, Tasa de Retrasos = {value[1]}%, Costo Total = ${value[2]:,.0f} USD")

    
    
# Ordena los productos por margen de ganancia en orden descendente
profitability_list = list(profitability_dict.items())
sorted_plist = sorted(profitability_list, key=lambda item: item[1][2], reverse=True)
sorted_profitability_dict = dict(sorted_plist)

highest_profit_data = None # Datos del producto más rentable
lowest_profit_data = None  # Datos del producto menos rentable

# Busca el producto más y menos rentable
print("\nProductos más y menos rentables:")
print("")
for key, value in sorted_profitability_dict.items():
    # Actualiza el producto más rentable
    if value[2] > highest_profit_q:
        highest_profit_name = key
        highest_profit_q = value[2]
        highest_profit_data = value
    # Actualiza el producto menos rentable
    if lowest_profit_q is None or value[2] < lowest_profit_q:
        lowest_profit_name = key
        lowest_profit_q = value[2]
        lowest_profit_data = value

# Verifica si se encontraron los productos más y menos rentables y los imprime
if highest_profit_data:
    print(f"Producto más rentable: {highest_profit_name} (Unidades Vendidas = {highest_profit_data[0]}, Ganancia Bruta = ${highest_profit_data[1]:,.0f} USD, Margen de Ganancia = {highest_profit_data[2]:.2f}%)")
else:
    print("No se encontró un producto más rentable.")

if lowest_profit_data:
    print(f"Producto menos rentable: {lowest_profit_name} (Unidades Vendidas = {lowest_profit_data[0]}, Ganancia Bruta = ${lowest_profit_data[1]:,.0f} USD, Margen de Ganancia = {lowest_profit_data[2]:.2f}%)")
else:
    print("No se encontró un producto menos rentable.")