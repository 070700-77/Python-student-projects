from bs4 import BeautifulSoup
# Importamos `BeautifulSoup` de la biblioteca `bs4`.
# Esta herramienta convierte contenido HTML en un formato que Python puede leer y manipular.
# Nos permitirá buscar y extraer las etiquetas `<span>` del HTML.

import urllib.request, urllib.parse, urllib.error
# Importamos módulos de `urllib`:
# - `urllib.request`: Para abrir y descargar páginas web.
# - `urllib.parse` y `urllib.error`: Herramientas adicionales para trabajar con URLs y manejar errores (aunque no se usan directamente aquí).

import ssl
# Importamos el módulo `ssl` (Secure Sockets Layer).
# Esto nos permitirá ignorar problemas con certificados de seguridad (SSL) en conexiones HTTPS.

count = 0
# Inicializamos la variable `count` en 0.
# Esta variable será utilizada para acumular (sumar) los números extraídos de las etiquetas `<span>`.

# Configuración para ignorar errores de certificados SSL.
ctx = ssl.create_default_context()
# Creamos un "contexto" SSL que define cómo manejar las conexiones HTTPS.
ctx.check_hostname = False
# Desactivamos la verificación del nombre del servidor en el certificado SSL.
ctx.verify_mode =ssl.CERT_NONE
# Desactivamos completamente la validación del certificado SSL, permitiendo conexiones con sitios que tienen certificados no válidos.

# Solicitamos al usuario que ingrese un enlace (URL).
while True: # Este bucle se repetirá hasta que el usuario ingrese un enlace válido.
    lname = input("Enter link: ")  # Mostramos el mensaje para que el usuario escriba un enlace.
    if lname == "":
        print("Invalid link. Try again please.") # Si el usuario deja el campo vacío, imprimimos un mensaje de error.
        print("")
        continue  # Volvemos al inicio del bucle para pedir el enlace nuevamente.
    break  # Si el usuario ingresa un enlace, salimos del bucle y continuamos.
    
# Abrimos la URL ingresada por el usuario y descargamos su contenido.
# `urllib.request.urlopen(lname, context=ctx)` abre la URL con el contexto SSL configurado.
# `.read()` lee todo el contenido de la página web y lo guarda como una cadena de bytes en `fhandle`.   
fhandle = urllib.request.urlopen(lname, context = ctx).read()

# Usamos BeautifulSoup para analizar (parsear) el contenido HTML descargado.
# Esto convierte el HTML en un objeto que facilita buscar y extraer etiquetas específicas.
# - `fhandle` contiene el HTML descargado.
# - `'html.parser'` indica que utilizamos el analizador HTML incorporado de Python.
soup = BeautifulSoup(fhandle, 'html.parser')

# Buscamos todas las etiquetas `<span>` en el documento HTML.
# `soup('span')` encuentra todas las etiquetas `<span>` y devuelve una lista de objetos BeautifulSoup.
tags = soup('span')

# Recorremos cada etiqueta `<span>` encontrada en el HTML.
for tag in tags:
    # Extraemos el contenido (texto) de la etiqueta `<span>` usando `tag.text`.
    # Por ejemplo, si la etiqueta es `<span>123</span>`, `tag.text` devolverá la cadena `"123"`.
    number_str = tag.text
    
    # Convertimos el texto extraído (cadena) a un número entero usando `int()`.
    # Por ejemplo, `"123"` se convierte en `123`.
    number = int(number_str)
    
    # Sumamos el número al acumulador `count`.
    # Cada vez que encontramos un número en una etiqueta `<span>`, lo agregamos al total.
    count += number
    
# Después de procesar todas las etiquetas `<span>`, imprimimos el resultado final.
# `count` contiene la suma de todos los números encontrados en las etiquetas `<span>`. 
print(count)
    
    