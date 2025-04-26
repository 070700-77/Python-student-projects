# Works with the following API: https://api.agify.io
# Esta API gratuita predice la edad más probable de una persona, basándose en su nombre y datos estadísticos.

# 🔹 Importamos los módulos necesarios para trabajar con URLs, solicitudes web, y datos JSON

import urllib.request   # Sirve para abrir URLs desde Python y leer su contenido.
import urllib.parse     # Permite codificar parámetros para incluirlos en una URL (como name=juan).
import urllib.error     # Permite capturar errores si ocurre un problema con la solicitud a la web.

import json             # Permite leer y convertir datos que vienen en formato JSON (muy usado en APIs).

import ssl              # Permite manejar conexiones seguras HTTPS, incluso si hay errores de certificados.

# 🔹 Creamos un contexto SSL que ignora errores de certificados (por seguridad normalmente no deberías hacer esto, pero algunas APIs no los tienen bien configurados)

ctx = ssl.create_default_context()   # Creamos una "configuración segura" para HTTPS
ctx.check_hostname = False           # No verificamos si el certificado coincide con el dominio
ctx.verify_name = ssl.CERT_NONE      # Desactivamos la validación del certificado

# 🔹 PRIMER BUCLE: Pedimos la URL base de la API

while True:
    lname = input("Enter API URL: ")  # Pedimos al usuario la URL base (ej: https://api.agify.io)
    if len(lname) < 1:                # Si el usuario no escribió nada...
        print("Try again. \n")        # Mostramos un mensaje
        continue                      # Volvemos a pedirlo
    break                             # Si sí escribió algo, salimos del bucle

# 🔹 SEGUNDO BUCLE: Pedimos el nombre que queremos analizar

while True:
    pname = input("Enter name: ")     # Pedimos el nombre de la persona
    if len(pname) < 1:                # Si está vacío...
        print('Try again. \n')        # Mostramos error
        continue                      # Volvemos a pedirlo
    break                             # Si es válido, salimos del bucle

# 🔹 Creamos un diccionario de parámetros para pasar a la URL
# En este caso, la API de Agify espera algo como `?name=juan`

params = {}
params['name'] = pname  # Guardamos el nombre que el usuario escribió bajo la clave 'name'

# 🔹 Codificamos los parámetros del diccionario en formato URL
# Esto convierte {'name': 'juan'} en 'name=juan'
query_string = urllib.parse.urlencode(params)

# 🔹 Creamos la URL final que incluye el parámetro del nombre
# Si la URL base ya incluye un "?", usamos "&" para agregar más parámetros.
# Si no lo incluye, usamos "?" para empezar la parte de parámetros.

if "?" in lname:
    full_url = lname + "&" + query_string
else:
    full_url = lname + "?" + query_string

# 🔹 Hacemos la solicitud a la API usando la URL construida

request = urllib.request.urlopen(full_url, context=ctx)  # Abrimos la URL
raw_data = request.read().decode()  # Leemos la respuesta y la convertimos de bytes a texto (string)

# 🔹 Convertimos el texto JSON en un diccionario de Python

info = json.loads(raw_data)  # Convierte algo como '{"name":"juan","age":34}' en un diccionario real
pretty_info = json.dumps(info, indent=4)  # (Opcional) Formatea los datos con sangría para que se vean bonitos

# 🔹 Extraemos los datos que queremos mostrar: nombre y edad

name = info['name']  # Tomamos el valor asociado a la clave 'name'
age = info['age']    # Tomamos el valor asociado a la clave 'age'

# 🔹 Imprimimos la información en consola

print("------------------------------\n")
print(f"NAME:  {name}\n")           # Mostramos el nombre
print(f"FORECASTED AGE:  {age}")    # Mostramos la edad estimada
