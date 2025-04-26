# 🔹 Importamos módulos necesarios para trabajar con solicitudes a internet y datos JSON

import urllib.request, urllib.error, urllib.parse  
# `urllib.request`: Permite abrir URLs y obtener datos de internet.
# `urllib.error`: Permite capturar errores si algo sale mal en la conexión.
# `urllib.parse`: Se puede usar para construir o codificar URLs, aunque no se usa en este código.

import json  
# `json` nos permite trabajar con datos en formato JSON, que es como un diccionario de texto.
# Este formato es usado frecuentemente por APIs (servicios web) para compartir datos.

import ssl  
# `ssl` permite manejar conexiones HTTPS (seguras). Lo usamos aquí para ignorar errores de certificado.

# 🔹 Creamos un contexto SSL para evitar errores por certificados inválidos

ctx = ssl.create_default_context()  # Creamos el contexto seguro para HTTPS.
ctx.check_hostname = False          # No verificamos el nombre del servidor en el certificado.
ctx.verify_name = ssl.CERT_NONE     # Ignoramos cualquier problema con la validez del certificado.

# 🔹 Mostramos el menú principal al usuario

print('------------------------------------------')
print('MENU\n')
print('1) Check available currencies')  # Opción 1: Ver lista de monedas disponibles.
print('2) Get the currency list with your desired currency as the base one')  # Opción 2: Ver tasas de cambio respecto a una moneda base.

# 🔹 Bucle para pedir una opción válida al usuario
while True:
    try:
        opt = int(input('Select an option: '))  # Pedimos al usuario que elija una opción y la convertimos en número.
    except:
        # Si el usuario no escribe un número, mostramos mensaje de error.
        print("Invalid selection. Select the number of the desired option. \n")
        continue  # Volvemos a mostrar el menú.

    if opt == 1 or opt == 2:
        # Si el número ingresado es válido (1 o 2), salimos del bucle.
        break
    else:
        # Si el número es incorrecto, mostramos error y volvemos a pedir opción.
        print("Invalid selection. Select the number of the desired option. \n")
        continue

# 🔹 Si el usuario eligió la opción 1: Mostrar todas las monedas disponibles

if opt == 1:
    # URL de la API que contiene el listado de monedas (códigos y nombres)
    base_url = 'https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies.json'
    
    raw_data = urllib.request.urlopen(base_url, context=ctx)  # Abrimos la URL y pedimos los datos.
    
    data = raw_data.read().decode()  # Leemos la respuesta y la convertimos de bytes a texto.
    
    info = json.loads(data)  # Convertimos el texto JSON en un diccionario de Python.
    pretty_info = json.dumps(info, indent=4)  # (Opcional) Formateamos los datos de forma legible.

    # Imprimimos la lista de monedas disponibles
    print("\n💱 Lista de monedas disponibles:")
    print("🌍 Código  -  Nombre")
    print("----------------------------------")
    for code, name in info.items():  # Recorremos el diccionario {codigo: nombre}
        print(f"🔹 {code.upper()}  -  {name.capitalize()}")  # Mostramos cada código en mayúsculas y su nombre en formato bonito.

# 🔹 Si el usuario eligió la opción 2: Mostrar tasas de cambio respecto a una moneda base

if opt == 2:
    # URL base que cambia dependiendo de la moneda elegida por el usuario
    base_url = 'https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/'

    # Bucle para pedir una moneda base válida al usuario
    while True:
        currency = input('Enter the symbol of the base currency you want to compare: ')  # Ej: usd, eur, mxn
        if len(currency) < 1:
            print('Invalid input. Try again.\n')  # Si el campo está vacío, mostramos error.
            continue
        break  # Salimos del bucle si el usuario ingresó algo.

    # Creamos la URL final añadiendo la moneda base y la extensión .json
    # Ejemplo: https://.../currencies/usd.json
    full_url = base_url + currency + '.json'

    request = urllib.request.urlopen(full_url, context=ctx)  # Abrimos la URL y pedimos los datos.

    data = request.read().decode()  # Leemos la respuesta y la convertimos a texto.

    info = json.loads(data)  # Convertimos el texto JSON en un diccionario.

    pretty_info = json.dumps(info, indent=4)  # (Opcional) Formateamos el diccionario en texto legible.

    # Extraemos del JSON la sección con las tasas de conversión.
    # info['usd'] o info['eur'], etc.
    conversions = info.get(currency.lower(), {})  # Usamos .get() por si no existe esa clave.
    fecha = info.get("date", "Desconocida")  # Obtenemos la fecha del tipo de cambio.

    # Recorremos y mostramos todas las conversiones
    for other_code, rate in conversions.items():
        print(f"💵 1 {currency.upper()} = {rate} {other_code.upper()}")  # Ej: 1 USD = 0.92 EUR

    # Mostramos la fecha de la información
    print(f"\n📅 Fecha de los datos: {fecha}")

    
    
    