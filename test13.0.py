import json

data = '''
{
  "empresas": [
    {
      "nombre": "Tech Innovations Inc",
      "ubicacion": "Silicon Valley",
      "empleados": [
        {
          "nombre": "John Doe",
          "edad": 30,
          "cargo": "Ingeniero de Software",
          "salario": 120000
        },
        {
          "nombre": "Jane Smith",
          "edad": 25,
          "cargo": "Diseñadora UX",
          "salario": 90000
        }
      ],
      "productos": [
        {
          "nombre": "App de Realidad Aumentada",
          "precio": 10.99
        },
        {
          "nombre": "Sistema de IA para Negocios",
          "precio": 499.99
        }
      ]
    },
    {
      "nombre": "GreenWorld Energies",
      "ubicacion": "Berlin",
      "empleados": [
        {
          "nombre": "Alice Müller",
          "edad": 35,
          "cargo": "Investigadora Energía Solar",
          "salario": 85000
        },
        {
          "nombre": "Marco Weiss",
          "edad": 28,
          "cargo": "Técnico de campo",
          "salario": 45000
        }
      ],
      "productos": [
        {
          "nombre": "Panel Solar de Alta Eficiencia",
          "precio": 1500.00
        }
      ]
    }
  ]
}
'''

info = json.loads(data)

print('Cantidad de empresas:', len(info))

for companies in info["empresas"]:
    count = 1
    print(f'Nombre de la empresa {count}: ', companies['nombre'])
    count += 1