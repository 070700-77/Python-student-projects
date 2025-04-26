while True:
    fname = input("Enter file name: ")
    try:
        fh = open(fname, encoding='utf-8') 
        break
    except FileNotFoundError:
        print(f"The file {fname} hasn't been found. Try again.")
parts = {}
for line in fh:
    line = line.strip()
    words = line.split()
    for word in words:
        parts[word] = parts.get(word,0)+1
print("Count: ", parts)