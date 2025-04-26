import socket
# Esta línea importa el módulo 'socket', el cual es una herramienta incluida en Python
# que nos permite establecer conexiones de red y comunicarnos con servidores de Internet.
# Por ejemplo, gracias a 'socket' podremos conectarnos a un servidor web y enviar y recibir datos.


mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Aquí estamos creando un "socket", que es básicamente un "enchufe" que nos permite conectarnos 
# a una dirección en Internet. 
# 'socket.AF_INET' indica que usaremos direcciones IPv4 (el tipo más común de direcciones de Internet).
# 'socket.SOCK_STREAM' indica que usaremos un socket de tipo "stream", o flujo, que suele utilizarse 
# con el protocolo TCP, el estándar para las conexiones web.
mysock.connect(('data.pr4e.org', 80))
# Aquí utilizamos el socket que acabamos de crear para conectarnos a un servidor específico.
# 'data.pr4e.org' es el nombre del servidor al que nos conectaremos.
# El segundo valor, '80', es el número de puerto. El puerto 80 es el puerto estándar para HTTP, 
# el protocolo que usamos para solicitar páginas web.
# Esta línea, por lo tanto, hace que nuestro programa se conecte a "http://data.pr4e.org" en el puerto 80, 
# creando una conexión a través de Internet.
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# Ahora creamos un mensaje que enviaremos al servidor para pedirle un recurso.
# El mensaje es una cadena que representa una solicitud HTTP del tipo GET.
# La solicitud dice: "GET http://data.pr4e.org/romeo.txt HTTP/1.0".
# Esto significa: 
# - "GET": queremos obtener (descargar) un recurso.
# - "http://data.pr4e.org/romeo.txt": esta es la ubicación completa del archivo que queremos.
# - "HTTP/1.0": indica que usaremos la versión 1.0 del protocolo HTTP.
# Al final añadimos '\r\n\r\n' que indica el final de la cabecera HTTP.
#
# Luego usamos '.encode()' para convertir la cadena de texto en bytes, 
# ya que el socket envía y recibe información en forma de bytes, no de texto.
mysock.send(cmd)
# Esta línea envía el comando (la petición GET) a través de la conexión que establecimos con el servidor.
# Después de esta línea, el servidor recibirá nuestra solicitud y nos enviará una respuesta.


while True:
    data = mysock.recv(512)
    # Aquí entramos en un bucle 'while True' que significa "haz lo que hay adentro 
    # hasta que hagamos un 'break' (una ruptura del bucle)".
    #
    # mysock.recv(512) intenta leer hasta 512 bytes de información provenientes del servidor.
    # ¿Qué significa esto? Una vez que hemos enviado la petición al servidor, este nos responderá 
    # con datos. Podrían ser las cabeceras HTTP y el contenido del archivo 'romeo.txt'.
    #
    # Si el servidor envía datos, 'data' contendrá esos bytes. Si no hay más datos que recibir, 
    # 'data' tendrá un largo (len) menor que 1, lo que significa que se acabó la información.
    if len(data) < 1:
        # Esta condición verifica si la cantidad de datos recibidos es menor que 1 byte, 
        # lo que significa que no hay más datos que leer del servidor.
        break
         # 'break' sale del bucle 'while True'.
    print(data.decode(),end='')
    # Si sí recibimos datos, entonces 'data' son bytes. Usamos 'data.decode()' 
    # para convertir esos bytes en texto entendible (cadena de caracteres).
    # Luego usamos 'print(..., end="")' para imprimir los datos sin agregar 
    # una nueva línea adicional cada vez.
    #
    # A medida que este bucle se repite, vamos leyendo en trozos (de 512 bytes cada uno) 
    # y los imprimimos hasta que ya no haya más datos. De esta forma, 
    # veremos el contenido completo de la respuesta del servidor, 
    # que incluye las cabeceras HTTP (información sobre el archivo, la fecha, etc.) 
    # y el contenido real del archivo 'romeo.txt'.
        
        
mysock.close()
# Finalmente, cerramos el socket con 'mysock.close()'.
# Esto es importante porque así liberamos la conexión 
# y no mantenemos recursos ocupados en el servidor o en nuestro programa.
#
# Después de esta línea, ya hemos recibido e impreso todo el contenido que el servidor nos envió.