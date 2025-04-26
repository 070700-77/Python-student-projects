# 🔹 Este programa se conecta a la API "https://randomuser.me/api/" y obtiene información de usuarios aleatorios.
# 🔹 Solicita 20 registros y muestra los datos de cada usuario, incluyendo nombre, dirección, contacto y credenciales de acceso.
# 🔹 También cuenta cuántos hombres y mujeres fueron generados aleatoriamente.

# Importamos los módulos necesarios para la conexión a la API y el manejo de datos.
import urllib.request, urllib.parse, urllib.error  
# `urllib.request`: Permite abrir URLs y descargar datos de Internet.
# `urllib.parse`: Ayuda a codificar parámetros en la URL.
# `urllib.error`: Permite manejar errores en la conexión a la API.

import json  
# `json`: Nos permite trabajar con datos en formato JSON (JavaScript Object Notation).
# JSON es un formato estándar para intercambiar información con APIs.

import time  
# `time`: Se usa aquí para manejar marcas de tiempo si es necesario (no se usa en este código).

import hashlib  
# `hashlib`: Proporciona funciones de hash seguro (MD5, SHA1, SHA256), pero en este código no se usa directamente.

import ssl  
# `ssl`: Maneja conexiones seguras HTTPS, permitiendo ignorar errores de certificados.

# 🔹 CONFIGURACIÓN DEL CONTEXTO SSL PARA IGNORAR ERRORES DE CERTIFICADO 🔹
ctx = ssl.create_default_context()  
# Creamos un contexto SSL para manejar conexiones HTTPS seguras.

ctx.check_hostname = False  
# Desactivamos la verificación del nombre del servidor en el certificado SSL.

ctx.verify_name = ssl.CERT_NONE  
# Desactivamos completamente la verificación del certificado SSL.
# Esto permite conectarnos a servidores que pueden tener certificados auto-firmados.

# 🔹 SOLICITAR AL USUARIO QUE INGRESE LA URL DE LA API 🔹
while True:
    base_url = input("Enter API URL: ")  
    # Pedimos al usuario que ingrese la URL de la API.

    if len(base_url) < 1:  
        # Si el usuario no ingresa nada (es decir, presiona ENTER sin escribir), mostramos un mensaje de error.
        print('Invalid URL. Try again. \n')
        continue  # Volvemos a pedir la URL.

    break  # Si la URL ingresada es válida, salimos del bucle.

# 🔹 SOLICITAMOS LOS DATOS A LA API 🔹
data_request = urllib.request.urlopen(base_url, context=ctx)  
# `urllib.request.urlopen(base_url, context=ctx)` abre la URL y descarga su contenido.

# 🔹 LEEMOS Y DECODIFICAMOS LA RESPUESTA JSON 🔹
get_data = data_request.read().decode()  
# `.read()` obtiene todo el contenido de la respuesta en bytes.
# `.decode()` convierte los bytes en una cadena de texto legible.

# 🔹 CONVERTIMOS LOS DATOS JSON A UN DICCIONARIO PYTHON 🔹
info = json.loads(get_data)  
# `json.loads(get_data)` convierte la respuesta JSON en un diccionario de Python.

# 🔹 FORMATEAMOS Y ORDENAMOS LA SALIDA JSON 🔹
pretty_info = json.dumps(info, indent=4)  
# `json.dumps(info, indent=4)` convierte el diccionario `info` en una cadena JSON bien formateada.
# `indent=4` hace que la salida sea más legible agregando espacios y saltos de línea.

# 🔹 INICIALIZAMOS CONTADORES PARA REGISTRAR EL GÉNERO DE LOS USUARIOS 🔹
i = 0  
# `i` se usará como contador para el bucle de solicitudes a la API.

men = 0  
# `men` almacenará la cantidad de hombres generados aleatoriamente.

women = 0  
# `women` almacenará la cantidad de mujeres generadas aleatoriamente.

