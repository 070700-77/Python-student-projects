Nota1 = (float (input("insert your first grade: ")))
Nota2 = (float (input("insert your second grade: ")))
Nota3 = (float (input("insert your third grade: ")))
Nota4 = (float (input("insert your fourth grade: ")))
Nota5 = (float (input("insert your fifth grade: ")))
prom = (Nota1+Nota2+Nota3+Nota4+Nota5)/5
if prom >=90:
    print ("Your final grade is an A")
elif prom >=80 and <=89:
    print ("Your final grade is a B")
elif prom >=70 and <=79:
    print ("Your final grade is a C")
elif prom >=60 and <=69:
    print ("your final grade is a D")
elif prom <=60 and >=0:
    print ("your final grade is a F.You reproved the course")
else:
    print ("Please check again your grades. They have to be in the 0/100 margin")
 