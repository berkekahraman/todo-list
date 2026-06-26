# Task Manager

A command-line task management application built with Python.

This project helps users organize their daily tasks by allowing them to create, update, complete, search, filter, and manage tasks directly from the terminal. All task data is stored locally in a JSON file, so tasks are preserved between program runs.

---

## Features

- Add new tasks
- View all tasks
- Edit existing tasks
- Mark tasks as completed
- Delete tasks
- Search tasks by keyword
- Filter tasks by status or priority
- Display task statistics
- Set task priorities (High, Medium, Low)
- Set due dates
- Automatically store task creation date
- Save and load data using JSON

---

## Technologies

- Python
- Object-Oriented Programming (OOP)
- JSON
- Git
- GitHub

---

## Project Structure

```
todo-list/
│
├── src/
│   ├── main.py
│   ├── task.py
│   ├── task_manager.py
│   └── storage.py
│
├── tasks.json
├── README.md
├── .gitignore
└── requirements.txt
```

---

## How to Run

1. Clone the repository

```bash
git clone https://github.com/berkekahraman/todo-list.git
```

2. Move into the project folder

```bash
cd todo-list
```

3. Run the application

```bash
python src/main.py
```

---

## Example Menu

```
=============================
        TASK MANAGER
=============================

1. Add Task
2. View Tasks
3. Edit Task
4. Complete Task
5. Delete Task
6. Search Tasks
7. Filter Tasks
8. Statistics
9. Exit

=============================
```

---

## Future Improvements

- Sort tasks by due date
- Export tasks to CSV
- Add colored terminal output
- Build a graphical interface with Tkinter
- Develop a web version using Flask

---

## Author

**Berke Kahraman**

GitHub:
https://github.com/berkekahraman