#El programa funciona, pero para que se pueda ejecutar, tengo que suscribirme a la API: https://rapidapi.com/dpventures/api/wordsapi/playground/54b863d2e4b0417be3482942

import urllib.request, urllib.parse, urllib.error
import ssl
import json
import os
import load_dotenv()

x_rapidapi_key = os.environ.get('x_rapidapi_key')

ctx = ssl.create_default_context()     # Crea un contexto SSL por defecto
ctx.check_hostname = False            # Desactiva la verificación del nombre del host en el certificado
ctx.verify_mode = ssl.CERT_NONE       # Desactiva la verificación de la validez del certificado

while True:
    word = input('Enter the word you are looking the meaning for: ')
    if len(word) < 1:
        print("Unvalid answer. Try again.\n")
        continue
    break
    
base_url = "https://wordsapiv1.p.rapidapi.com/words/"
    
request_protocol = base_url + word
req = urllib.request.Request(request_protocol)

req.add_header('X-RapidAPI-Key', x_rapidapi_key)
req.add_header("X-RapidAPI-Host", "wordsapiv1.p.rapidapi.com")
req.add_header("Accept",          "application/json")

try:
    get_info = urllib.request.urlopen(req, context=ctx)
    raw_info = get_info.read().decode()
    
    data = json.loads(raw_info)
    pretty_data =json.dumps(data, indent = 4)
    print(pretty_data)

except urllib.error.HTTPError as e:
    print(f"Error: {e.code} - {e.reason}")  # Imprimimos el código y la causa del error (por ejemplo, 404 Not Found)
    print("There was a problem connecting to the API.")
    print("Please check that your API key is correct and that you have access to this endpoint.")

# 9) Manejamos cualquier otro tipo de error que no sea un HTTPError específico
except Exception as e:
    print(f"An unexpected error occurred: {e}")
