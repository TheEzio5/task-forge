from task import Task
from task_manager import TaskManager
from menu import menu, filtered_menu, sort_menu
from save import save_task, load_task

manager = TaskManager()
try:
    load_task(manager)
except FileNotFoundError:
    pass

def get_task_number():
    try:
        task_number = int(input("Please enter task number: "))
        return task_number
    except ValueError:
        print("Please enter a valid number")




while True:

    menu()

    main_menu = input("Please enter your choice: ")
    if main_menu == "1":

        title = input("Please enter desired name of the task: ")
        description = input("Please enter the description of the task: ")
        priority = input("Please enter the priority of the task: ")

        task = Task(title, description, priority)
        manager.add_task(task)
        save_task(manager)

        print("Task added successfully!")

    elif main_menu == "2":
        manager.view_tasks()
    elif main_menu == "3":
        task_number = get_task_number()
        if task_number is None:
            continue
        manager.complete_task(task_number)
        save_task(manager)
    elif main_menu == "4":
        task_number = get_task_number()
        if task_number is None:
            continue
        manager.delete_task(task_number)
        save_task(manager)
    elif main_menu == "5":
        search = input("Please enter task name: ")
        print("I have found the following tasks: ")
        manager.search_tasks(search)

    elif main_menu == "6":

        task_number = get_task_number()
        if task_number is None:
            continue
        title = input("Please enter new name of the task: ")
        description = input("Please enter new description of the task: ")
        priority = input("Please enter new priority of the task: ")
        manager.edit_task(task_number, title, description, priority)
        save_task(manager)
    elif main_menu == "7":
        filtered_menu()
        filter_choice = input("Please enter your choice: ")
        if filter_choice == "1":
            manager.view_tasks()
        elif filter_choice == "2":
            manager.filter_tasks(True)
        elif filter_choice == "3":
            manager.filter_tasks(False)
        elif filter_choice == "4":
            continue

    elif main_menu == "8":
        sort_menu()
        sort_choice = input("Please enter your choice: ")
        if sort_choice == "1":
            manager.sort_by_priority()
            save_task(manager)
        elif sort_choice == "2":
            manager.sort_by_title()
            save_task(manager)
        elif sort_choice == "3":
            continue

    elif main_menu == "9":

        print("Bye Bye")
        break
    else:
        print("Invalid choice")