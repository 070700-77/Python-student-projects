#Final test: It works with the file named 'test7.txt'

# Bucle infinito para solicitar al usuario el nombre del archivo
while True:
    fname = input("Enter file name: ")
    try:
        # Intenta abrir el archivo con codificación UTF-8
        fh = open(fname, encoding='utf-8') 
        break # Si el archivo se abre correctamente, sale del bucle
    except FileNotFoundError:
        # Si no se encuentra el archivo, muestra un mensaje y pide nuevamente el nombre
        print(f"The file {fname} hasn't been found. Try again.")

# Inicializa diccionarios y variables necesarias
monthly_revenue_average = {}
highest_average = {}

found= False # Indicador para saber cuándo comenzar a leer los datos relevantes
total_revenue = 0 # Acumulador para la rentabilidad total

# Bucle for que lee cada línea del archivo
for line in fh:
    # Busca la línea que contiene los encabezados de los dato
    if "Gastos de Capital (USD),Ganancia Bruta (USD),Ganancia Neta (USD)" in line:
        found = True # Señala que los siguientes datos son relevantes
        continue # Continúa con la siguiente iteración
    elif found is True:
        # Si encuentra la sección que indica el final de los datos relevantes, sale del bucle
        if "## Detalles de Ventas por Producto y Región" in line:
            break
        line = line.strip() # Elimina espacios en blanco al inicio y al final
        parts = line.split(",") # Elimina espacios en blanco al inicio y al final
        if len(parts) > 5:
            month = parts[0] # Obtiene el mes
            net_revenue = int(parts[5]) # Convierte la ganancia neta a entero
            income = int(parts[1]) # Convierte los ingresos a entero
            # Calcula la rentabilidad mensual en porcentaje
            monthly_revenue = ((net_revenue/income)*100)
            # Almacena la rentabilidad mensual en el diccionario
            monthly_revenue_average[month] = monthly_revenue_average.get(month,0) + monthly_revenue
            # Suma la rentabilidad mensual al total
            total_revenue += monthly_revenue_average[month]
fh.close()# Cierra el archivo

print("Rentabilidad mensual por mes:")
#Bucle que accede directamente a clave y valor en cada iteración, simplificando el acceso a ambos.
for month, value in monthly_revenue_average.items():
    print(f"{month}: {value:.2f}%") #Se imprime la clave y el valor de la clave de cada interaccion . (:.2f) -> Esta funcion se asegura que solo se impriman dos digitos de los numeros decimales
print("")

# Inicializa variables para encontrar el mes con mayor rentabilidad
key = None
value_total = 0
# Recorre el diccionario de rentabilidad mensual
for month, value in monthly_revenue_average.items():
    if value > value_total:
        value_total = value # Actualiza el mayor valor encontrado
        key = month # Guarda el mes correspondiente
# Imprime el mes con mayor rentabilidad y su porcentaje. (:.2f) -> Esta funcion se asegura que solo se impriman dos digitos de los numeros decimales
print(f"Mes con mayor rentabilidad: {key} ({value_total:.2f}%)")
print("")

# Calcula el promedio anual de rentabilidad
average_revenue = total_revenue/12
# Imprime el promedio de rentabilidad anual
print(f"Promedio de rentabilidad anual: {average_revenue:.2f}%")
print("")

# Bucle for que identifica los meses con rentabilidad superior al promedio anual
for month, value in monthly_revenue_average.items():
    if value > average_revenue:
        # Almacena estos meses en un nuevo diccionario
        highest_average[month] = highest_average.get(month, 0) + value

print("Meses con rentabilidad superior al promedio anual:")
# Bucle que imprime los meses con rentabilidad superior al promedio anual
for month, value in highest_average.items():
    print(f'{month}: {value:.2f}%')