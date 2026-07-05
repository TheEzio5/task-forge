from task import Task
from task_manager import TaskManager
from menu import menu
from save import save_task, load_task

manager = TaskManager()
try:
    load_task(manager)
except FileNotFoundError:
    pass



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
        task_number = int(input("Please enter task number: "))
        manager.complete_task(task_number)
        save_task(manager)
    elif main_menu == "4":
        task_number = int(input("Please enter task number: "))
        manager.delete_task(task_number)
        save_task(manager)
    elif main_menu == "5":
        print("Bye Bye")
        break
    else:
        print("Invalid choice")