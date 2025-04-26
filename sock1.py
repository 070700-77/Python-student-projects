# Este bucle "while True" se utiliza para asegurarnos de que el usuario
# ingrese una URL (un enlace) válido. Si el usuario deja el campo vacío,
# se le pedirá que ingrese un enlace hasta que lo haga.
while True:
    url = input("Enter link: ")  # Pide al usuario que escriba una dirección URL.
    if url == "":
        # Si el usuario no ingresa nada (deja la URL vacía),
        # imprimimos un mensaje indicándole que debe ingresar un enlace válido.
        print("Enter a valind link, please. ")
        continue
    break

# Importamos el módulo 'socket' que nos permite conectarnos a servidores
# a través de la red utilizando diferentes protocolos, en este caso el protocolo TCP.
import socket

# Aquí dividimos la URL en partes. La función 'split("/")' separa el texto
# cada vez que encuentra el carácter "/". Por ejemplo, si la URL es:
# "http://www.example.com/index.html"
# Al hacer 'url.split("/")', obtendremos una lista:
# ["http:", "", "www.example.com", "index.html"]
words = url.split('/')

# La variable 'host' será el nombre del servidor (host) al que queremos conectarnos.
# Según el ejemplo anterior, 'words[2]' sería "www.example.com",
# ya que en las URLs la parte del host va después de "http://" o "https://".
# Indice 0: "http:"
# Indice 1: "" (porque entre http: y www.example.com hay dos barras //)
# Indice 2: "www.example.com"
host = words[2]

# Creamos un objeto 'mysock' que es nuestro "socket". Un socket es como un "enchufe"
# que nos permite conectarnos a una dirección en la red.
# 'socket.AF_INET' indica que utilizaremos el protocolo de internet IPv4.
# 'socket.SOCK_STREAM' indica que usaremos un socket de tipo "stream", que se utiliza para TCP.
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Nos "conectamos" al host en el puerto 80, que es el puerto estándar para HTTP.
# Esto significa que estamos abriendo una conexión TCP con el servidor web.
mysock.connect((host, 80))

# Para solicitar un documento a través del protocolo HTTP, debemos enviar una línea
# de pedido (request) al servidor. Esa petición suele tener la forma:
# "GET /ruta/del/recurso HTTP/1.0\r\n\r\n"
# '\r\n' indica un salto de línea en el estándar de internet.
# Aquí enviamos, por ejemplo: "GET http://www.example.com/index.html HTTP/1.0\r\n\r\n"
# En realidad, el servidor espera el camino del recurso (path), pero usar la URL completa a veces también funciona.
# La parte 'encode()' convierte el texto a bytes, que es lo que el socket envía realmente.
mysock.send(('GET '+url+' HTTP/1.0\r\n\r\n').encode())

# Ahora entraremos en un bucle para recibir la respuesta del servidor.
# Cuando enviamos la petición 'GET', el servidor nos responderá con información.
# 'mysock.recv(512)' intentará leer hasta 512 bytes de datos desde el servidor.
# Si el servidor ya no envía más datos, entonces 'recv' devolverá un valor menor que 1,
# lo que significa que no hay más datos que recibir.
while True:
    data = mysock.recv(512)  # Recibimos datos en paquetes de 512 bytes.
    if len(data) < 1:
        # Si la cantidad de datos recibidos es menor que 1, significa que ya no hay más información.
        # Entonces salimos del bucle con 'break'.
        break
    # 'data.decode()' convierte los datos desde bytes a una cadena (texto).
    # 'print(..., end="")' imprime sin agregar una nueva línea por defecto.
    # Imprimimos todo lo que recibimos del servidor, que incluirá las cabeceras HTTP
    # y el contenido del documento solicitado.
    print(data.decode(),end='')
    
# Cerramos el socket ya que hemos terminado de recibir datos.    
mysock.close()


