#test3.txt
#Sistema de try / catch para gestionar cualquier error en el input del usuario
while True:
    fname = input("Enter file name: ")
    try:
        fh = open(fname)
        break
    except:
        print(f"The file {fname} haven't been found. Try again.")
#Se declara la variable que dara la senal cuando se encuentre la linea indicada en el archivo
found = False
scolours = []
#Bucle for que recorre todo el archivo
for line in fh:
    #Condicional que busca dar la senal a la variable anteriormente declarada para que cambie su valor
    if "Tipos de Estrellas" in line:
        #Se cambia el valor de la variable
        found = True
        #Se pasa a la siguiente linea
        continue
    #Condicional que entra en uso cuando la variable ha cambiado de valor
    if found is True:
        # Si encontramos una línea vacía o un título nuevo, salimos de la sección
        if line.strip() == "" or line.startswith("Conceptos Básicos"):
            break
        # Verifica que la línea tenga el formato correcto
        if "|" in line:
            parts = line.split("|") #Divide la linea de texto en una lista de palabras
            if len(parts) >= 3:# Me aseguro de que tenga al menos 3 columnas
                try:
                    class1 = parts[0].strip()# Extrae el tipo de estrella
                    colour = parts[2].strip()# Extrae el color de la estrella
                    scolours.append((class1,colour))# Agrega la tupla a la lista
                except:
                    continue
fh.close()
print(scolours)