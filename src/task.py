from datetime import datetime


class Task:
    def __init__(
        self,
        title,
        completed=False,
        priority="Medium",
        due_date="",
        created_at=None
    ):
        self.title = title
        self.completed = completed
        self.priority = priority
        self.due_date = due_date

        if created_at is None:
            self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M")
        else:
            self.created_at = created_at

    def mark_completed(self):
        self.completed = True

    def to_dict(self):
        return {
            "title": self.title,
            "completed": self.completed,
            "priority": self.priority,
            "due_date": self.due_date,
            "created_at": self.created_at
        }

    @staticmethod
    def from_dict(data):
        return Task(
            data["title"],
            data["completed"],
            data.get("priority", "Medium"),
            data.get("due_date", ""),
            data.get("created_at")
        )