import xml.etree.ElementTree as ET
data = '''<biblioteca>
    <libros>
        <libro id="001">
            <titulo>Cien años de soledad</titulo>
            <autor>Gabriel García Márquez</autor>
            <categoria>Narrativa</categoria>
            <disponible>Si</disponible>
            <prestamos>
                <prestamo>
                    <usuario>Andrea Gomez</usuario>
                    <fecha_inicio>2025-01-15</fecha_inicio>
                    <fecha_fin>2025-02-15</fecha_fin>
                </prestamo>
                <prestamo>
                    <usuario>Juan Pérez</usuario>
                    <fecha_inicio>2025-03-01</fecha_inicio>
                    <fecha_fin>2025-03-30</fecha_fin>
                </prestamo>
            </prestamos>
        </libro>
        <libro id="002">
            <titulo>El Hobbit</titulo>
            <autor>J.R.R. Tolkien</autor>
            <categoria>Fantasía</categoria>
            <disponible>No</disponible>
            <prestamos>
                <prestamo>
                    <usuario>Laura Martinez</usuario>
                    <fecha_inicio>2025-04-20</fecha_inicio>
                    <fecha_fin>2025-05-20</fecha_fin>
                </prestamo>
            </prestamos>
        </libro>
    </libros>
    <usuarios>
        <usuario id="101">
            <nombre>Andrea Gomez</nombre>
            <telefono>123456789</telefono>
            <email>andrea.gomez@example.com</email>
            <prestamos_activos>1</prestamos_activos>
        </usuario>
        <usuario id="102">
            <nombre>Juan Pérez</nombre>
            <telefono>987654321</telefono>
            <email>juan.perez@example.com</email>
            <prestamos_activos>1</prestamos_activos>
        </usuario>
    </usuarios>
    <categorias>
        <categoria>
            <nombre>Narrativa</nombre>
            <descripcion>Literatura en forma de prosa, principalmente narrativa, que puede ser en parte imaginaria.</descripcion>
        </categoria>
        <categoria>
            <nombre>Fantasía</nombre>
            <descripcion>Género de ficción que utiliza la magia u otros elementos sobrenaturales como parte principal del argumento, la temática o el ambiente.</descripcion>
        </categoria>
    </categorias>
</biblioteca>'''

tree = ET.fromstring(data)

optns = [1,2,3,0]

print("MENU OPCIONES")
print("1). Ver inventario libros \n2). Ver lista de usuarios activos \n3). Informacion categorias disponibles \n0). Salir del programa")
print("")
while True:
    try:
        option = int(input("Selecciona el numero de la opcion que desees del menu: "))
        if option in optns:
            break
        else:
            print("Opcion invalida. intentalo de nuevo")
            continue
    except:
        print("Opcion invalida. intentalo de nuevo")
        print('')
        continue

while True:
    if option == 1:
        books = tree.findall('libros/libro')
        for item in books:
            book_id = int(item.get('id'))
            title =  item.find('titulo').text
            category = item.find('categoria').text
            loans = item.findall('prestamos/prestamo')
            print("--------------------------------------------------------")
            print("\n")
            print(f'ID: {book_id} \nTitulo: {title} \nCategoria: {category}')
            print("")
            for client in loans:
                user_book = client.find('usuario').text
                start_date = client.find('fecha_inicio').text
                end_date = client.find('fecha_fin').text
                print(f'Informacion alquiler \nNombre client@: {user_book} \nFecha de inicio del alquiler: {start_date} \nFecha de fin del alquiler: {end_date}')
                print("")
        option = 9
        continue
        

    if option == 2:    
        users = tree.findall('usuarios/usuario')
        for item in users:
            user_id = int(item.get('id'))
            name = item.find('nombre').text
            cel = int(item.find('telefono').text)
            email = item.find('email').text
            services = int(item.find('prestamos_activos').text)
            print("--------------------------------------------------------")
            print("\n")
            print(f'ID del usuario: {user_id} \nNombre del usuario: {name} \nNumero celular: {cel} \nEmail: {email} \nPrestamos activos: {services}')
            print("")
        option = 9
        continue

    if option == 3:   
        categories = tree.findall('categorias/categoria')
        for item in categories:
            category_name = item.find('nombre').text
            description = item.find('descripcion').text
            print("--------------------------------------------------------")
            print("\n")
            print(f'Nombre de la categoria: {category_name} \nDescripcion de la categoria: {description}')
            print("")
        option = 9
        continue

    if option == 9:
        print("Haz vuelto a\nMENU OPCIONES")
        print("1). Ver inventario libros \n2). Ver lista de usuarios activos \n3). Informacion categorias disponibles \n0). Salir del programa")
        print("")
        while True:
            try:
                option = int(input("Selecciona el numero de la opcion que desees del menu: "))
                if option in optns:
                    break
                else:
                    print("Opcion invalida. intentalo de nuevo")
                    continue
            except:
                print("Opcion invalida. intentalo de nuevo")
                print('')
                continue
                
    if option == 0:
        print('Hasta luego.')
        break
