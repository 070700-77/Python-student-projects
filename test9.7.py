#test7.txt
while True:
    fname = input("Enter file name: ")
    try:
        fh = open(fname, encoding='utf-8') 
        break
    except FileNotFoundError:
        print(f"The file {fname} hasn't been found. Try again.")

found0 = False
product_sales_dict = {}
rank = 0

for line in fh:
    if "|Región|Unidades Vendidas|Precio Unitario (USD)|Ingresos Totales (USD)" in line:
        found0 = True
        continue
    elif found0 is True:
        if "## Resumen de Clientes por Segmento" in line:
            break
        line = line.strip()
        parts = line.split("|")
        if len(parts) > 4:
            product =parts[0]
            region = parts[1]
            unit_price = int(parts[2])
            units_sold = int(parts[3])
            total_sales = unit_price*units_sold
            product_sales_dict[product] = product_sales_dict.get(product, ()) + (region, total_sales)
fh.close()

sales_list = list(product_sales_dict.items())
sorted_list = sorted(sales_list, key=lambda item: item[1][1], reverse=True)
sorted_sales_dict = dict(sorted_list)

print("Ranking de productos con mayores ingresos:")
print("")
for key, value in sorted_sales_dict.items():
    rank += 1
    print(f"{rank}. {key}: Producto tuvo ingresos por ${value[1]:,.0f} y su venta es exclusiva para la region de {value[0]}")