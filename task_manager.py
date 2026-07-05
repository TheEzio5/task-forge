
class TaskManager:

    def __init__(self):
        self.tasks = []

    def add_task(self, task,):
        self.tasks.append(task)

    def view_tasks(self):
        for task in self.tasks:
            print(task)