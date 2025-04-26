#The following program finds email adresses in the file named mbox-short.txt, counting and printing them as output
count = 0
while True:
    try:
        fname = (input("Enter File name: "))
        fh = open (fname)
        break
    except FileNotFoundError:
        print ("File Not found.\nTry again.")
for line in fh:
    if not line.startswith("From:"):
        continue
    line = line.rstrip()
    print({line[6:]})
    count += 1
print("")
print(f"Numer of email adresses: {count}")