import os
import json

FILE_NAME = 'tasks.json'

def load_tasks():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, 'r') as file:
                data = json.load(file)
                if isinstance(data, list):
                    return data
        except json.JSONDecodeError:
            print("Warning: Could not read tasks file, starting fresh.")
    return []

    
def save_tasks(tasks):
    with open(FILE_NAME, 'w') as file:
        json.dump(tasks, file, indent = 2)

def show_menu():
    print("\n To-Do List App")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Sort Tasks (Optional)")
    print("6. Exit")

def add_task(tasks):
    title = input("Enter task title: ").strip()
    if title:
        task = {"id": len(tasks)+1, "title": title, "done": False}
        tasks.append(task)
        print("Task added.")
    else:
        print("Tasks cannot be empty.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    print("\n Tasks:")
    for task in tasks:
        status = "[ ✅ ]" if task ["done"] else "[   ]"
        print(f'{task["id"]}. {status} {task["title"]}')

def mark_complete(tasks):
    try:
        task_id = int(input("Enter task ID to mark complete:"))
        for task in tasks:
            if task["id"] == task_id:
                task["done"] = True
                print("Task marked as completed.")
                return
            print("Task not found.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_task(tasks):
    try:
        task_id = int(input("Enter task ID to delete: "))
        for i, task in enumerate(tasks):
            if task["id"] == task_id:
                tasks.pop(i)
                print("Task deleted.")
                return
            print("Tasks not found.")
    except ValueError:
        print("Invalid input. Please enter a number.") 

def sort_tasks(tasks):
    print("\nSort by:")
    print("1. Alphabetically")
    print("2 Completion Status")
    choice = input("Enter your choice: ")
    if choice == "1":
        tasks.sort(key = lambda x : x["title"].lower())
        print("Tasks sorted alphabetically.")
    elif choice == "2":
        tasks.sort(key = lambda x : x["done"])
        print("Tasks sorted by status.")
    else:
        print("Invalid choice.")

def main():
    tasks = load_tasks()
    while True:
        show_menu()
        choice = input("choose an option (1-6): ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            sort_tasks(tasks)
        elif choice == "6":
            save_tasks(tasks)
            print("Goodbye! Tasks saved.")
            break
        else:
            print("Invalid choice. Please select 1-6.")

if __name__ == "__main__":
    main() 

