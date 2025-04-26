while True:
    fname = input("Insert file name: ")
    try:
        fh = open(fname, encoding='utf-8')
        break
    except FileNotFoundError:
        print("File hasn't been found. Try again")
        print("")
coincidencias_2 = []
coincidencias = []
        
import re
#Patron para extraer los correos electronicos
patron = r"([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})"
#Patron que extrae los links de los sitios web
patron2 = r"https?://[a-zA-Z0-9.-]+(?:\.[a-zA-Z]{2,})+"


found1 = False
found0 = False

for line in fh:
    if "## Contactos de Empleados y Directivos" in line:
        found0 = True
        continue
    elif found0 is True:
        if "xxx" in line:
            found0 = False
            continue
        line = line.strip()
        coincidencia = re.findall(patron, line)
        if coincidencia:
            coincidencias.extend(coincidencia)
            
            
    elif "## Sitios Web Oficiales" in line:
        found1= True
        continue
    elif found1 is True:
        if "## Identificaciones de Usuarios y Roles" in line:
            found1= False
            continue
        line = line.strip()    
        coincidencia_2 = re.findall(patron2, line)
        if coincidencia_2:
            coincidencias_2.extend(coincidencia_2)
        
        
print(coincidencias)    
print(coincidencias_2)    
