# test7.txt
# Bucle infinito para solicitar al usuario el nombre del archivo hasta que se encuentre
while True:
    fname = input("Enter file name: ") # Pide al usuario que ingrese el nombre del archivo
    try:
        fh = open(fname, encoding='utf-8') # Intenta abrir el archivo con codificación UTF-8
        break # Si el archivo se abre correctamente, sale del bucle
    except FileNotFoundError:
        print(f"The file {fname} hasn't been found. Try again.")

        
# Inicializa una bandera para indicar si hemos encontrado la sección de interés
found = False
# Crea un diccionario vacío para almacenar los datos de inversiones y ROI
roi_lib = {}

# Itera sobre cada línea del archivo
for line in fh:
    # Verifica si la línea actual contiene el encabezado de la sección que nos interesa
    if "ROI (%)|Retorno Estimado (USD)" in line:
        found = True # Activa la bandera para comenzar a procesar las líneas siguientes
        continue # Salta a la siguiente iteración del bucle
    elif found is True:
         # Verifica si hemos llegado al final de la sección de interés
        if "Informe elaborado para fines internos y análisis estratégico." in line:
            break  # Sale del bucle for, ya no necesitamos procesar más líneas
        line = line.strip()  # Elimina espacios en blanco al inicio y final de la línea
        parts = line.split("|")  # Divide la línea en partes separadas por '|'
        if len(parts) > 3:
            investment = int(parts[1]) # Convierte el monto invertido a entero
            roi = int(parts[2])  # Convierte el ROI (%) a entero
            expected_ammount = int(parts[3])
            category= parts[0]  # Obtiene la categoría de inversión
            data = (roi, investment, expected_ammount)  # Crea una tupla con los datos
            # Agrega los datos al diccionario, manejando posibles múltiples entradas por categoría
            roi_lib [category] = roi_lib.get(category,()) + (data,)
# Cierra el archivo después de procesarlo
fh.close()

# Convierte los items del diccionario a una lista para poder ordenarlos
items = list(roi_lib.items())
# Ordena la lista en orden descendente basándose en el ROI del primer elemento de cada categoría
items_sorted = sorted(items, key=lambda item: item[1][0][0], reverse=True)
# Convierte la lista ordenada de nuevo a un diccionario
roi_lib_sorted = dict(items_sorted)

# Imprime el resultado ordenado
print("Inversiones ordenadas por ROI:")
for category, values in roi_lib_sorted.items():
    for value in values:
        print(f"{category}: ROI = {value[0]}%, Monto Invertido = {value[1]:,.2f} USD, Retorno Estimado = {value[2]:,.2f} USD")