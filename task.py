class Task:

    def __init__(self, title, description, priority):
        self.id = None
        self.title = title
        self.description = description
        self.priority = priority
        self.completed = False

    def __str__(self):
        return f"{self.title} | {self.priority}"
