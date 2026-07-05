

class TaskManager:

    def __init__(self):
        self.tasks = []

    def add_task(self, task,):
        self.tasks.append(task)

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found")
            return
        for number, task in enumerate(self.tasks):
            print(f"Task #{number + 1}")
            print(f"Title: {task.title}")
            print(f"Description: {task.description}")
            print(f"Priority: {task.priority}")
            print(f"Completed: {task.completed}")
            print("-" * 20)
