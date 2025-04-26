#test7.txt
# Bucle para solicitar el nombre del archivo hasta que sea válido
while True:
    fname = input("Enter file name: ")
    try:
        fh = open(fname, encoding='utf-8') 
        break
    except FileNotFoundError:
        print(f"The file {fname} hasn't been found. Try again.")

# Inicializa variables y estructuras de datos
found = False  # Bandera para indicar si se encontró la sección de interés
count = 0 # Contador para enumerar los meses al imprimir
profit_lib = {}  # Diccionario para almacenar las ganancias brutas por mes

# Itera sobre cada línea del archivo abierto
for line in fh:
    # Busca la línea que indica el inicio de la sección "Resumen de Ingresos y Gastos por Mes (2023)"
    if "Ganancia Bruta (USD),Ganancia Neta (USD)" in line:
        found = True  # Activa la bandera al encontrar el encabezado de la tabla
        continue  # Salta a la siguiente iteración, ya que no necesitamos procesar esta línea
    elif found is True:
        # Verifica si hemos llegado al final de la sección de interés
        if "## Detalles de Ventas por Producto y Región" in line:
            break # Sale del bucle for, ya no necesitamos leer más líneas
        line = line.strip()  # Elimina espacios en blanco al inicio y final de la línea
        parts = line.split(",")  # Divide la línea en partes separadas por comas
         # Verifica que la línea tenga suficientes datos (al menos 5 columnas)
        if len(parts) > 4:
            month = parts[0]  # Obtiene el mes (primer elemento de la línea)
            gross_profit = int(parts[4])  # Convierte la ganancia bruta a entero (quinto elemento) 
            # Agrega la ganancia bruta al diccionario, acumulando si el mes ya existe
            profit_lib[month]=profit_lib.get(month,0) + gross_profit
# Cierra el archivo después de procesarlo
fh.close()

# Convierte el diccionario en una lista de tuplas para poder ordenarlo
profit_list = list(profit_lib.items())
# Ordena la lista en orden descendente según la ganancia bruta
list_sorted_profit = sorted(profit_list, key=lambda item: item[1], reverse=True)
# Convierte la lista ordenada de nuevo a un diccionario (opcional en este caso)
sorted_profit_lib = dict(list_sorted_profit)


# Imprime las ganancias brutas ordenadas
print("Ganancias brutas ordenadas:")
for key, value in sorted_profit_lib.items():
    count += 1 # Incrementa el contador para enumerar los meses
    print(f"{count}. {key}: ${value:,.0f}")  # Imprime el número, mes y ganancia bruta formateada