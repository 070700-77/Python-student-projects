# 🔹 Este programa consulta la API 'https://py4e-data.dr-chuck.net/opengeo?'
# 🔹 Permite obtener información geográfica sobre una ubicación ingresada por el usuario.
# 🔹 Muestra el país, estado, ciudad, coordenadas, dirección formateada y un código especial de ubicación.

# Importamos los módulos necesarios para la conexión a la API y el manejo de datos.
import urllib.request, urllib.parse, urllib.error  
# `urllib.request`: Permite abrir URLs y descargar datos de Internet.
# `urllib.parse`: Ayuda a construir y codificar parámetros para la URL.
# `urllib.error`: Permite manejar errores en la conexión a la API.

import ssl  
# `ssl`: Maneja conexiones seguras HTTPS, permitiendo ignorar errores de certificados.

import json  
# `json`: Nos permite trabajar con datos en formato JSON (JavaScript Object Notation).
# JSON es un formato estándar para intercambiar información con APIs.

from bs4 import BeautifulSoup  
# `BeautifulSoup` se usa para analizar HTML y XML.
# **En este código no se está utilizando**, posiblemente fue agregado por error.

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
    base_url = input('Enter API URL: ')  
    # Pedimos al usuario que ingrese la URL base de la API.

    base_url = base_url.strip()  
    # `.strip()` elimina espacios en blanco antes y después del texto ingresado.

    if len(base_url) < 1:  
        # Si el usuario no ingresa nada, mostramos un mensaje de error.
        print(f'The URL: {base_url} is invalid. Try again please. \n')
        continue  # Volvemos a pedir la URL.

    break  # Si la URL ingresada es válida, salimos del bucle.

# 🔹 SOLICITAR AL USUARIO QUE INGRESE UNA UBICACIÓN 🔹
while True:
    location = input('Enter location name: ')  
    # Pedimos al usuario que ingrese el nombre de una ubicación.

    if len(location) < 1:  
        # Si el usuario no ingresa nada, mostramos un mensaje de error.
        print(f'The location requested: {location} is invalid. Try again please. \n')
        continue  # Volvemos a pedir la ubicación.

    break  # Si la ubicación ingresada es válida, salimos del bucle.

# 🔹 LIMPIAR EL NOMBRE DE LA UBICACIÓN 🔹
location = location.strip()  
# `.strip()` elimina espacios en blanco antes y después del texto ingresado por el usuario.

# 🔹 CONSTRUCCIÓN DE LOS PARÁMETROS DE LA SOLICITUD 🔹
parameter = {}  
# Creamos un diccionario `parameter` para almacenar los parámetros de la solicitud.

parameter['q'] = location  
# Agregamos el parámetro `q` con la ubicación ingresada por el usuario.

# 🔹 CREAR LA URL FINAL CON LOS PARÁMETROS 🔹
url = base_url + urllib.parse.urlencode(parameter)  
# `urllib.parse.urlencode(parameter)` convierte el diccionario `parameter` en una cadena de consulta URL.
# Esto generará algo como: "https://py4e-data.dr-chuck.net/opengeo?q=Paris"

# 🔹 ENVIAR SOLICITUD A LA API Y OBTENER DATOS 🔹
requested_info = urllib.request.urlopen(url, context=ctx)  
# `urllib.request.urlopen(url, context=ctx)` abre la URL y descarga su contenido.

# 🔹 LEER Y DECODIFICAR LA RESPUESTA JSON 🔹
info = requested_info.read().decode()  
# `.read()` obtiene todo el contenido de la respuesta en bytes.
# `.decode()` convierte los bytes en una cadena de texto legible.

# 🔹 CONVERTIR LOS DATOS JSON A UN DICCIONARIO PYTHON 🔹
data = json.loads(info)  
# `json.loads(info)` convierte la respuesta JSON en un diccionario de Python.

# 🔹 FORMATEAR LA SALIDA JSON PARA HACERLA MÁS LEGIBLE 🔹
sorted_data = json.dumps(data, indent=4)  
# `json.dumps(data, indent=4)` convierte el diccionario `data` en una cadena JSON bien formateada.
# `indent=4` agrega espacios y saltos de línea para facilitar la lectura.

# 🔹 IMPRIMIR SEPARADOR VISUAL 🔹
print("------------------------------------------------------------------------------- \n")

# 🔹 EXTRAER E IMPRIMIR INFORMACIÓN DETALLADA SOBRE LA UBICACIÓN 🔹
for item in data['features']:  
    # Iteramos sobre la lista `features` en el JSON recibido.

    location_name = item['properties']["display_name"]  
    # Nombre completo de la ubicación.

    country = item['properties']["country"]  
    # Nombre del país.

    country_code = item['properties']["country_code"]  
    # Código de dos letras del país (ejemplo: "US" para Estados Unidos).

    state = item['properties']["state"]  
    # Nombre del estado o región.

    city = item['properties']["city"]  
    # Nombre de la ciudad.

    lat = item['properties']['lat']  
    # Latitud de la ubicación.

    lon = item['properties']['lon']  
    # Longitud de la ubicación.

    formatted = item['properties']['formatted']  
    # Dirección formateada.

    plus_code = item['properties']['plus_code']  
    # Código único de Google Maps para identificar la ubicación.

    # 🔹 IMPRIMIR LA INFORMACIÓN OBTENIDA 🔹
    print("\n📍 Location Information 📍\n")
    print(f"   🏙️ Location Name: {location_name}")
    print(f"   🌍 Country: {country} ({country_code.upper()})")
    print(f"   🏛️ State: {state}")
    print(f"   🏘️ City: {city}")
    print(f"   📌 Coordinates: {lat}, {lon}")
    print(f"   🗺️ Formatted Address: {formatted}")
    print(f"   ➕ Plus Code: {plus_code}\n")
