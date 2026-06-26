class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def to_dict(self):
        return {
            "title": self.title,
            "completed": self.completed
        }