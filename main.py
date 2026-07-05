from task import Task
from task_manager import TaskManager
from menu import menu



while True:

    menu()

    main_menu = input("Please enter your choice:")
    if main_menu == "1":
        print("Add task")
    elif main_menu == "2":
        print("View tasks")
    elif main_menu == "3":
        print("Bye Bye")
        break
    else:
        print("Invalid choice")