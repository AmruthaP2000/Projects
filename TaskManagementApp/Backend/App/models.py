class Task:
    def __init__(self, title, description, status, due_date, task_id=None):
        self.id = task_id
        self.title = title
        self.description = description
        self.status = status
        self.due_date = due_date

    def to_tuple(self):
        return (self.title, self.description, self.status, self.due_date)
