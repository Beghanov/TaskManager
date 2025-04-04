import json

# Task Manager
def load_tasks(filename="tasks.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks, filename="tasks.json"):
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(task, filename="tasks.json"):
    tasks = load_tasks(filename)
    tasks.append(task)
    save_tasks(tasks, filename)
    print("Task added!")

def list_tasks(filename="tasks.json"):
    tasks = load_tasks(filename)
    if not tasks:
        print("No tasks available.")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def remove_task(index, filename="tasks.json"):
    tasks = load_tasks(filename)
    try:
        tasks.pop(index - 1)
        save_tasks(tasks, filename)
        print("Task removed!")
    except IndexError:
        print("Invalid task number.")

while True:
    print("\nTask Manager")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Remove Task")
    print("4. Exit")
    choice = input("Enter choice: ")
    
    if choice == "1":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "2":
        list_tasks()
    elif choice == "3":
        list_tasks()
        index = int(input("Enter task number to remove: "))
        remove_task(index)
    elif choice == "4":
        break
    else:
        print("Invalid choice. Try again.")
