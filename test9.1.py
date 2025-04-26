#test8.txt
while True:
    fname = input("Enter file name: ")
    try:
        fh = open(fname, encoding='utf-8') 
        break
    except FileNotFoundError:
        print(f"The file {fname} hasn't been found. Try again.")
        
found = False
temp_list = []
suppliers = {}

for line in fh:
    if "Entregas,Tasa de Retrasos (%)" in line:
        found = True
        continue
    elif found is True:
        if "## Datos Generales de Inventario" in line:
            break
        line = line.strip()
        parts =line.split(",")
        if len(parts) > 3:
            name = parts[0]
            rating = float(parts[1])
            suppliers[name] = suppliers.get(name,0) +rating
fh.close()

for key, value in suppliers.items():
    temp_list.append((value, key))
    
for items in temp_list:
    print(items)