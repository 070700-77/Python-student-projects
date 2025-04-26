#test7.txt
while True:
    fname = input("Enter file name: ")
    try:
        fh = open(fname, encoding='utf-8') 
        break
    except FileNotFoundError:
        print(f"The file {fname} hasn't been found. Try again.")
        
clients_dict = {}
found = False
rank = 0

for line in fh:
    if "Ingresos Totales (USD),Ingreso Promedio por Cliente (USD)" in line:
        found = True
        continue
    elif found is True:
        if "## Costos Operativos Desglosados (USD)" in line:
            break
        line = line.strip()
        parts = line.split(",")
        if len(parts) > 4:
            client = parts[0]
            income = int(parts[3])
            clients_dict[client] = clients_dict.get(client,0) + income
fh.close()

income_list = list(clients_dict.items())
sorted_list = sorted(income_list, key=lambda item: item[1], reverse=True)
sorted_dict = dict(sorted_list)

print("Main clients by annual income")
for key, value in sorted_dict.items():
    rank += 1
    print(f"{rank}. {key}: ${value:,.0f}")