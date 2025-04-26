import xml.etree.ElementTree as ET
# Importamos la biblioteca `xml.etree.ElementTree` con el alias `ET`.
# Esta biblioteca nos permite analizar datos en formato XML y trabajar con ellos como objetos en Python.

data = '''<?xml version="1.0"?>
<productos>
    <producto id="001">
        <nombre>Cafetera</nombre>
        <precio>120.00</precio>
        <cantidad>10</cantidad>
        <especificaciones>
            <color>Negro</color>
            <voltaje>120V</voltaje>
        </especificaciones>
        <comentarios>
            <comentario autor="Ana">Muy buena cafetera, funciona bien.</comentario>
            <comentario autor="Pedro">Podría ser más barata.</comentario>
        </comentarios>
    </producto>
    <producto id="002">
        <nombre>Teclado Mecánico</nombre>
        <precio>80.50</precio>
        <cantidad>15</cantidad>
        <especificaciones>
            <tipo>RGB</tipo>
            <idioma>ES</idioma>
        </especificaciones>
        <comentarios>
            <comentario autor="Luis">Excelente para gaming.</comentario>
        </comentarios>
    </producto>
</productos>
'''
# Creamos una variable `data` que contiene un bloque de texto en formato XML.
# Este XML representa una lista de productos, donde:
# - `<productos>` es el elemento raíz que contiene todos los productos.
# - `<producto>` representa cada producto con información como su nombre, precio, cantidad, especificaciones y comentarios.

tree = ET.fromstring(data)
# Convertimos el texto XML en un árbol de elementos con `ET.fromstring(data)`.
# Este árbol es una estructura jerárquica donde cada etiqueta XML se convierte en un objeto manipulable.
# El elemento raíz (`<productos>`) se almacena en la variable `tree`.

products = tree.findall('producto')
# Usamos `tree.findall('producto')` para buscar todos los elementos `<producto>` dentro del árbol.
# Esto devuelve una lista de todos los productos como objetos `Element`.
# Guardamos esta lista en la variable `products`.

for item in products:
    # Iniciamos un bucle `for` para recorrer cada producto en la lista `products`.
    # Cada iteración trabaja con un elemento `<producto>` (almacenado en la variable `item`).
    
    prod_id = item.get('id')
    # Usamos `item.get('id')` para obtener el valor del atributo `id` del producto.
    # Por ejemplo, para el primer producto, devuelve "001".
    # Este valor se guarda en la variable `prod_id`.
    
    name = item.find('nombre').text
    # Usamos `item.find('nombre')` para buscar el subelemento `<nombre>` dentro del producto.
    # Usamos `.text` para extraer el texto que contiene, que es el nombre del producto.
    # Por ejemplo, "Cafetera".
    # Guardamos el texto en la variable `name`.
    
    price = float(item.find('precio').text)
    # Usamos `item.find('precio')` para buscar el subelemento `<precio>` y extraer su texto con `.text`.
    # Convertimos el texto a un número decimal con `float()`.
    # Guardamos el precio en la variable `price`.

    quantity = int(item.find('cantidad').text)
    # Usamos `item.find('cantidad')` para buscar el subelemento `<cantidad>` y extraemos su texto.
    # Convertimos el texto a un número entero con `int()`.
    # Guardamos la cantidad en la variable `quantity`.

    specify = item.find('especificaciones')
    # Usamos `item.find('especificaciones')` para buscar el subelemento `<especificaciones>`.
    # Este elemento contiene subelementos como `<color>` o `<voltaje>`.
    # Guardamos este subelemento en la variable `specify`.

    colour_tag = specify.find('color')
    # Buscamos el subelemento `<color>` dentro de `specify` con `specify.find('color')`.
    # Si el subelemento `<color>` no existe, `find` devuelve `None`.
    # Guardamos el subelemento (o `None`) en la variable `colour_tag`.

    volts_tag = specify.find('voltaje')
    # Similar a `colour_tag`, buscamos el subelemento `<voltaje>` dentro de `specify`.
    # Guardamos el subelemento (o `None`) en la variable `volts_tag`.

    colour = colour_tag.text if colour_tag is not None else "N/A"
    # Si `colour_tag` no es `None`, extraemos su texto con `.text`.
    # Si es `None` (es decir, el subelemento `<color>` no existe), usamos "N/A" como valor predeterminado.
    # Guardamos el resultado en la variable `colour`.

    volts = volts_tag.text if volts_tag is not None else "N/A"
    # Hacemos lo mismo que con `colour`, pero para el voltaje.
    # Si `<voltaje>` no existe, usamos "N/A" como valor predeterminado.
    # Guardamos el resultado en la variable `volts`.

    comments = item.find('comentarios').findall('comentario')  
     # Usamos `item.find('comentarios')` para buscar el subelemento `<comentarios>`.
    # Dentro de este elemento, usamos `.findall('comentario')` para obtener todos los subelementos `<comentario>`.
    # Esto devuelve una lista de comentarios como objetos `Element`.
    # Guardamos esta lista en la variable `comments`.

    print("-------------------------------------")
    print("")
    print("")
    print(f"ID del producto: {prod_id} \nNombre del producto: {name} \nPrecio: {price:.2f}\nCantidad disponible: {quantity}")
    # Imprimimos la información básica del producto: su ID, nombre, precio (formateado con 2 decimales) y cantidad disponible.
    
    print(f"Especificaciones\nColor: {colour} \nVoltaje: {volts}")
    # Imprimimos las especificaciones del producto, como el color y el voltaje.
    # Si alguno de estos no está disponible, se mostrará "N/A".
    
    print("")
    print(f"Reviews\n")
    parts = len(comments)
    # Calculamos cuántos comentarios hay en la lista `comments` usando `len()`.
    # Guardamos este número en la variable `parts`.
    
    print(f"{parts}")
    # Imprimimos la cantidad total de comentarios.
    
    for review in comments:
        # Iniciamos un bucle `for` para recorrer cada comentario en la lista `comments`.
        
        review_x= review.get('autor')
        # Usamos `review.get('autor')` para obtener el valor del atributo `autor` del comentario.
        # Por ejemplo, "Ana" o "Pedro".
        # Guardamos el autor en la variable `review_x`.

        message_x = review.text
        # Usamos `.text` para extraer el texto del comentario (el mensaje escrito por el autor).
        # Por ejemplo, "Muy buena cafetera, funciona bien."
        # Guardamos el mensaje en la variable `message_x`.
        
        print(f"Autor: {review_x}\nComentario: {message_x}")
        # Imprimimos el autor y el mensaje del comentario.
    