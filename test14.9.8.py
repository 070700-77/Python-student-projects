import urllib.request, urllib.parse, urllib.error
import json
import ssl
import sys

API_KEY = "911a3c8e59c9408286053ac595221028"          # Paso 1
BASE_URL = "https://randommer.io/api/Name"

# 1️⃣  Pedimos y validamos opciones
valid_types = {"firstname", "surname", "fullname"}
name_type = input("Type (firstname / surname / fullname): ").strip().lower()
if name_type not in valid_types:
    sys.exit("❌  nameType no permitido.")

qty = input("How many names? (1‑100): ").strip()
if not qty.isdigit() or int(qty) < 1:
    sys.exit("❌  quantity debe ser un entero positivo.")

# 2️⃣  Construimos la URL
params = urllib.parse.urlencode({"nameType": name_type, "quantity": qty})
url = f"{BASE_URL}?{params}"
print("Generated URL →", url)

# 3️⃣  Preparamos la solicitud
req = urllib.request.Request(url)
req.add_header("accept", "*/*")                # Paso 2
req.add_header("X-Api-Key", API_KEY)

# (No desactivamos SSL – mantenemos seguridad)
ctx = ssl.create_default_context()

try:
    with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
        data = json.loads(resp.read().decode())
        print(json.dumps(data, indent=4))

except urllib.error.HTTPError as err:
    if err.code == 403:
        print("🔒 403 Forbidden – key inválida, cuota agotada o cabeceras incorrectas.")
    else:
        print(f"Error {err.code}: {err.reason}")
        print(err.read().decode())             # Muestra detalle del servidor
except Exception as ex:
    print("Error inesperado:", ex)
