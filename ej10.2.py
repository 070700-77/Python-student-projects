#mbox-short.txt
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

hours = {}

for line in handle:
    if line.startswith("From "):
        line = line.strip()
        parts = line.split(" ")
        if len(parts) > 5:
            time = parts[6]
            hour = time[:2]
            hours[hour] = hours.get(hour,0) + 1
            
handle.close

for key in sorted(hours.keys()):
    print(f"{key} {hours[key]}")