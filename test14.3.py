# Programa desarrollado para intentar acceder a la API de Marvel

# 🔹 Módulos necesarios para conectarse a la web, manejar URLs y trabajar con datos JSON
import urllib.request    # Permite abrir URLs y leer contenido desde internet
import urllib.parse      # Sirve para codificar parámetros y crear URLs válidas
import urllib.error      # Permite capturar errores si la solicitud a una URL falla
import os
import load_dotenv()

from bs4 import BeautifulSoup  # Se usa para analizar HTML o XML, aunque aquí no lo estamos usando realmente

import json             # Permite trabajar con datos en formato JSON (muy común en APIs)
import hashlib          # Permite crear "hashes", una forma segura de cifrado de datos
import time             # Permite acceder a la hora actual (timestamps)

import ssl              # Permite manejar conexiones HTTPS (seguras)

load_dotenv()

marvel_key = os.environ.get('marvel_key')

# 🔹 Configuración SSL para evitar errores por certificados de seguridad no válidos
ctx = ssl.create_default_context()     # Crea un "contexto seguro" para conexiones HTTPS
ctx.check_hostname = False             # Desactiva la verificación del nombre del servidor
ctx.verify_name = ssl.CERT_NONE        # Ignora cualquier error de verificación SSL

# 🔹 Claves necesarias para acceder a la API de Marvel (debes registrarte para obtener las tuyas)
public_key = "8e73048904bf7ea3a8dfdc24001aae69"     # Tu clave pública (se puede mostrar)
private_key = marvel_key # Tu clave privada (secreta y personal)

# 🔹 Pedimos al usuario que ingrese el link base de la API que desea consultar
while True:
    raw_url = input('Enter API link: ')  # Ejemplo: https://gateway.marvel.com/v1/public/characters
    if len(raw_url) < 1:                 # Si el campo está vacío, mostramos error
        print('Invalid URL. Try again')
        continue                         # Volvemos a pedirlo
    base_url = raw_url                   # Guardamos la URL como base
    break                                # Salimos del bucle si el input es válido

# 🔹 Creamos un timestamp (marca de tiempo actual)
# La API de Marvel lo requiere para generar una "firma segura"
ts = str(time.time())  # Obtenemos el tiempo actual (en segundos) y lo convertimos a string

# 🔹 Creamos el hash requerido por Marvel (md5 de timestamp + clave privada + clave pública)
# Esto sirve como una firma digital para autorizar el acceso a la API
hash_value = hashlib.md5((ts + private_key + public_key).encode('utf-8')).hexdigest()

# 🔹 Creamos un diccionario con los parámetros que Marvel requiere en la URL
params = {
    'ts': ts,              # Timestamp
    'apikey': public_key,  # Tu clave pública
    'hash': hash_value     # Hash generado con tus claves y timestamp
}

# 🔹 Convertimos el diccionario de parámetros en una cadena que se pueda añadir a la URL
# Por ejemplo, se convierte en: ts=123456&apikey=abc123&hash=xyz456
query_string = urllib.parse.urlencode(params)

# 🔹 Unimos la URL base con los parámetros para crear la URL completa a la que haremos la solicitud
if '?' in base_url:
    url_with_params = base_url + "&" + query_string  # Si ya hay parámetros en la URL, añadimos con "&"
else:
    url_with_params = base_url + "?" + query_string  # Si no hay parámetros, los añadimos con "?"

# 🔹 Hacemos la solicitud a la URL completa y recibimos la respuesta
url = urllib.request.urlopen(url_with_params, context=ctx)  # Abrimos la URL con contexto SSL

# 🔹 Leemos los datos recibidos y los decodificamos de bytes a texto
data = url.read().decode()  # Convertimos el contenido recibido a string

# 🔹 Convertimos el texto (que está en formato JSON) a un diccionario de Python
info = json.loads(data)

# 🔹 (Opcional) Formateamos el JSON de forma legible, con sangrías para imprimirlo bonito
sorted_info = json.dumps(info, indent=4)

# 🔹 Mostramos en pantalla la respuesta completa de la API
print(sorted_info)
