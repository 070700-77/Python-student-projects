print("-------------------------------------")
print("")
print("Welcome to your personal health diary")
print("")
print("-------------------------------------")
#Crear librerias para almacenar dato semanales
weekly_water = []
weekly_steps = []
#definir funciones
def dialy_data():
    while True:
        try:
            dialy_water = (float(input("Please enter the ammount in Ltrs of today's drinked water: ")))
            break
        except:
            print("You entered an invalid value. Please try again")
    while True:
        try:
            dialy_steps = (int(input("Please enter the ammount of today's walked steps: ")))
            break
        except:
            print("You entered an invalid value. Please try again")
    if dialy_water >= 2.0:
        print("Congratulations. You achieved your dialy 2L of water goal on your day. ")
    else:
        missing_l = 2.0 - dialy_water
        print(f"you are missing {missing_l:.2f}L to reach the goal")
    if dialy_steps >= 10000:
        print("Congratulations. You achieved your dialy 10.000 steps goal. ")
    else:
        missing_s = 10000 - dialy_steps
        print(f"you are missing {missing_s} steps to reach the goal")
def weekly_data():
    for day in range(8):
        print("")
        while True:
            try:
                qwater = (float(input(f"Enter the ammount of Ltrs drank on day {day+1}: ")))
                weekly_water.append(qwater)
                break
            except:
                print("you entered an invalid value. Please try again")
        while True:
            try:
                qsteps = (int(input(f"Enter the ammount of walked steps on day {day+1}: ")))
                weekly_steps.append(qsteps)
                break
            except:
                print("you entered an invalid value. Please try again")
def promedio (lista):
    sumatory = sum(lista)
    lenght = len(lista)
    promedio = sumatory/lenght
    return promedio
def main_menu ():
    while True:
        print("")
        print("Select the number of an option")
        print("")
        print("1). Register your dialy steps and Ltrs of water & get feedback")
        print("2). Calculate the average amount of water drank and steps walked over a week")
        print("9). Exit program")
        print("")
        try:
            opt = (int(input("Enter the number of the desired option: ")))
            break
        except:
            print("You entered an invalid value. Please try again")
    if opt == 1:
        dialy_data()
        main_menu()
    elif opt ==2:
        weekly_data()
        average_water = promedio(weekly_water)
        average_steps = promedio(weekly_steps)
        print("")
        print(f"The average value of your weekly steps is {average_steps}")
        print(f"The average value of your weekly volume of drank water is {average_water}")
        print("")
        main_menu()
    elif opt == 9:
        print("GOODBYE.")
        exit()
    else:
        print("Invalid value. Please try again")
main_menu()

