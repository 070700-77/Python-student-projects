# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
# Importamos `urlopen` del módulo `urllib.request`.
# `urlopen` se utiliza para abrir URLs y descargar su contenido (como una página web o un archivo).

from bs4 import BeautifulSoup
# Importamos `BeautifulSoup` de la biblioteca `bs4`.
# BeautifulSoup es una herramienta que convierte documentos HTML (o XML) en un formato
# que Python puede leer y manipular fácilmente.
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
# Esto significa que el programa no comprobará si el nombre del certificado coincide con el del servidor.
ctx.verify_mode = ssl.CERT_NONE
# Desactivamos completamente la validación del certificado SSL.
# Esto permite conectarse a servidores HTTPS incluso si tienen un certificado no válido.

# Solicitamos al usuario que ingrese la URL
url = input('Enter - ')
# La función `input()` muestra el mensaje `'Enter - '` y espera a que el usuario escriba algo.
# Lo que el usuario escribe se guarda en la variable `url`.

# Abrimos la URL proporcionada por el usuario y descargamos su contenido.
# `urlopen(url, context=ctx)` abre la URL utilizando el contexto SSL que configuramos.
# `.read()` lee todo el contenido de la página y lo guarda como una cadena de bytes en la variable `html`.
html = urlopen(url, context=ctx).read()

# Analizamos (parseamos) el contenido HTML con BeautifulSoup.
# `BeautifulSoup(html, "html.parser")` convierte el contenido HTML en un objeto BeautifulSoup.
# Esto nos permite buscar y extraer elementos específicos del HTML fácilmente.
soup = BeautifulSoup(html, "html.parser")

# Recuperamos todas las etiquetas de enlace (`<a>`) del documento HTML.
# `soup('a')` busca todas las etiquetas `<a>` (enlaces) en el HTML.
# Devuelve una lista de objetos BeautifulSoup que representan cada etiqueta `<a>`.
tags = soup('a')

# Iteramos sobre cada etiqueta `<a>` que encontramos en el HTML.
for tag in tags:
    # Imprimimos la etiqueta completa.
    # Esto incluye todo el contenido de la etiqueta `<a>`, como atributos y texto.
    print('TAG:', tag)
    
    # Imprimimos el valor del atributo `href`, que contiene el enlace al que apunta la etiqueta `<a>`.
    # `tag.get('href', None)` busca el atributo `href`.
    # Si no existe, devuelve `None`.
    print('URL:', tag.get('href', None))
    
    # Imprimimos el contenido de la etiqueta `<a>`.
    # `tag.contents[0]` devuelve el texto o elemento dentro de la etiqueta `<a>`.
    # Si la etiqueta está vacía, podría generar un error.
    print('Contents:', tag.contents[0])
    
    # Imprimimos todos los atributos de la etiqueta `<a>` como un diccionario.
    # `tag.attrs` devuelve un diccionario donde las claves son los nombres de los atributos
    # y los valores son los valores de esos atributos.
    print('Attrs:', tag.attrs)
