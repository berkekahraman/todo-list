from task_manager import TaskManager


def show_menu():
    print("\n=============================")
    print("        TASK MANAGER")
    print("=============================")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Edit Task")
    print("4. Complete Task")
    print("5. Delete Task")
    print("6. Search Tasks")
    print("7. Filter Tasks")
    print("8. Statistics")
    print("9. Exit")
    print("=============================")


def main():
    manager = TaskManager()
    manager.load_tasks()

    while True:
        show_menu()

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Task title: ")
            priority = input("Priority (High/Medium/Low): ")
            due_date = input("Due date (YYYY-MM-DD, optional): ")

            manager.add_task(title, priority, due_date)
            print("Task added successfully!")

        elif choice == "2":
            manager.view_tasks()

        elif choice == "3":
            manager.view_tasks()

            if manager.tasks:
                try:
                    task_number = int(input("Enter task number: "))

                    title = input("New title: ")
                    priority = input("Priority (High/Medium/Low): ")
                    due_date = input("Due date (YYYY-MM-DD): ")

                    manager.edit_task(
                        task_number,
                        title,
                        priority,
                        due_date
                    )

                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "4":
            manager.view_tasks()

            if manager.tasks:
                try:
                    task_number = int(input("Enter task number: "))
                    manager.complete_task(task_number)
                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "5":
            manager.view_tasks()

            if manager.tasks:
                try:
                    task_number = int(input("Enter task number: "))
                    manager.delete_task(task_number)
                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "6":
            keyword = input("Search keyword: ")
            manager.search_tasks(keyword)

        elif choice == "7":
            print("\nFilter Tasks")
            print("1. Completed")
            print("2. Pending")
            print("3. High Priority")
            print("4. Medium Priority")
            print("5. Low Priority")

            filter_choice = input("Choose filter: ")

            if filter_choice == "1":
                manager.filter_tasks("completed")
            elif filter_choice == "2":
                manager.filter_tasks("pending")
            elif filter_choice == "3":
                manager.filter_tasks("high")
            elif filter_choice == "4":
                manager.filter_tasks("medium")
            elif filter_choice == "5":
                manager.filter_tasks("low")
            else:
                print("Invalid filter option.")
        
        elif choice == "8":
            manager.show_statistics()
        elif choice == "9":
            print("Goodbye!")
            break


        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()