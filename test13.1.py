import json
data = '''
{
  "universidad": "Universidad Internacional",
  "estudiantes": [
    {
      "nombre": "Carlos Rodríguez",
      "edad": 21,
      "carrera": "Ingeniería de Sistemas",
      "cursos": [
        {
          "nombre": "Algoritmos",
          "nota": 4.5
        },
        {
          "nombre": "Estructuras de Datos",
          "nota": 4.2
        }
      ],
      "actividades": [
        "Club de Robótica",
        "Equipo de Fútbol"
      ]
    },
    {
      "nombre": "Ana María Castro",
      "edad": 22,
      "carrera": "Medicina",
      "cursos": [
        {
          "nombre": "Anatomía Humana",
          "nota": 4.8
        },
        {
          "nombre": "Bioquímica",
          "nota": 4.4
        }
      ],
      "actividades": [
        "Voluntariado Hospital",
        "Sociedad de Debate"
      ]
    }
  ]
}
'''

info = json.loads(data)

print("")

for students in info['estudiantes']:
    name = students['nombre']
    age =  students['edad']
    career = students ['carrera']
    courses = students ['cursos']
    print(f"Nombre del estudiante: {name} \nEdad: {age} \nCarrera: {career} \nActividades extracurriculares en las que participa:")
    for act in students['actividades']:
        print(act)
    print("")
    print("NOTAS ACADEMICAS:")
    for course in courses:
        c_name = course['nombre']
        grade = course['nota']
        print(f"{c_name}: {grade}")
    print("")
    print("-------------------------------------------------------------------------------------------------------------------------")
        


    