import urllib.request, urllib.parse, urllib.error
# Importamos tres módulos de `urllib`:
# - `urllib.request`: Nos permite abrir URLs y descargar su contenido.
# - `urllib.parse`: Herramientas para analizar o construir URLs (no se usa directamente en este código).
# - `urllib.error`: Maneja errores al intentar abrir URLs (no se usa directamente aquí).

from bs4 import BeautifulSoup
# Importamos `BeautifulSoup` de la biblioteca `bs4`.
# BeautifulSoup es una herramienta que convierte contenido HTML en un formato que Python puede entender.
# Esto nos permite buscar y extraer elementos específicos, como etiquetas `<a>` en el HTML.

import ssl
# Importamos el módulo `ssl`, que se utiliza para manejar conexiones seguras (HTTPS).
# Nos ayudará a ignorar problemas con certificados SSL no válidos.

# Configuración para ignorar errores de certificados SSL.
ctx = ssl.create_default_context()
# Creamos un "contexto SSL" con la configuración predeterminada.

ctx.check_hostname = False
# Configuramos el contexto para que no verifique si el nombre del certificado SSL coincide con el servidor.

ctx.verify_mode = ssl.CERT_NONE
# Configuramos el contexto para ignorar completamente la validación del certificado SSL.
# Esto permite conectarse a sitios HTTPS incluso si tienen certificados no válidos.

# Inicia un bucle para asegurarse de que el usuario ingrese un enlace válido.
while True:
    link = input("Enter link: ") # Solicita al usuario que ingrese un enlace (URL).
    if link == "":
         # Si el usuario no escribe nada (URL vacía), imprimimos un mensaje de error.
        print("Invalid link. Try again")
        continue # Volvemos al inicio del bucle para pedir un enlace nuevamente.
    break  # Si el usuario ingresó un enlace, salimos del bucle.

# Abre la URL ingresada por el usuario y descarga su contenido HTML.
# - `urllib.request.urlopen(link, context=ctx)` se conecta al servidor de la URL usando el contexto SSL configurado.
# - `.read()` lee todo el contenido de la página web y lo guarda en la variable `url` como una cadena de bytes.
url = urllib.request.urlopen(link, context=ctx).read()

# Creamos un objeto BeautifulSoup para analizar el HTML descargado.
# - `url` contiene el contenido HTML de la página.
# - `"html.parser"` indica que usaremos el analizador de HTML integrado en Python.
# Este objeto nos permitirá buscar y extraer información específica del HTML.
soup = BeautifulSoup(url, "html.parser")

# Buscamos todas las etiquetas `<a>` en el documento HTML.
# Las etiquetas `<a>` en HTML representan enlaces (hipervínculos).
# `soup('a')` devuelve una lista con todas las etiquetas `<a>` encontradas en el HTML.
tags = soup('a')

# Recorremos cada etiqueta `<a>` encontrada en el HTML.
for tag in tags:
    # Para cada etiqueta `<a>`, obtenemos el valor de su atributo `href`.
    # - `tag.get('href', None)` busca el atributo `href` dentro de la etiqueta `<a>`.
    # - Si no existe el atributo `href`, devuelve `None`.
    print("LINK: ", tag.get('href', None))
    # Imprimimos el enlace (valor de `href`) o `None` si no hay enlace.
