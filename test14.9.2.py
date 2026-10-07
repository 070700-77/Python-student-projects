# Este programa se conecta a una API financiera para buscar información de empresas por su ticker o nombre.
# Usa la API: https://financialmodelingprep.com/api/v3/search-ticker

# 🔹 Módulos necesarios para conectarse a internet, manejar errores y procesar datos JSON
import urllib.request  # Permite abrir URLs y descargar contenido
import urllib.parse    # Permite construir y codificar parámetros en URLs
import urllib.error    # Maneja errores al hacer peticiones a internet

import json            # Nos permite trabajar con datos en formato JSON
import ssl             # Permite manejar conexiones HTTPS seguras

import os
import load_dotenv()

load_dotenv()
api_key = os.environ.get('api_key')

# 🔹 Crear un "contexto SSL" para evitar errores con certificados al abrir URLs seguras (https)
ctx = ssl.create_default_context()    # Crea un contexto seguro para conexiones
ctx.check_hostname = False            # No revisa el nombre del servidor en el certificado
ctx.verify_name = ssl.CERT_NONE       # Ignora problemas de validez del certificado SSL


# 🔹 Bucle para pedir al usuario que escriba la URL base de la API
while True:
    lname = input('Enter API URL: ')   # Por ejemplo: https://financialmodelingprep.com/api/v3/search-ticker
    if len(lname) < 1:                 # Si no escribió nada, mostramos error
        print("Invalid URL. Try again. \n")
        continue                       # Repetimos la solicitud
    break                              # Salimos si la URL es válida

# 🔹 Bucle para pedir el nombre de la empresa o su símbolo en bolsa (ticker)
while True:
    query = input('Enter Ticker or Company name: ')  # Ej: AAPL, Apple, TSLA, Tesla
    if len(query) < 2:                # Verificamos que el input tenga al menos 2 caracteres
        print('Invalid input. Try again. \n')
        continue
    break

# 🔹 Bucle para pedir cuántos resultados se quieren mostrar en pantalla
while True:
    q_list = int(input('Enter the number of cassualities shown in the screen: '))  # Número de resultados deseados
    if q_list < 1:
        print('Invalid input. Try again. \n')
        continue
    break

# 🔹 Campo opcional para ingresar el nombre de la bolsa de valores (NYSE, NASDAQ, etc.)
market = input('Enter the stock market where the company its being traded (OPTIONAL): ')

# 🔹 Diccionario con los parámetros a enviar en la URL
params = {
    "query": query,     # Nombre o ticker
    "limit": q_list     # Cuántos resultados mostrar
}
if market:
    params['exchange'] = market  # Si el usuario escribió el nombre del mercado, lo agregamos

# 🔹 Convertimos los parámetros en una cadena de texto válida para una URL
# Ejemplo: query=apple&limit=5&exchange=NASDAQ
query_string = urllib.parse.urlencode(params)

# 🔹 Verificamos si la URL ya tiene un "?" (parámetro incluido)
if "?" in lname:
    # Si ya tiene "?", añadimos nuevos parámetros con "&"
    full_url = lname + "&" + query_string + f"&apikey={api_key}"
else:
    # Si no tiene "?", la iniciamos con "?" y luego añadimos los parámetros
    full_url = lname + "?" + query_string + f"&apikey={api_key}"

# 🔹 Mostramos la URL final que será usada para hacer la solicitud
print("👉 Full URL:", full_url)

# 🔹 Hacemos la solicitud a la API
url_with_params = urllib.request.urlopen(full_url, context=ctx)  # Abrimos la URL con los parámetros

# 🔹 Leemos y decodificamos la respuesta JSON
raw_data = url_with_params.read().decode()

# 🔹 Convertimos el texto JSON en un diccionario o lista de Python
info = json.loads(raw_data)

# 🔹 Opcional: version bonita del JSON (para depuración, no se imprime aquí)
pretty_info = json.dumps(info, indent=4)

# 🔹 Recorremos los resultados obtenidos (cada uno es una empresa)
for item in info:
    symbol = item['symbol']  # Ticker (ej: AAPL)
    name = item['name']  # Nombre completo (ej: Apple Inc)
    currency = item['currency']  # Moneda en la que cotiza (USD, EUR)
    stock = item['stockExchange']  # Bolsa de valores (ej: Nasdaq Global Select)
    abreviated_name = item['exchangeShortName']  # Abreviación del mercado (ej: NASDAQ)

    # 🔹 Mostramos los datos obtenidos de cada empresa
    print("📈 Empresa Encontrada")
    print("🧾 Nombre completo: ", name)
    print("🔤 Ticker: ", symbol)
    print("💲 Moneda: ", currency)
    print("🏛️ Bolsa de valores: ", stock)
    print("📍 Abreviación de mercado: ", abreviated_name)
    print("--------------------------------------------------")
