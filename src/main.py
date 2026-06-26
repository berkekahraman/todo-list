from task_manager import TaskManager


def show_menu():
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Exit")   


def main():
    manager = TaskManager()
    manager.load_tasks()

    while True:
        show_menu()

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Task title: ")
            manager.add_task(title)
            print("Task added successfully!")

        elif choice == "2":
            manager.view_tasks()

        elif choice == "3":
            manager.view_tasks()

            if manager.tasks:
                try:
                    task_number = int(input("Enter task number: "))
                    manager.complete_task(task_number)
                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()