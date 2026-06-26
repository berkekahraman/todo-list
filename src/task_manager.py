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
        priority = priority.capitalize()

        if priority not in ["High", "Medium", "Low"]:
            print("Invalid priority. Using Medium as default.")
            priority = "Medium"

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

        task = self.tasks[task_number - 1]
        task.mark_completed()
        self.save_tasks()

        print("Task marked as completed.")

    def delete_task(self, task_number):
        if task_number < 1 or task_number > len(self.tasks):
            print("Invalid task number.")
            return

        deleted_task = self.tasks.pop(task_number - 1)
        self.save_tasks()

        print(f"Deleted: {deleted_task.title}")

    def edit_task(self, task_number, title, priority, due_date):
        if task_number < 1 or task_number > len(self.tasks):
            print("Invalid task number.")
            return

        priority = priority.capitalize()

        if priority not in ["High", "Medium", "Low"]:
            print("Invalid priority. Using Medium as default.")
            priority = "Medium"

        task = self.tasks[task_number - 1]
        task.title = title
        task.priority = priority
        task.due_date = due_date

        self.save_tasks()

        print("Task updated successfully.")

    def search_tasks(self, keyword):
        found_tasks = []

        for task in self.tasks:
            if keyword.lower() in task.title.lower():
                found_tasks.append(task)

        if not found_tasks:
            print("No matching tasks found.")
            return

        print("\nSearch Results:")

        for index, task in enumerate(found_tasks, start=1):
            status = "✓" if task.completed else "✗"
            print(
                f"{index}. [{status}] {task.title} "
                f"| Priority: {task.priority} "
                f"| Due: {task.due_date if task.due_date else 'No due date'}"
            )

    def filter_tasks(self, filter_type):
        filtered_tasks = []

        for task in self.tasks:
            if filter_type == "completed" and task.completed:
                filtered_tasks.append(task)
            elif filter_type == "pending" and not task.completed:
                filtered_tasks.append(task)
            elif filter_type == "high" and task.priority.lower() == "high":
                filtered_tasks.append(task)
            elif filter_type == "medium" and task.priority.lower() == "medium":
                filtered_tasks.append(task)
            elif filter_type == "low" and task.priority.lower() == "low":
                filtered_tasks.append(task)

        if not filtered_tasks:
            print("No tasks found.")
            return

        print("\nFiltered Tasks:")

        for index, task in enumerate(filtered_tasks, start=1):
            status = "✓" if task.completed else "✗"
            print(
                f"{index}. [{status}] {task.title} "
                f"| Priority: {task.priority} "
                f"| Due: {task.due_date if task.due_date else 'No due date'}"
            )

    def show_statistics(self):
        total_tasks = len(self.tasks)
        completed_tasks = 0
        pending_tasks = 0
        high_priority = 0
        medium_priority = 0
        low_priority = 0

        for task in self.tasks:
            if task.completed:
                completed_tasks += 1
            else:
                pending_tasks += 1

            if task.priority.lower() == "high":
                high_priority += 1
            elif task.priority.lower() == "medium":
                medium_priority += 1
            elif task.priority.lower() == "low":
                low_priority += 1

        if total_tasks == 0:
            completion_rate = 0
        else:
            completion_rate = (completed_tasks / total_tasks) * 100

        print("\n========== TASK STATISTICS ==========")
        print(f"Total Tasks      : {total_tasks}")
        print(f"Completed Tasks  : {completed_tasks}")
        print(f"Pending Tasks    : {pending_tasks}")
        print()
        print(f"High Priority    : {high_priority}")
        print(f"Medium Priority  : {medium_priority}")
        print(f"Low Priority     : {low_priority}")
        print()
        print(f"Completion Rate  : {completion_rate:.1f}%")
        print("=====================================")