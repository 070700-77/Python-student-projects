#test8.txt
while True:
    fname = input("Enter file name: ")
    try:
        fh = open(fname, encoding='utf-8') 
        break
    except FileNotFoundError:
        print(f"The file {fname} hasn't been found. Try again.")
        
found0 = False
inventory_cost = []
        
for line in fh:
    if "Categoría,Producto,Código,Stock,Precio Unitario (USD),Proveedor" in line:
        found0 = True
        continue
    elif found0 is True:
        if "## Historial de Ventas Anuales por Producto" in line:
            break
        line = line.strip()
        parts = line.split(',')
        if len(parts) > 5:
            if "Electrodomésticos" in line:
                product = parts[1]
                stock = int(parts[3])
                unit_price = int(parts[4])
                stock_price = stock*unit_price
                inventory_cost.append((product, stock_price))
fh.close()


for items in inventory_cost:
    print(f"Valor de inventario de {items[0]}: ${items[1]:,.2f}")