

class TaskManager:

    def __init__(self):
        self.tasks = []

    def add_task(self, task):
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

    def complete_task(self,task_completed):
        try:
            task = self.tasks[task_completed - 1]
            task.completed = True
            print("Task completed!")
        except IndexError:
            print("Invalid task number.")

    def delete_task(self,task_number):
        self.tasks.pop(task_number-1)

        print("Task deleted!")

    def search_tasks(self, search):
        found = False
        for number, task in enumerate(self.tasks):
            if search.lower() in task.title.lower():
                found = True
                print(f"Task #{number + 1}")
                print(f"Title: {task.title}")
                print(f"Description: {task.description}")
                print(f"Priority: {task.priority}")
                print(f"Completed: {task.completed}")
                print("-" * 20)
        if not found:
            print("No matching tasks found.")

    def edit_task(self, task_number, title, description, priority):

        task = self.tasks[task_number - 1]

        task.title = title
        task.description = description
        task.priority = priority
        print("Task edited!")

