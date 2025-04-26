#test3.txt
#Sistema de try / catch para gestionar cualquier error en el input del usuario
while True:
    fname = input("Enter file name: ")
    try:
        fh = open(fname)
        break
    except:
        print(f"The file {fname} haven't been found. Try again.")
#Se declara variable que va a guardar el resultado
moons = 0
#Se declara variable que va a dar la senal cuando encuentre la linea indicada en el archivo
found_section = False
#Bucle for que va a recorrer todo el archivo
for line in fh:
    line = line.strip()# Elimina espacios en blanco al inicio y al final
    #condicional que va a validar que se encontro la linea indicada en el archivo
    
    if "Planetas del Sistema Solar" in line:
        #Se cambia el valor de la variable encargada de dar senal
        found_section = True
        continue# Pasa a la siguiente línea después de encontrar la sección

    #Condicional que busca un cambio en el valor de la variable anterior
    # Empieza a procesar solo después de encontrar la sección correcta
    if found_section is True:
        # Verifica si la línea contiene datos de un planeta
        if "|" in line:
            parts = line.split("|")# Divide la línea en partes usando el delimitador '|'
            
            # Condicional para asegúrarme de que tiene suficientes columnas antes de intentar acceder
            if len(parts) > 3:
                try:
                    # Extrae el número de lunas y conviértelo a entero
                    moon = int(parts[3].strip())
                    moons += moon
                except:
                    # Ignora cualquier línea donde el número de lunas no sea válido
                    continue
fh.close()
# Imprime el total de lunas
print(f"Total moons in solar system: {moons}")
        