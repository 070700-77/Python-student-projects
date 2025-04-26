print("-------------------------------------------------------")
print("")
print("Welcome to techao.com's  id authenticator for employees")
print("")
print("-------------------------------------------------------")
#Craete empty list to save ID info
user_ids = []
user_passwords = []
#MENU
def menu():
    global menu_opt
    print("Please, select the numeric value of the desire option.")
    print("")
    print("1). Register a new user")
    print("2). Log in with you ID")
    print("3). Exit program")
    print("")
    while True:
        try:
            menu_opt = (int(input("Enter the numeric option: ")))
            break
        except:
            print("The numeric option you have entered is invalid. Please try again.")
        print("You have enterd an invalid option value. Please select a correct numeric value for the desire option")

def register_user ():
    print("")
    user_id = (str(input("Please enter your full name (It would be you ID): ")))
    user_ids.append(user_id)   
    user_password = (str(input("Please enter a password: ")))
    user_passwords.append(user_password)
    print("")
    print(f"WELCOME " + user_id.upper())
    
def login (user_ids, user_passwords):
    while True:
        user_id = (str(input("Please enter your ID (Your full name): ")))
        user_password = (str(input("Please enter your password: ")))
        if user_id in user_ids:
            print(f"WELCOME " + user_id.upper())
        else:
            print("Unknow ID. Try again.")
        if user_password in user_passwords:
            print("You have logged in succesfully into your employee account.")
            break
        else:
            print("You have entered a wrong password. Try again.")
    
#Program options main bucle
menu()
while menu_opt != 3:
    if menu_opt == 1:
        register_user()
        menu()
    elif menu_opt ==2:
        login (user_ids, user_passwords)
        menu()
print("You have selected the option numer 3 (Exit program). GOODBYE")