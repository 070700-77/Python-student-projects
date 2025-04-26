#Works with the following API URL: https://rickandmortyapi.com/api

# Este programa interactúa con la API pública de Rick and Morty para consultar información de personajes usando sus IDs.

# Importamos los módulos necesarios para hacer peticiones web y procesar respuestas en formato JSON

import urllib.request   # Permite abrir URLs y descargar contenido (como HTML o JSON)
import urllib.parse     # (No se usa aquí) Sirve para codificar parámetros en URLs
import urllib.error     # Permite manejar errores si la conexión falla

import json             # Nos permite trabajar con archivos o respuestas en formato JSON (estructura de texto tipo diccionario)

import ssl              # Nos permite establecer conexiones HTTPS ignorando errores de certificados

# Creamos un "contexto SSL" que se va a usar para evitar problemas de seguridad con certificados SSL (cuando accedemos a una URL HTTPS)
ctx = ssl.create_default_context()         # Creamos el objeto de contexto seguro
ctx.check_hostname = False                 # Le decimos que no verifique el nombre del host (servidor)
ctx.verify_name = ssl.CERT_NONE            # Le decimos que ignore por completo si el certificado no es válido

params = []  # Creamos una lista vacía donde vamos a guardar los IDs que el usuario escriba

# 🔹 PRIMER BUCLE: Pedimos al usuario la URL base de la API
while True:
    api_base_endopint = input('Enter API URL: ')  # Solicitamos al usuario que ingrese la URL (ej: https://rickandmortyapi.com/api)
    api_base_endopint = api_base_endopint.strip()  # .strip() elimina los espacios al inicio y al final del texto ingresado

    if len(api_base_endopint) < 1:  # Si el usuario no escribió nada...
        print("Invalid URL. Try again, please. \n")
        continue  # ...le volvemos a pedir que lo intente
    break  # Si la URL es válida, salimos del bucle

# 🔹 SEGUNDO BUCLE: Permitimos al usuario ingresar uno o varios IDs de personajes
while True:
    character_id = input('Enter user ID: ')  # Solicitamos al usuario que escriba el ID del personaje (ej: 1, 2, 35)

    # Verificamos que haya ingresado algo y que ese algo sea un número usando .isdigit()
    if len(character_id) < 1 or not character_id.strip().isdigit():
        print("Invalid ID. Try again, please. \n")
        continue  # Si no es válido, volvemos a empezar

    params.append(character_id.strip())  # Agregamos el ID a la lista de parámetros

    # Preguntamos al usuario si quiere ingresar otro personaje (y = sí, n = no)
    answer = input('Do you want to get info on another Rick And Morty character? (y/n): ').lower()
    if answer == 'y':
        continue  # Si responde "y", repetimos el bucle
    else:
        break  # Si responde otra cosa, salimos

# Unimos todos los IDs con comas usando ",".join() y los colocamos al final de la URL
# Ejemplo: "https://rickandmortyapi.com/api/character/1,2,3"
base_url = api_base_endopint + "/character/" + ",".join(params)

# Hacemos la solicitud a la URL construida
raw_data = urllib.request.urlopen(base_url, context=ctx)  # Abrimos la URL con contexto SSL para evitar errores
data = raw_data.read().decode()  # Leemos el contenido (en bytes) y lo decodificamos a texto plano (string)

# Cargamos la respuesta JSON (texto) como un diccionario de Python
info = json.loads(data)

# Formateamos el diccionario en un formato legible para impresión (con indentación)
pretty_info = json.dumps(info, indent=4)  # Esto no se usa en pantalla, pero puede servir para depuración

# Si el usuario ingresó más de un ID, la API devuelve una lista de personajes
if len(params) > 1:
    characters = info  # Ya está en formato lista
else:
    characters = [info]  # Convertimos el único personaje en una lista con un solo elemento para poder recorrerlo igual

# 🔹 Recorremos todos los personajes y extraemos su información
for item in characters:
    c_id = item['id']  # ID del personaje
    name = item['name']  # Nombre completo
    status = item['status']  # Estado: Alive, Dead, unknown
    species = item['species']  # Especie: Human, Alien, etc.
    typee = item['type']  # Tipo: en algunos casos está vacío
    gender = item['gender']  # Género: Male, Female, Genderless, unknown

    # ORIGEN: es un diccionario dentro del diccionario principal
    origin = item['origin']
    o_name = origin['name']  # Nombre del planeta o universo de origen
    o_url = origin['url']    # URL con más información sobre el origen

    # UBICACIÓN ACTUAL: accedemos directamente con notación en cadena
    location_name = item['location']['name']
    location_url = item['location']['url']

    # Mostramos los datos de manera clara y decorativa
    print("🧬 Personaje Encontrado")
    print(f"🆔 ID: {c_id}")
    print(f"👤 Nombre: {name}")
    print(f"📊 Estado: {status}")
    print(f"🧪 Especie: {species}")
    print(f"🔎 Tipo: {typee}")
    print(f"🚻 Género: {gender}")
    print(f"🌍 Origen: {o_name}")
    print(f"📍 Última ubicación conocida: {location_name}")
    print("🎬 Aparece en episodios:")

    # La clave 'episode' es una lista con URLs de episodios donde aparece el personaje
    for ep in item['episode']:
        print(f"   - {ep}")

    # Imprimimos el link de la imagen del personaje
    print("🖼️ Imagen: ", item['image'])
    print("--------------------------------------------------")

        