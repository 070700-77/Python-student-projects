print("")
print("To\nDo\nList")
print("")

#Create task list
tasks = []

#Define functions
def create_task ():
    while True:
        try:
            task = (str(input("Please writhe the task you want to add to your To Do List: ")))
            tasks.append(task)
            print(f"The following task: {task}, has been succsefully uploaded to your to do list")
            break
        except:
            print("You have not entered any new task. Try again")
def see_tasks ():
    print ("Actual task list")
    if len(tasks) == 0:
        print("Your task list is empty at the moment")
    else:
        for i, task in enumerate (tasks, 1):
            print (f"{i}. {task}")
def delete_task ():
    task = (str(input("Please enter the task you want to eliminate from your task list: ")))
    if task in tasks:
        tasks.remove(task)
    else:
        print(f"The task you have entered: {task}, hasn't been found on your task list.")
def find_task ():
    keyword = (input("Enter a keyword you'll like to look up to: "))
    #list comprehension
    results = [task for task in tasks if keyword in task]
    if len(results) == 0:
        print("No task has been found.")
    else:
        for task in results:
            print(task)
def menu():
    print ("Main\nmenu")
    print("")
    print("1). Create task")
    print("2). See current tasks")
    print("3). Delete task")
    print("4). Find task")
    print("5). Turn off program")
    
#Main menu bucle
while True:
    menu()
    try:
        opt = (int(input("Select the numeric value of the desired option: ")))
        if opt in [1,2,3,4,5]:
            if opt == 1:
                create_task()
            elif opt == 2:
                see_tasks()
            elif opt == 3:
                delete_task()
            elif opt == 4:
                find_task()
            elif opt == 5:
                print("GOODBYE.")
                break
        else:
            print("You have entered an invalid numeric option.")
    except:
        print("Please enter a valid numeric option.")