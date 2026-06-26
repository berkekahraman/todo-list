class Task:
    def __init__(self, title, completed=False, priority="Medium", due_date=""):
        self.title = title
        self.completed = completed
        self.priority = priority
        self.due_date = due_date

    def mark_completed(self):
        self.completed = True

    def to_dict(self):
        return {
            "title": self.title,
            "completed": self.completed,
            "priority": self.priority,
            "due_date": self.due_date
        }

    @staticmethod
    def from_dict(data):
        return Task(
            data["title"],
            data["completed"],
            data.get("priority", "Medium"),
            data.get("due_date", "")
        )