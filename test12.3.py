import xml.etree.ElementTree as ET
# Importamos la biblioteca `ElementTree` con el alias `ET`.
# Esta biblioteca nos permite trabajar con datos en formato XML, como analizarlos y extraer información.

data = '''
<usuarios>
    <usuario id="101">
        <nombre>Andrea</nombre>
        <apellido>Gomez</apellido>
        <contacto>
            <email>andrea.gomez@example.com</email>
            <telefono>123456789</telefono>
        </contacto>
        <edad>28</edad>
    </usuario>
    <usuario id="102">
        <nombre>Juan</nombre>
        <apellido>Pérez</apellido>
        <contacto>
            <email>juan.perez@example.com</email>
            <telefono>987654321</telefono>
        </contacto>
        <edad>35</edad>
    </usuario>
</usuarios>
'''
# Creamos una variable `data` que contiene un bloque de texto en formato XML.
# Este XML representa una lista de usuarios.
# Cada usuario está definido por:
# - Un atributo `id` que identifica al usuario.
# - Subelementos como `<nombre>`, `<apellido>`, `<contacto>` (que contiene `<email>` y `<telefono>`), y `<edad>`.

tree = ET.fromstring(data)
# Usamos `ET.fromstring(data)` para analizar el texto XML almacenado en `data`.
# Esto convierte el XML en un "árbol de elementos" que podemos recorrer y manipular.
# La raíz del XML (`<usuarios>`) se almacena en la variable `tree`.

users = tree.findall('usuario')
# Usamos `tree.findall('usuario')` para encontrar todos los elementos `<usuario>` dentro del árbol.
# Esto devuelve una lista de todos los usuarios como objetos `Element`.
# Guardamos esta lista en la variable `users`.

for item in users:
    # Iniciamos un bucle `for` para iterar sobre cada usuario en la lista `users`.
    # En cada iteración, `item` será un objeto `Element` que representa a un usuario individual.
    
    user_id = int(item.get('id'))
    # Usamos `item.get('id')` para obtener el valor del atributo `id` del usuario.
    # Este valor se devuelve como una cadena de texto, así que lo convertimos en un entero con `int()`.
    # Por ejemplo, para el primer usuario, esto devuelve 101.
    # Guardamos el resultado en la variable `user_id`.

    name = item.find('nombre').text
    # Usamos `item.find('nombre')` para buscar el subelemento `<nombre>` dentro del usuario.
    # Usamos `.text` para extraer el texto que contiene (por ejemplo, "Andrea").
    # Guardamos el nombre en la variable `name`.

    last_name = item.find('apellido').text
    # Similar al nombre, usamos `item.find('apellido')` para buscar el subelemento `<apellido>` y extraemos su texto.
    # Por ejemplo, "Gomez".
    # Guardamos el apellido en la variable `last_name`.

    contact = item.find('contacto')
    # Usamos `item.find('contacto')` para buscar el subelemento `<contacto>`, que contiene más información como `<email>` y `<telefono>`.
    # Guardamos el elemento completo `<contacto>` en la variable `contact`.

    email = contact.find('email').text
    # Dentro del elemento `<contacto>`, buscamos el subelemento `<email>` con `contact.find('email')`.
    # Usamos `.text` para extraer el texto que contiene (por ejemplo, "andrea.gomez@example.com").
    # Guardamos el correo electrónico en la variable `email`.

    cel = contact.find('telefono').text
    # Similar al correo electrónico, usamos `contact.find('telefono')` para buscar el subelemento `<telefono>`.
    # Usamos `.text` para extraer el texto del número de teléfono (por ejemplo, "123456789").
    # Guardamos el número de teléfono en la variable `cel`.

    age = int(item.find('edad').text)
    # Usamos `item.find('edad')` para buscar el subelemento `<edad>` dentro del usuario.
    # Usamos `.text` para extraer el texto que contiene (la edad) y lo convertimos en un número entero con `int()`.
    # Por ejemplo, 28 para el primer usuario.
    # Guardamos la edad en la variable `age`.

    print(user_id)
    print(name)
    print(last_name)
    print(age)
    print(email)
    print(cel)