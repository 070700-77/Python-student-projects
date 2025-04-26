import urllib.request, urllib.parse, urllib.error
# Aquí importamos módulos del paquete `urllib`:
# - `urllib.request`: Nos permite abrir URLs y descargar su contenido.
# - `urllib.parse` y `urllib.error`: Son herramientas adicionales para trabajar con URLs o manejar errores (aunque no se usan directamente en este programa).

# Creamos un bucle que se repetirá hasta que el usuario ingrese una URL válida.
while True:
    lname = input("Enter link: ") # Solicitamos al usuario que escriba un enlace (URL).
    if lname == "":
        # Si el usuario deja el campo vacío (no escribe nada), mostramos un mensaje de error.
        print("Url not valid. Please try again")
        continue  # Volvemos al inicio del bucle para pedir una URL válida.
    break  # Si el usuario ingresa una URL, salimos del bucle y continuamos con el programa.

# Creamos un diccionario vacío llamado `info` donde almacenaremos las palabras y su conteo.
# Este diccionario funcionará como un "contador de palabras".
info = {}    

# Usamos `urllib.request.urlopen` para abrir la URL ingresada por el usuario.
# Esto descarga el contenido del recurso al que apunta la URL (por ejemplo, una página web o un archivo de texto).
# El contenido descargado se almacena en la variable `fhand`.
fhand = urllib.request.urlopen(lname)

# Entramos en un bucle para procesar cada línea del contenido descargado.
for line in fhand:
    # Las líneas del archivo están en formato de bytes, así que las decodificamos
    # para convertirlas en texto entendible.
    # `.decode()` convierte los bytes en texto.
    # `.strip()` elimina espacios en blanco adicionales al principio y al final de la línea.
    print(line.decode().strip()) # Mostramos en la pantalla cada línea de texto procesada.
    
    # Dividimos la línea en palabras usando `.split()`.
    # Esto crea una lista donde cada palabra de la línea es un elemento.
    words = line.split()
    
    # Iteramos sobre cada palabra en la lista `words`.
    for word in words:
        # Para cada palabra, usamos el método `.get()` para verificar si ya está en el diccionario `info`.
        # - Si la palabra ya está, obtenemos su valor actual (el número de veces que ha aparecido).
        # - Si la palabra no está, `.get()` devuelve `0` (significa que es la primera vez que aparece).
        # Sumamos 1 al conteo actual de la palabra y actualizamos el diccionario.
        info[word] = info.get(word,0)+1
        # Después de procesar todas las palabras de la línea, imprimimos el diccionario `info`.
        # Esto muestra el conteo acumulado de cada palabra hasta este punto.
        
    print(info)  

        