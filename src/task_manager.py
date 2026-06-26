from task import Task
from storage import load_tasks, save_tasks


class TaskManager:
    def __init__(self):
        self.tasks = []

    def load_tasks(self):
        task_data = load_tasks()

        for data in task_data:
            task = Task.from_dict(data)
            self.tasks.append(task)

    def save_tasks(self):
        task_data = []

        for task in self.tasks:
            task_data.append(task.to_dict())

        save_tasks(task_data)

    def add_task(self, title):
        task = Task(title)
        self.tasks.append(task)
        self.save_tasks()

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return

        print("\nTasks:")

        for index, task in enumerate(self.tasks, start=1):
            status = "✓" if task.completed else "✗"
            print(f"{index}. [{status}] {task.title}")

    def complete_task(self, task_number):
        if task_number < 1 or task_number > len(self.tasks):
            print("Invalid task number.")
            return

        task = self.tasks[task_number - 1]
        task.mark_completed()
        self.save_tasks()
        print("Task marked as completed.")