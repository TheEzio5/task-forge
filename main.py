from task import Task
from task_manager import TaskManager
from menu import menu


manager = TaskManager()



while True:

    menu()

    main_menu = input("Please enter your choice: ")
    if main_menu == "1":

        title = input("Please enter desired name of the task: ")
        description = input("Please enter the description of the task: ")
        priority = input("Please enter the priority of the task: ")

        task = Task(title, description, priority)
        manager.add_task(task)

        print("Task added successfully!")
    elif main_menu == "2":
        manager.view_tasks()
    elif main_menu == "3":
        print("Bye Bye")
        break
    else:
        print("Invalid choice")