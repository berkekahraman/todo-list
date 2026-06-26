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

    def add_task(self, title, priority, due_date):
        task = Task(title, priority=priority, due_date=due_date)
        self.tasks.append(task)
        self.save_tasks()

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return

        print("\nTasks:")

        for index, task in enumerate(self.tasks, start=1):
            status = "✓" if task.completed else "✗"
            print(
                f"{index}. [{status}] {task.title} "
                f"| Priority: {task.priority} "
                f"| Due: {task.due_date if task.due_date else 'No due date'}"
)

    def complete_task(self, task_number):
        if task_number < 1 or task_number > len(self.tasks):
            print("Invalid task number.")
            return
    def delete_task(self, task_number):
        if task_number < 1 or task_number > len(self.tasks):
            print("Invalid task number.")
            return

        deleted_task = self.tasks.pop(task_number - 1)
        self.save_tasks()

        print(f"Deleted: {deleted_task.title}")

        task = self.tasks[task_number - 1]
        task.mark_completed()
        self.save_tasks()
        print("Task marked as completed.")