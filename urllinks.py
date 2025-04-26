# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
# Importamos módulos del paquete `urllib`:
# - `urllib.request`: Permite abrir URLs y descargar su contenido (como páginas web o archivos).
# - `urllib.parse`: Proporciona herramientas para analizar y manipular URLs (aunque no se usa en este programa).
# - `urllib.error`: Maneja posibles errores que ocurren cuando intentamos acceder a una URL inválida.

from bs4 import BeautifulSoup
# Importamos `BeautifulSoup` de la biblioteca `bs4`.
# BeautifulSoup es una herramienta que convierte documentos HTML (o XML)
# en un formato que Python puede leer y manipular fácilmente.

import ssl
# Importamos el módulo `ssl` (Secure Sockets Layer).
# Este módulo se usa para manejar conexiones seguras (https).
# Nos permitirá ignorar problemas con certificados SSL si la URL tiene uno no válido.

# Configuración para ignorar errores de certificados SSL
ctx = ssl.create_default_context()
# Creamos un "contexto" SSL con la función `ssl.create_default_context()`.
# Este contexto define cómo manejar las conexiones HTTPS.

ctx.check_hostname = False
# Desactivamos la verificación del nombre del host en el certificado SSL.
# Esto significa que el programa no comprobará si el nombre del certificado
# coincide con el del servidor.

ctx.verify_mode = ssl.CERT_NONE
# Desactivamos completamente la validación del certificado SSL.
# Esto permite conectarse a servidores HTTPS incluso si tienen un certificado no válido.

# Solicitamos al usuario que ingrese la URL del sitio web que desea analizar.
url = input('Enter - ')
# La función `input()` muestra el mensaje `'Enter - '` y espera a que el usuario escriba algo.
# Lo que el usuario escribe se guarda en la variable `url`.


# Abrimos la URL proporcionada por el usuario y descargamos su contenido.
# `urllib.request.urlopen(url, context=ctx)` abre la URL utilizando el contexto SSL que configuramos.
# `.read()` lee todo el contenido de la página y lo guarda como una cadena de bytes en la variable `html`.
html = urllib.request.urlopen(url, context=ctx).read()

# Convertimos el contenido HTML descargado en un objeto BeautifulSoup.
# Esto facilita la búsqueda y extracción de elementos específicos del HTML.
# - `html` es el contenido de la página web que acabamos de descargar.
# - `'html.parser'` indica que usaremos el analizador de Python para procesar el HTML.
soup = BeautifulSoup(html, 'html.parser')

# Buscamos todas las etiquetas `<a>` en el documento HTML.
# Las etiquetas `<a>` representan enlaces en una página web.
# `soup('a')` devuelve una lista con todas las etiquetas `<a>` encontradas en el HTML.
tags = soup('a')

# Iteramos sobre cada etiqueta `<a>` que encontramos en el HTML.
for tag in tags:
    # Extraemos el atributo `href` de cada etiqueta `<a>`.
    # El atributo `href` contiene el enlace al que apunta la etiqueta.
    # `tag.get('href', None)` busca el atributo `href`.
    # Si la etiqueta `<a>` no tiene un atributo `href`, devuelve `None`.
    print(tag.get('href', None))
    # Imprimimos el valor del atributo `href` (el enlace).
    # Si no hay un enlace, imprimimos `None`.