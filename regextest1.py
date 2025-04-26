while True:
    fname = input("Enter file name: ")
    try:
        fh = open(fname, encoding='utf-8')
        break
    except FileNotFoundError:
        print("File hasn't been found. Try again please.")
        print("")

import re        
        
count = []
final_total = 0
patron = ('[0-9]+')

for line in fh:
    line = line.strip()
    
    coincidencia = re.findall(patron, line)
    if coincidencia:
        count.append(coincidencia)

for items in count:
    for item in items:
        item = int(item)
        final_total += item
        
print("")
print(f"{final_total:,.0f}")