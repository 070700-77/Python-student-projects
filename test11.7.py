import urllib.request, urllib.parse, urllib.error# Importamos módulos de la biblioteca estándar para manejar URLs.
# - `urllib.request`: Permite abrir URLs y leer su contenido.
# - `urllib.parse`: Ayuda a construir y manipular URLs, por ejemplo, combinando partes.
# - `urllib.error`: Maneja errores que ocurren al trabajar con URLs, como tiempo de espera o errores 404.

from urllib.parse import urljoin
# Importamos específicamente `urljoin` de `urllib.parse`.
# Este método toma una URL base y combina enlaces relativos con ella para formar URLs completas.
# Por ejemplo, si la URL base es `http://example.com/page` y el enlace es `next.html`, 
# el resultado será `http://example.com/next.html`.

from bs4 import BeautifulSoup
# Importamos `BeautifulSoup` de la biblioteca `bs4`. Es una herramienta para analizar documentos HTML.
# Permite buscar elementos como etiquetas `<a>` (enlaces), `<p>` (párrafos), etc., 
# y extraer información de ellos.

import ssl
# Importamos la biblioteca `ssl` para manejar conexiones seguras con HTTPS.
# HTTPS utiliza SSL/TLS para cifrar las comunicaciones, lo que evita que sean interceptadas.

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_name = ssl.CERT_NONE
# Creamos un "contexto SSL" personalizado.
# 1. `create_default_context()` inicializa configuraciones por defecto para conexiones seguras.
# 2. `ctx.check_hostname = False` desactiva la verificación del nombre del host (normalmente se valida que coincida con el certificado del servidor).
# 3. `ctx.verify_name = ssl.CERT_NONE` desactiva completamente la verificación del certificado SSL.
# Estas configuraciones permiten conectarse incluso a sitios con certificados no válidos.

history = []
# Declaramos una lista vacía llamada `history`.
# Aquí almacenaremos todas las URLs que encontremos para evitar procesar la misma página varias veces.

while True:
    link = input("Enter link: ")
    # Pedimos al usuario que ingrese una URL inicial desde donde comenzaremos el proceso.
    # El programa no avanza hasta que el usuario proporcione una entrada válida.
    
    if link.strip() == "":
        # `link.strip()` elimina espacios en blanco al inicio y al final de la cadena.
        # Si, después de esto, la cadena sigue vacía, significa que el usuario no ingresó nada.
        print("Invalid URL. Try again")
        # Mostramos un mensaje indicando que la URL no es válida.
        continue
        # Volvemos al inicio del bucle `while True` para que el usuario lo intente nuevamente.
    try:
        base_url = urllib.request.urlopen(link, context = ctx).geturl()
         # Intentamos abrir la URL proporcionada utilizando `urlopen`.
        # Si se abre correctamente:
        # - `geturl()` devuelve la URL final después de redirecciones (si las hubo).
        # Guardamos esta URL como la `base_url`.

        break
        # Si todo sale bien, salimos del bucle porque ya tenemos una URL válida.
    except Exception as e:
        # Si ocurre algún error (por ejemplo, la URL no es válida, el servidor no responde, etc.):
        print(f"Error accessing URL: {e}")
         # Mostramos un mensaje de error con el detalle de lo que ocurrió.
        continue
        # Volvemos al inicio del bucle para pedir otra URL al usuario.
    
try:
    url = urllib.request.urlopen(base_url, context = ctx).read()
    # Abrimos la URL base que proporcionó el usuario y leemos su contenido.
    # `read()` devuelve el contenido en formato binario (bytes), que representa el HTML de la página.
    
    soup = BeautifulSoup(url, "html.parser")
    # Creamos un objeto `BeautifulSoup` a partir del contenido HTML descargado.
    # El segundo argumento, `"html.parser"`, le dice a BeautifulSoup que use el analizador HTML incluido en Python.
    
    tags = soup("a")
    # Buscamos todas las etiquetas `<a>` en el HTML. Estas etiquetas representan enlaces en la página.
    # `tags` es una lista de objetos BeautifulSoup que representan cada enlace.

    for tag in tags:
        href = tag.get("href", None)
        # Iteramos sobre cada etiqueta `<a>` encontrada en la página.
        # Usamos `tag.get("href", None)` para obtener el valor del atributo `href` de cada enlace.
        # Si el atributo `href` no existe, devolvemos `None`.
        
        if href:
            # Solo trabajamos con enlaces que tengan un atributo `href` válido (no `None`).
            full_url = urljoin(base_url, href)
            # Convertimos el enlace en una URL completa usando `urljoin`.
            # Esto es útil porque algunos enlaces pueden ser relativos, como `/about`, y necesitamos combinarlos con la URL base.
            
            if full_url not in history:
                # Si la URL completa no está ya en la lista `history` (es decir, no la hemos procesado antes):
                history.append(full_url)
                # La agregamos a la lista para evitar procesarla otra vez en el futuro.
except Exception as e:
    print(f"Error processing initial page: {e}")
    # Si ocurre algún error al procesar la página inicial (por ejemplo, HTML malformado),
    # mostramos un mensaje con el detalle del error.

for item in history[:]:
    # Iteramos sobre una copia de la lista `history`. El operador `[:]` crea una copia completa.
    # Esto nos permite agregar nuevas URLs al historial mientras seguimos procesando sin afectar la iteración.
    
    try: 
        print(f"Procesing: {item}")
        # Imprimimos la URL que estamos procesando actualmente.
        
        url = urllib.request.urlopen(item, context=ctx).read()
        # Abrimos la URL actual y leemos su contenido HTML.
        
        soup = BeautifulSoup(url, "html.parser")
        # Analizamos el contenido HTML descargado con BeautifulSoup.
        
        tags = soup("a")
        # Buscamos todas las etiquetas `<a>` (enlaces) en esta nueva página.
        
        for tag in tags:
            href = tag.get("href", None)
            # Para cada enlace encontrado, obtenemos el valor del atributo `href`.
            
            if href:
                full_url = urljoin(item, href)
                # Convertimos el enlace relativo en una URL absoluta usando `urljoin`.
                # La URL base para este enlace es `item` (la página actual).
                
                if full_url not in history:
                    # Si esta URL no está ya en nuestro historial:
                    history.append(full_url)
                    # La agregamos al historial para procesarla más adelante.
    except Exception as e:
        print(f"Error procesing {item}: {e}")
        # Si ocurre algún error al procesar esta página (por ejemplo, la página no existe o tiene errores),
        # mostramos un mensaje indicando el error.    