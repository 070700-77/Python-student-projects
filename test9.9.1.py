# test10.txt
# Bucle para solicitar el nombre del archivo hasta que sea válido
while True:
    fname = input("Insert file name: ")
    try:
        fh = open(fname, encoding='utf-8')
        break
    except FileNotFoundError:
        print("File hasn't been found. Try again")
        print("")

# Inicialización de estructuras de datos y variables
product_info_list = [] # Lista para almacenar tuplas de código y nombre de productos
product_info_dict = {} # Diccionario para almacenar información detallada de productos
        

profitability_dict = {}  # Diccionario para almacenar rentabilidad por categoría        
suppliers_dict = {}  # Diccionario para almacenar datos de proveedores

# Banderas para controlar la lectura de diferentes secciones del archivo
found0 = False # Bandera para la sección de proveedores
found1 = False  # Bandera para la sección de rentabilidad por categoría
found2 =  False  # Bandera para la sección de información de productos
found2a = False  # Bandera para la sección de historial de ventas de productos
rank = 0 # Variable para numerar rankings en la salida

# Itera sobre cada línea del archivo abierto
for line in fh:
    
    # Sección para obtener códigos y nombres de productos
    if "Categoría,Producto,Código,Stock,Precio Unitario (USD),Costo Unitario (USD),Margen de Ganancia (%),Proveedor" in line:
        found2 = True # Activa la bandera para indicar que estamos en la sección relevante
    elif found2 is True:
        if "## Historial de Ventas Anuales por Producto" in line:
            found2 = False  # Desactiva la bandera al llegar al final de la sección
            continue  # Continúa con la siguiente línea
        line = line.strip()  # Elimina espacios en blanco al inicio y final de la línea
        parts = line.split(",")  # Divide la línea en partes separadas por comas
        if len(parts) > 7:
            code = parts[2]  # Obtiene el código del producto (tercera columna
            product_name = parts[1]  # Obtiene el nombre del producto (segunda columna)
            product_name_tuple = (code, product_name)  # Crea una tupla con el código y nombre
            product_info_list.append(product_name_tuple)  # Agrega la tupla a la lista de información de productos
    
    # Sección para obtener información de ventas de productos
    elif "Código de Producto,Año,Unidades Vendidas,Ingresos Totales (USD),Costo Total (USD),Ganancia Bruta (USD)" in line:
        found2a = True  # Activa la bandera para indicar que estamos en la sección de ventas de productos
        continue
    elif found2a is True:
        if "## Rentabilidad por Categoría de Producto" in line:
            found2a = False  # Desactiva la bandera al llegar al final de la sección
            continue
        line = line.strip()
        parts = line.split(",")
        if len(parts) > 5:
            code = parts[0]  # Obtiene el código del producto
            # Busca el nombre del producto correspondiente al código
            for item in product_info_list:
                if code == item[0]:
                    name = item[1]
                    break # Sale del bucle una vez encontrado el nombre
                    
            sold_units = int(parts[2])  # Convierte las unidades vendidas a entero
            total_sales_income = int(parts[3])  # Convierte los ingresos totales a entero
            total_sales_cost = int(parts[4])  # Convierte el costo total a entero
            gross_profit = int(parts[5])  # Convierte la ganancia bruta a entero
            
            # Calcula el margen de ganancia bruta como porcentaje
            gross_profit_margin = ((total_sales_income - total_sales_cost)/total_sales_cost)*100
            # Crea una tupla con la información del producto
            product_info_tuple = (sold_units, total_sales_income, total_sales_cost, gross_profit, gross_profit_margin)
            # Agrega la información al diccionario usando el nombre del producto como clave
            product_info_dict[name] = product_info_dict.get(name, ()) + product_info_tuple
    
     # Sección para obtener datos de rentabilidad por categoría
    elif "Categoría,Ingresos Totales (USD),Costo Total (USD),Ganancia Bruta (USD),Margen Bruto (%)" in line:
        found1 = True  # Activa la bandera para indicar que estamos en la sección relevante 
        continue
    elif found1 is True:
        if "## Proveedores con Métricas de Rendimiento" in line:
            found1 = False  # Desactiva la bandera al llegar al final de la sección
            continue
        line = line.strip()
        parts = line.split(",")
        if len(parts) > 4:
            
            category = parts[0]  # Obtiene la categoría
            total_income= int(parts[1])  # Convierte los ingresos totales a entero
            total_cost = int(parts[2])  # Convierte el costo total a entero
            gross_profit = int(parts[3])  # Convierte la ganancia bruta a entero
            gross_profit_margin = float(parts[4])  # Convierte el margen bruto a flotante
            
            
            projected_income = total_income*1.10 # Calcula los ingresos proyectados con un aumento del 10%
            projected_gross_profit_margin =(gross_profit/projected_income)*100  # Calcula el margen bruto proyectado
            # Crea una tupla con los datos de rentabilidad
            category_tuple = (total_income, projected_income, gross_profit_margin, projected_gross_profit_margin)
            # Agrega la información al diccionario usando la categoría como clave
            profitability_dict[category] = profitability_dict.get(category, ()) + category_tuple
            
    
    # Sección para obtener datos de proveedores
    elif "Tasa de Retrasos (%),Costo Total de Productos (USD)" in line:
        found0 = True  # Activa la bandera para indicar que estamos en la sección de proveedores
        continue
    elif found0 is True:
        if "## Observaciones Finales" in line:
            break # Sale del bucle ya que hemos llegado al final de los datos necesarios
        line = line.strip()
        parts = line.split(",")
        if len(parts) > 4:
            
            supplier = parts[0]  # Obtiene el nombre del proveedor
            products_supplied = int(parts[1])  # Convierte la cantidad de productos suministrados a entero
            satisfaction_score = float(parts[2])  # Convierte la puntuación de satisfacción a flotante
            delay_rate =int(parts[3]) # Convierte la tasa de retrasos a entero
            total_products_cost = int(parts[4])  # Convierte el costo total de productos a entero
            
            # Calcula el costo promedio por producto
            average_product_cost = total_products_cost/products_supplied
            # Crea una tupla con los datos del proveedor y Agrega la información al diccionario usando el nombre del proveedor como clave
            suppliers_dict[supplier] = suppliers_dict.get(supplier, ()) + (products_supplied, satisfaction_score, delay_rate, average_product_cost)

