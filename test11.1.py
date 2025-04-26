from bs4 import BeautifulSoup
# Importamos la biblioteca `BeautifulSoup`, que forma parte del paquete `bs4`.
# BeautifulSoup es una herramienta que se utiliza para analizar (parsear) documentos HTML o XML.
# Básicamente, convierte un archivo HTML en un formato que Python puede leer y manipular fácilmente.

import urllib.request, urllib.parse, urllib.error
# Aquí importamos tres módulos del paquete `urllib`:
# - `urllib.request`: Permite hacer solicitudes HTTP, como descargar una página web.
# - `urllib.parse`: Sirve para analizar y manipular URLs (aunque aquí no lo usamos directamente).
# - `urllib.error`: Maneja errores que pueden ocurrir cuando intentamos acceder a una URL inválida.

# Bucle infinito que garantiza que el usuario ingrese un enlace válido.
while True:
    lname = input("Enter link") # Solicita al usuario que escriba un enlace web.
    if lname == "":
        # Si el usuario no escribe nada, mostramos un mensaje de error.
        print("Invalid URL. Try again")
        continue  # Volvemos al inicio del bucle para pedir un enlace válido.
    break  # Si el usuario ingresó un enlace, salimos del bucle.

# Aquí obtenemos el contenido HTML de la URL ingresada por el usuario.
# `urllib.request.urlopen(lname)` abre la URL y descarga su contenido.
# `.read()` lee todo el contenido descargado y lo guarda en la variable `html` como una cadena de bytes.    
html = urllib.request.urlopen(lname).read()

# Convertimos el contenido HTML en un objeto BeautifulSoup.
# Esto facilita analizar el documento HTML y extraer información específica.
# - `html` es el contenido que acabamos de leer.
# - `'html.parser'` es el analizador que se usará para interpretar el contenido HTML.
soup = BeautifulSoup(html, 'html.parser')

# Buscamos todas las etiquetas `<a>` en el documento HTML.
# Las etiquetas `<a>` en HTML representan hipervínculos (enlaces).
# `soup('a')` devuelve una lista con todas las etiquetas `<a>` encontradas en el documento.
tags = soup('a')

# Recorremos cada una de las etiquetas `<a>` que encontramos en el HTML.
for tag in tags:
    # Dentro de cada etiqueta `<a>`, buscamos el valor del atributo `href`, que contiene el enlace.
    # Si no hay un atributo `href`, devolvemos `None`.
    print(tag.get('href', None))
    # `tag.get('href', None)` busca el enlace dentro de la etiqueta `<a>`.
    # Si la etiqueta `<a>` tiene un enlace, se imprimirá en la pantalla.
    # Si no tiene un enlace, imprimiremos `None`.