# 🔹 BUCLE PARA GENERAR 20 USUARIOS ALEATORIOS 🔹
while i < 20:
    # Realizamos una nueva solicitud a la API para obtener un nuevo usuario aleatorio.
    data_request = urllib.request.urlopen(base_url, context=ctx)
    get_data = data_request.read().decode()
    info = json.loads(get_data)

    # Formateamos la salida para que sea legible.
    pretty_info = json.dumps(info, indent=4)

    # Iteramos sobre los resultados dentro de `info['results']`.
    for item in info['results']:
        # Extraemos los datos del usuario desde el JSON.

        # 🔹 Datos personales del usuario 🔹
        gender = item['gender']  # Género del usuario ("male" o "female").
        first_name = item['name']['first']  # Nombre del usuario.
        family_name = item['name']['last']  # Apellido del usuario.

        # 🔹 Dirección del usuario 🔹
        street_num = item['location']['street']['number']  # Número de la calle.
        street_name = item['location']['street']['name']  # Nombre de la calle.
        city = item['location']['city']  # Ciudad.
        state = item['location']['state']  # Estado o región.
        country = item['location']['country']  # País.
        zip_code = str(item['location']['postcode'])  # Código postal.

        # 🔹 Coordenadas de ubicación 🔹
        lat = item['location']['coordinates']['latitude']  # Latitud.
        lon = item['location']['coordinates']['longitude']  # Longitud.

        # 🔹 Información de contacto 🔹
        email = item['email']  # Correo electrónico.
        birthday = item['dob']['date']  # Fecha de nacimiento.
        age = item['dob']['age']  # Edad del usuario.
        r_date = item['registered']['date']  # Fecha de registro en la API.
        r_years = item['registered']['age']  # Años desde el registro.

        # 🔹 Información de contacto 🔹
        phone = item['phone']  # Número de teléfono fijo.
        cel = item['cell']  # Número de teléfono móvil.

        # 🔹 Imágenes del perfil del usuario 🔹
        large_user_picture = item['picture']['large']  # Imagen grande del usuario.
        medium_user_picture = item['picture']['medium']  # Imagen mediana del usuario.
        thumbnail_picture = item['picture']['thumbnail']  # Imagen miniatura del usuario.

        # 🔹 Credenciales de acceso 🔹
        uuid = item['login']['uuid']  # Identificador único del usuario.
        username = item['login']['username']  # Nombre de usuario.
        password = item['login']['password']  # Contraseña en texto plano.
        salt = item['login']['salt']  # Salt usado para cifrar la contraseña.
        md5 = item['login']['md5']  # Hash MD5 de la contraseña.
        sha1 = item['login']['sha1']  # Hash SHA1 de la contraseña.
        sha256 = item['login']['sha256']  # Hash SHA256 de la contraseña.

    # 🔹 MOSTRAR INFORMACIÓN DEL USUARIO 🔹
    print(f"""
        -------------------------------------------
        User Information:
        -------------------------------------------
        Name: {first_name} {family_name}
        Gender: {gender}
        Address: {street_num} {street_name}, {city}, {state}, {country} - {zip_code}
        Coordinates: Latitude {lat}, Longitude {lon}
        Email: {email}
        Birthday: {birthday} (Age: {age})
        Registered: {r_date} ({r_years} years ago)
        Phone: {phone}
        Cell: {cel}
        Profile Pictures:
          - Large: {large_user_picture}
          - Medium: {medium_user_picture}
          - Thumbnail: {thumbnail_picture}
        Login Credentials:
          - UUID: {uuid}
          - Username: {username}
          - Password: {password}
          - Salt: {salt}
          - MD5 Hash: {md5}
          - SHA1 Hash: {sha1}
          - SHA256 Hash: {sha256}
        -------------------------------------------
        """)

    # 🔹 CONTAMOS CUÁNTOS HOMBRES Y MUJERES SE GENERARON 🔹
    if gender == "male":
        men += 1
    else:
        women += 1

    i += 1  # Aumentamos el contador del bucle.

# 🔹 MOSTRAR RESUMEN DE GÉNEROS 🔹
print("----------------------------------------------") 
print("Total gender count \n")
print(f'Male = {men}')
print(f'Female = {women}')
