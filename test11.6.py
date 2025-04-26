# http://py4e-data.dr-chuck.net/known_by_Kyhran.html
import urllib.request, urllib.parse, urllib.error
# Estas importaciones nos permiten usar las funciones de la librería 'urllib' 
# para abrir URLs (páginas web), manejar parámetros de la URL (parse) y posibles errores.

from bs4 import BeautifulSoup
# Importamos la clase 'BeautifulSoup' de la librería 'bs4'. 
# Esta clase nos permitirá "leer" el HTML de una página web 
# y extraer información de manera sencilla (como los enlaces <a>).

import ssl
# 'ssl' significa 'Secure Sockets Layer' y se usa para manejar conexiones cifradas.
# Aquí lo usaremos para configurar aspectos de seguridad en nuestra conexión HTTP/HTTPS.

# A continuación definimos algunas variables que usaremos más adelante.
i = 0
# 'i' es un contador que empezamos en 0. Lo usaremos para contar el número de veces 
# que repetimos el seguimiento de enlaces.

adresses = []
# 'adresses' será una lista vacía donde vamos a guardar temporalmente 
# todos los links (los href) que encontremos en la página actual.

history = []
# 'history' será otra lista vacía que almacenará el historial de enlaces 
# en el orden en que los visitamos. Esto nos permitirá ver la secuencia 
# de URLs que seguimos.

# Configuramos nuestro contexto de seguridad SSL:
ctx = ssl.create_default_context()
# 'create_default_context()' crea un "entorno" con valores predeterminados de seguridad. 

ctx.check_hostname = False
# Con esto desactivamos la verificación de que el nombre del host (la URL) 
# coincida exactamente con el certificado SSL. (En escenarios reales, 
# lo normal sería dejarlo activado por seguridad.)

ctx.verivy_name = ssl.CERT_NONE
# (Este nombre de atributo parece tener un error ortográfico, 
# probablemente queríamos poner 'verify_mode' o algo similar. 
# Aun así, la idea es desactivar la verificación del certificado SSL por completo,
# lo cual no es recomendable en ambientes de producción, pero sirve 
# para evitar errores de certificados al momento de aprender.)

# A continuación, pediremos al usuario que introduzca la URL (enlace) 
# desde la cual va a empezar la búsqueda de enlaces.
# Usamos un bucle 'while True' para asegurarnos de que la URL no esté en blanco.
while True:
    link = input("Enter link: ")
    # 'input()' muestra el mensaje "Enter link: " en la consola 
    # y permite que el usuario escriba algo (la URL en este caso).
    
    if link == "":
        # Si el usuario presiona Enter sin escribir nada, 
        # significa que la cadena está vacía ("").
        
        print("")
         # Simplemente imprime una línea en blanco.
        
        print("Invalid URL. Try again please. ")
        # Muestra un mensaje de error para indicar que la URL no es válida.
        
        continue
        # 'continue' hace que el bucle while se "reinicie" 
        # y vuelva a pedir la URL, sin pasar a las siguientes líneas.
    
    break
    # Si el usuario sí escribió algo (no está vacío), 'break' rompe el bucle 
    # y continuamos con el programa.

# Ahora que tenemos un 'link' válido, usamos 'urllib.request.urlopen' para abrir la página.
# 'context=ctx' significa que usamos nuestro contexto SSL que desactiva ciertas verificaciones.
url = urllib.request.urlopen(link, context = ctx).read()
# '.read()' lee todo el contenido HTML de la página y lo guarda 
# en la variable 'url' (aunque el nombre 'url' puede ser algo confuso, 
# lo que se guarda es el *contenido* de la página, no la dirección).

# Usamos BeautifulSoup para analizar (parsear) este contenido HTML.
soup = BeautifulSoup(url, "html.parser")
# 'BeautifulSoup(url, "html.parser")' crea un objeto que nos permite 
# acceder a diferentes partes del HTML, por ejemplo, a todas las etiquetas <a>.

tags = soup("a")
# Con 'soup("a")', le pedimos a BeautifulSoup que nos devuelva 
# todas las etiquetas <a> (todos los enlaces) que existen en la página. 
# 'tags' será una lista de todos esos objetos <a>.

# Recorremos la lista de etiquetas <a> para extraer los enlaces (href).
for tag in tags:
    x = tag.get("href", None)
    # 'tag.get("href", None)' intenta obtener el valor del atributo 'href' 
    # de la etiqueta <a>. Si no lo encuentra, devuelve 'None'.
    
    adresses.append(x)
    # Agregamos ese enlace (sea URL o None) a nuestra lista 'adresses'.
    # Por cada etiqueta <a>, tendremos un elemento en 'adresses'.

# Según el enunciado del ejercicio, necesitamos tomar el enlace 
# que se encuentra en la posición 17 de la lista 'adresses' (contando desde 0).
# Recordar que la posición "18" para un humano es índice "17" para Python.
follow_up = adresses[17]
# 'follow_up' será la dirección que debemos seguir. 

history.append(follow_up)
# Agregamos este primer enlace 'follow_up' al historial 'history'. 
# Así vamos construyendo la secuencia de enlaces que visitamos.

adresses.clear()
# Limpiamos la lista 'adresses' para que no se acumulen enlaces de la página anterior.
# 'adresses.clear()' borra todos los elementos de la lista, dejándola vacía.

# Ahora queremos repetir este proceso varias veces. El enunciado dice 7 veces, 
# pero aquí se ha puesto un bucle que se repetirá 6 veces. 
# En total, según el código, se visitará el primer enlace y luego 6 más (7 en total).
    
while i < 6:
    # Este bucle se repetirá mientras 'i' sea menor que 6. 
    # Cada vez que pase, 'i' se incrementará al final. 
    # Por lo tanto, el bucle correrá 6 veces.
    
    url = urllib.request.urlopen(follow_up, context = ctx).read()
    # Abrimos la página que está en 'follow_up' (la dirección que recogimos anteriormente)
    # y leemos su contenido HTML.
    
    soup = BeautifulSoup(url, "html.parser")
    # Convertimos el contenido HTML en un objeto BeautifulSoup para poder analizarlo.
    
    tags = soup("a")
    # Buscamos nuevamente todas las etiquetas <a> de la nueva página.
    
    adresses.clear()
    # Vaciamos la lista 'adresses' para guardar los enlaces de esta nueva página, 
    # evitando mezclar enlaces de la página anterior.
    
    for tag in tags:
        x = tag.get("href", None)
        # De cada etiqueta <a>, sacamos el atributo 'href'.
        adresses.append(x)
        # Lo ponemos en 'adresses'.
        
    follow_up = adresses[17]
    # Otra vez, de la lista de enlaces de esta nueva página, 
    # nos quedamos con el enlace en la posición 17 (el que hace 18 si contásemos desde 1).
    
    history.append(follow_up)
    # Agregamos este enlace a nuestro 'history' para llevar la secuencia visitada.
    i +=1     
    # Sumamos 1 a 'i'. Cuando 'i' llegue a 6, el bucle terminará.

# Cuando el bucle termina, hemos visitado enlaces sucesivos un total de 7 veces (incluyendo la inicial).
print(history)
# Finalmente, imprimimos la lista completa de 'history', 
# donde aparecerán todas las URLs que se han ido siguiendo 
# en el orden exacto en que fueron visitadas.