from task import Task


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        task = Task(title)
        self.tasks.append(task)

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
    def complete_task(self, task_number):
        if task_number < 1 or task_number > len(self.tasks):
            print("Invalid task number.")
            return

        task = self.tasks[task_number - 1]
        task.mark_completed()
        print("Task marked as completed.")

        print("\nTasks:")

        for index, task in enumerate(self.tasks, start=1):
            status = "✓" if task.completed else "✗"
            print(f"{index}. [{status}] {task.title}")