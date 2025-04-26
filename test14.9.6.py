# Comentarios principales:
# ---------------------------------------------------------------------------
# Este programa realiza una solicitud a un API privado de 'tradewatch.io'
# para obtener información sobre una materia prima (commodity).
# Se incluye una API key y se construye la URL en función del 'symbol' que ingrese el usuario.
# ---------------------------------------------------------------------------

# private API KEY: tuRMJ1YWekWubi14CSu4jKaLYcEh2dBn   # Clave para autenticar el acceso al API
# Base API endpoint: https://api.tradewatch.io/      # Punto base de acceso al servicio

# 1) Importamos módulos necesarios para trabajar con JSON y con solicitudes HTTP/HTTPS
import json                                        # Módulo para trabajar con datos en formato JSON
import urllib.request, urllib.parse, urllib.error  # Módulos para hacer solicitudes y manejar errores
import ssl                                         # Módulo para manejar conexiones seguras (SSL/TLS)

# 2) Configuramos el "contexto SSL" para manejar conexiones HTTPS sin verificar el certificado (no recomendable en prod)
ctx = ssl.create_default_context()     # Crea un contexto SSL por defecto
ctx.check_hostname = False            # Desactiva la verificación del nombre del host en el certificado
ctx.verify_mode = ssl.CERT_NONE       # Desactiva la verificación de la validez del certificado

# 3) Usamos un bucle "while True" para solicitar repetidamente un símbolo (commodity)
#    hasta que el usuario ingrese algo válido (no vacío).
while True:
    symbol = input('Enter the commodity symbol u want info about: ')  # Pedimos al usuario el símbolo
    if len(symbol) < 1:                                              # Si el usuario deja el campo vacío
        print('Invalid symbol. Try again. \n')                       # Mostramos error y volvemos a pedir
        continue                                                     # "continue" hace que se reinicie el bucle
    break                                                            # Si el símbolo es válido, salimos del bucle

# 4) Construimos la URL dinámica que usaremos en la solicitud
#    Usamos una f-string para insertar el valor de 'symbol' dentro de la ruta.
request_protocol = f'https://api.tradewatch.io/commodities/symbols/{symbol}'

# 5) Creamos un objeto 'Request' y configuramos las cabeceras necesarias para llamar al API
req = urllib.request.Request(request_protocol)                  # Creamos la solicitud con la URL ya construida
req.add_header('api-key', 'tuRMJ1YWekWubi14CSu4jKaLYcEh2dBn')    # Agregamos la clave de acceso al API
req.add_header('Accept', 'application/json')                    # Recomendamos que el servidor responda en formato JSON

# 6) Imprimimos la URL generada (opcional; útil para verificar que sea correcta)
print('generated URL: ', request_protocol)

# 7) Intentamos hacer la solicitud y manejar errores
try:
    # 7.1) Abrimos la URL con las credenciales y el contexto SSL configurado
    get_info = urllib.request.urlopen(req, context=ctx)
    # 7.2) Leemos la respuesta (raw_info) en bytes y la convertimos a string
    raw_info = get_info.read().decode()
    # 7.3) Cargamos la cadena de texto JSON en un diccionario de Python
    data = json.loads(raw_info)
    # 7.4) Convertimos ese diccionario a una cadena JSON con indentaciones para mejor lectura
    pretty_data = json.dumps(data, indent=4)
    # 7.5) Finalmente, imprimimos en pantalla la información formateada
    print(pretty_data)

# 8) Manejamos errores específicos de tipo HTTP (como 404, 401, etc.)
except urllib.error.HTTPError as e:
    print(f"Error: {e.code} - {e.reason}")  # Imprimimos el código y la causa del error (por ejemplo, 404 Not Found)
    print("There was a problem connecting to the API.")
    print("Please check that your API key is correct and that you have access to this endpoint.")

# 9) Manejamos cualquier otro tipo de error que no sea un HTTPError específico
except Exception as e:
    print(f"An unexpected error occurred: {e}")