# Cierra el archivo después de procesarl           
fh.close()

# Ordena las categorías por margen bruto actual en orden descendente
profitability_list = list(profitability_dict.items())  # Convierte el diccionario en una lista de tuplas
sorted_list = sorted(profitability_list, key=lambda item: item[1][2], reverse=True)
sorted_profitability_dict = dict(sorted_list) # Convierte la lista ordenada de nuevo a un diccionario
# Imprime la comparación de rentabilidad por categoría
print("------------------------------------------")
print("Comparación de rentabilidad por categoría:")
print("")
 # Muestra los ingresos actuales y proyectados, y los márgenes brutos actuales y proyectados
for key, value in sorted_profitability_dict.items():
    print(f"- {key}\nIngresos Actuales = ${value[0]:,} USD, Ingresos Proyectados = ${value[1]:,.0f} USD\nMargen Bruto Actual = {value[2]}%, Margen Bruto Proyectado = {value[3]:.2f}%")

# Ordena los proveedores por tasa de retrasos en orden ascendente
suppliers_list = list(suppliers_dict.items())
sorted_list = sorted(suppliers_list, key=lambda item: item[1][2], reverse = False)
sorted_suppliers_dict = dict(sorted_list)
print("-------------------------------------------")
print("Proveedores ordenados por tasa de retrasos:")
print("")

for key, value in sorted_suppliers_dict.items():
    rank += 1# Incrementa el ranking
    # Muestra el proveedor con su tasa de retrasos y costo promedio por producto
    print(f"{rank}. {key}: Tasa de Retrasos = {value[2]}%, Costo Promedio = ${value[3]:,.0f} USD")

# Identifica productos de baja rotación y calcula plan de optimización
print("--------------------------------------------------")
print("Productos de baja rotación y plan de optimización:")
print("")

for key, value in product_info_dict.items():
    if value[0] < 100:
        unit_price = value[1]/value[0]
        necessary_quantity = (50000 - value[1])/unit_price
        print(f"-{key}\nUnidades Actuales = {value[0]}, Margen de Ganancia = {value[4]:.2f}%\nUnidades Necesarias para Optimizar = {necessary_quantity:.0f}")

        

product_profitability_list = list(product_info_dict.items())
sorted_list = sorted(product_profitability_list, key=lambda item: item[1][4], reverse=True)
sorted_product_info_dict = dict(sorted_list)

print("--------------------------------------------------")
print("Productos ordenados por margen de ganancia:")
print("")

rank = 0
for key, value in sorted_product_info_dict.items():
    rank +=1
    print(f"{rank}. {key}: Margen = {value[4]:.2f}%, Ganancia Bruta = ${value[3]:,.0f} USD")