#test7.txt
while True:
    fname = input("Enter file name: ")
    try:
        fh = open(fname, encoding='utf-8') 
        break
    except FileNotFoundError:
        print(f"The file {fname} hasn't been found. Try again.")

profit_dict = {}
found0 = False
found1 = False
monthly_cost = 0

for line in fh:
    if "Costo Promedio Mensual|Costo Total Anual" in line:
        found0 = True
        continue
    elif found0 is True:
        if "## Empleados por Departamento y Salarios" in line:
            found0 = False
            continue
        line = line.strip()
        parts = line.split("|")
        if len(parts) > 2:
            monthly_cost += int(parts[1])
    
    if "Ingresos del Trimestre,Variación (%) respecto al trimestre anterior" in line:
        found1 = True
    elif found1 is True:
        if "## Proyecciones Financieras para 2024" in line:
            break
        line = line.strip()
        parts = line.split(",")
        if len(parts) > 2:
            quarter = parts[0]
            quarterly_income = int(parts[1])
            quarterly_profit = (quarterly_income - (monthly_cost *3))/quarterly_income
            profit_dict[quarter] = profit_dict.get(quarter,0) + quarterly_profit
    
fh.close()
    
profit_list = list(profit_dict.items())
sorted_list = sorted(profit_list, key=lambda item: item[1], reverse=True)
sorted_profit_dict = dict(sorted_list)

print("Rentabilidad trimestral ordenada:")
for key, value in sorted_profit_dict.items():
    print(f"{key}: {value:.2f}%")