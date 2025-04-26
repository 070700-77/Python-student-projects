import xml.etree.ElementTree as ET
data = '''<clase>
    <estudiante id="101">
        <nombre>Ana García</nombre>
        <edad>20</edad>
        <notas>
            <matematicas>85</matematicas>
            <historia>92</historia>
            <ciencias>88</ciencias>
        </notas>
        <ciudad>Madrid</ciudad>
    </estudiante>
    <estudiante id="102">
        <nombre>Carlos López</nombre>
        <edad>19</edad>
        <notas>
            <matematicas>78</matematicas>
            <historia>95</historia>
            <ciencias>82</ciencias>
        </notas>
        <ciudad>Barcelona</ciudad>
    </estudiante>
</clase>'''

tree = ET.fromstring(data)

estudiantes = tree.findall('estudiante')

for item in estudiantes:
    estudiante = item.find('nombre').text
    id_estudiante = item.get('estudiante')
    edad = int(item.find('edad').text)
    notas = item.find('notas')
    math = notas.find('matematicas').text if notas.find('matematicas') is not None else "No encontrado"
    hist = notas.find('historia').text if notas.find('historia') is not None else "No encontrado"
    cien = notas.find('ciencias').text if notas.find('ciencias') is not None else "No encontrado"
    ciudad = item.find('ciudad').text
    print("")
    print("")
    print(f"Nombre del estudiante : {estudiante} \nID del estudiante: {id_estudiante} \nEdad: {edad}")
    print("")
    print(f"Notas \nMatematicas:{math} \nHistoria:{hist} \nCiencias: {cien}")