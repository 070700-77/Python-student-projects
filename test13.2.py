import json

data = '''
{
  "hospital": "Hospital Central Ciudad",
  "pacientes": [
    {
      "nombre": "Eduardo Pérez",
      "edad": 40,
      "tratamientos": [
        {
          "nombre": "Cirugía de Rodilla",
          "fecha": "2025-01-10",
          "costo": 2000
        }
      ],
      "citas": [
        {
          "fecha": "2025-01-15",
          "especialista": "Dr. Ana Ruiz"
        }
      ]
    },
    {
      "nombre": "Luisa Fernández",
      "edad": 29,
      "tratamientos": [
        {
          "nombre": "Terapia Física",
          "fecha": "2025-01-20",
          "costo": 150
        }
      ],
      "citas": [
        {
          "fecha": "2025-01-22",
          "especialista": "Dr. Marco González"
        }
      ]
    }
  ]
}
'''

info = json.loads(data)

hospital = info['hospital']
print(f'Hospital: {hospital}')
print('==============================================================================================================================')
print('')
print('Informacion de pacientes activos: \n')
for item in info['pacientes']:
    name = item['nombre']
    age =  item['edad']
    print(f'Nombre del paciente: {name} \nEdad: {age} \n')
    print("Historial clinico:")
    for treatment in item['tratamientos']:
        t_name = treatment['nombre']
        date = treatment['fecha']
        cost = int(treatment['costo'])
        print(f'Tratamiento: {t_name} \nFecha: {date} \nCosto: ${cost:,.2f} \n')
    print("Citas vigentes")
    for cita in item['citas']:
        a_date = cita['fecha']
        doc = cita['especialista']
        print(f"Fecha: {a_date} \nEspecialista: {doc}")
        
        
        
        