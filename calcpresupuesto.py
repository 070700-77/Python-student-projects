print("--------------------------------------------------")
print("")
print("Bienvenido a tu calculadora de presupuesto mensual")
print("")
print("--------------------------------------------------")
valores_categorias = []
gasto_total = 0
while True:
    try:
        ingresos = (float(input("por favor ingresa tu ingreso proyectado o el total de ingresos del ultimo mes: ")))
        break
    except:
        print("Has ingresado un valor invalido. Intentalo de nuevo")
print("")
print("Se han definido las siguientes categorias de egresos")
print("")
print("1).Vida diaria\n(Ejemplos: Comida en la Universidad, Mercado GYM ,Suplementos, Café, Restaurantes")
print("")
print("2).Transporte\n(Ejemplos: SITP, Uber, Gasolina, Lavado del coche y servicios de detalles similares, Aparcamiento")
print("")
print("3).Entretenimiento\n(Ejemplos: Citas, Club Independiente Santa Fe, Conciertos, Ferías, Planes organizados, Cine, Discotecas y fiesta)")  
print("")
print("4).Educacion / desarrollo profesional\n(Ejemplos: Licencia de Platzi, ChatGPT-4, Lumosity, Claude AI)")
print("")
print("5).Personal\n(Ejemplos: Ropa, Regalos, Barberías, Dentista, Libros Psicologo, GYM, Rutina skin care)")
print("")
print("6).Viajes\n(Ejemplos: Estadia, Comidas, Rumba, Transporte)")
print("")
print("7).Inversiones\n(Ejemplos:  CDTs, ETFs, Acciones)")
for i in range (7):
    try: 
        egreso = (float(input(f"Ingrese el monto de egresos equivalente a la Categoria numero {i+1}: ")))
        valores_categorias.append(egreso)
    except:
        print("Valor invalido. Intentelo de nuevo")
def margen (ingresos, valores_categorias):
    if ingresos >= sum(valores_categorias):
        print("Tus gastos estan dentro del margen de ingresos")
        print("")
    else:
        print("Precaucion. Estas gastando mas de lo que ganas")
        print("")
def calcular_gastos(lista):
    calcular_gastos = sum(lista)
    return calcular_gastos
def calcular_ahorro (lista):
    total_egresos = sum(lista)
    calcular_ahorro = ingresos - total_egresos
    return calcular_ahorro
margen (ingresos, valores_categorias)
total_gastos = calcular_gastos(valores_categorias)
print(f"El total de tus gastos fue ${total_gastos}")
total_ahorro = calcular_ahorro (valores_categorias)
print(f"El total ahorrado fue ${total_ahorro}")
