# test7.txt
while True:
    fname = input("Enter file name: ")
    try:
        fh = open(fname, encoding='utf-8') 
        break
    except FileNotFoundError:
        print(f"The file {fname} hasn't been found. Try again.")

# Inicializa el diccionario para almacenar los costos operativos
op_costs_lib = {}
found = False # Bandera para indicar si se encontró la sección de interés en el archivo


# Itera sobre cada línea del archivo abierto
for line in fh:
     # Busca el encabezado que indica el inicio de la sección "Costos Operativos Desglosados (USD)"
    if "|Costo Promedio Mensual|Costo Total Anual" in line:
        found = True # Activa la bandera al encontrar el encabezado
    elif found is True:
        # Verifica si hemos llegado al final de la sección de interés
        if "## Empleados por Departamento y Salarios" in line:
            break  # Sale del bucle for, ya no necesitamos leer más líneas
        line = line.strip()  # Elimina espacios en blanco al inicio y final de la línea
        parts = line.split("|")  # Divide la línea en partes separadas por '|'
        if len(parts) > 2:
            category = parts[0]  # Obtiene la categoría de costo (primer elemento)
            monthly_op_cost = int(parts[1])  # Convierte el costo promedio mensual a entero (segundo elemento)
            anual_op_cost = monthly_op_cost * 12  # Calcula el costo total anual multiplicando por 12
            costs_data = (monthly_op_cost, anual_op_cost)  # Crea una tupla con los costos
             # Agrega los datos al diccionario, acumulando si la categoría ya existe
            op_costs_lib[category] = op_costs_lib.get(category, ()) + (costs_data)
# Cierra el archivo después de procesarlo
fh.close()

# Convierte el diccionario en una lista de tuplas para poder ordenarlo
costs_list = list(op_costs_lib.items())
# Ordena la lista en orden descendente según el costo total anual (segundo valor en la tupla)
sorted_list = sorted(costs_list, key=lambda item: item[1][1], reverse=True)
# Convierte la lista ordenada de nuevo a un diccionario
sorted_op_costs_lib = dict(sorted_list)

# Imprime las categorías con costos totales anuales mayores a $100,000 USD
print("Costos mayores a $100,000 USD:")
for key, value in sorted_op_costs_lib.items():
    # value es una tupla que contiene otra tupla con (costo mensual, costo anual)
    if value[1] > 100000:
        print(f"- {key}: ${value[1]:,.0f}")  # Imprime la categoría y el costo anual formateado
        
print("IM SUCCESFULL IN ALL AREAS OF MY LIFE. IM WHEALTHY AND SO INTELIGENT")