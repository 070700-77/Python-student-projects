# Works with:  http://universities.hipolabs.com/search
# Este programa consulta una API pública que devuelve una lista de universidades por país.

# 🔹 Importamos los módulos necesarios para hacer solicitudes web, manejar errores y trabajar con datos JSON

import urllib.request   # Sirve para abrir URLs desde Python (como un navegador pero por código)
import urllib.parse     # Sirve para codificar parámetros dentro de URLs, como country=Colombia
import urllib.error     # Permite detectar errores cuando fallan las conexiones

import ssl              # Para manejar conexiones HTTPS seguras (aunque aquí la URL es HTTP, lo dejamos por compatibilidad)
import json             # Para procesar datos en formato JSON (texto estructurado, tipo diccionario)

# 🔹 Creamos un contexto SSL para ignorar errores de certificados digitales
ctx = ssl.create_default_context()    # Creamos una "configuración de seguridad" para HTTPS
ctx.check_hostname = False            # No revisamos si el certificado coincide con el dominio
ctx.verify_name = ssl.CERT_NONE       # No validamos el certificado en sí

# 🔹 PRIMER BUCLE: Pedimos al usuario la URL base de la API
while True:
    lname = input('Enter API URL: ')   # Ejemplo: http://universities.hipolabs.com/search
    if len(lname) < 1:                 # Si el usuario no escribe nada...
        print('Invalid URL. Try again. \n')
        continue                       # Repetimos la pregunta
    break                              # Si escribió algo, salimos del bucle

# 🔹 SEGUNDO BUCLE: Pedimos al usuario el nombre del país
while True:
    country = input('Enter the Country of which you want the list of universities: ')
    if len(country) < 1:              # Validamos que el nombre no esté vacío
        print("Invalid Country. Try again. \n")
        continue
    break

# 🔹 Creamos un diccionario para guardar los parámetros de búsqueda
params = {}
params['country'] = country   # Guardamos el país con la clave 'country'

# 🔹 Codificamos ese diccionario para incluirlo en una URL
# Ejemplo: {'country': 'Colombia'} → 'country=Colombia'
query_string = urllib.parse.urlencode(params)

# 🔹 Unimos la URL base con los parámetros para crear la URL final
if "?" in lname:
    full_url = lname + "&" + query_string    # Si ya hay parámetros en la URL, usamos "&"
else:
    full_url = lname + "?" + query_string    # Si no hay parámetros, usamos "?"

# 🔹 Hacemos la solicitud a la URL completa y obtenemos los datos
info = urllib.request.urlopen(full_url, context=ctx)  # Abrimos la URL
raw_data = info.read().decode()  # Leemos la respuesta y la convertimos de bytes a texto

# 🔹 Convertimos el texto (en formato JSON) a una lista de diccionarios de Python
data = json.loads(raw_data)

# 🔹 Opcional: mostramos el contenido de forma bonita (aunque no se imprime aquí)
pretty_data = json.dumps(data, indent=4)

# 🔹 Inicializamos un contador de universidades
count = 0

# 🔹 Recorremos la lista de universidades obtenidas
for item in data:
    wpage = item['web_pages'][0]         # Tomamos la primera página web
    u_name = item['name']                # Nombre de la universidad
    u_country = item['country']          # País
    domains = item['domains']            # Lista de dominios
    state = item['state-province']       # Estado o provincia

    if state is None:                    # Si no hay estado definido, lo marcamos como "Unknown"
        state = "Unknown"

    count += 1                           # Aumentamos el contador

    # 🔹 Mostramos los datos de la universidad
    print("Numero: ", count)
    print("🏫 Universidad: ", u_name)
    print("🌍 País: ", u_country)
    print("📍 Provincia/Estado: ", state)
    print("🔗 Sitio web: ", wpage)
    print("🌐 Dominio(s): ", ", ".join(domains))  # Convertimos la lista de dominios en una cadena
    print("--------------------------------------------------")

# 🔹 Al final, mostramos cuántas universidades se encontraron
print('Total universidades encontradas: ', count)
