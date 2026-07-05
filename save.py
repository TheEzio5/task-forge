import json
from task import Task

def save_task(manager):
    task_data = []
    for task in manager.tasks:
        task_data.append(task.to_dict())

    with open("tasks.json", "w") as file:
        json.dump(task_data, file, indent=4)



def load_task(manager):

    with open("tasks.json", "r") as file:
        task_data = json.load(file)

    for task in task_data:

        new_task = Task(
            task["title"],
            task["description"],
            task["priority"]
        )
        new_task.completed = task["completed"]
        manager.add_task(new_task)