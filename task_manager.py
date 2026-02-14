import json



print("***********************************")
print("• Easy Task Manager")
print("• Authors: Djouama Farid, Derias Oussama, Djaramou Hichem")
print("  Environmental Engineering PhD Students, FST, UMK-Biskra")
print("  (with a little help of ai ;))")
print()
print("• This program helps you create, edit and organize")
print("  your tasks for better time management.")
print()
print("  ENJOY!")
print("***********************************")




FILE_NAME = "tasks.json"

def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file)

def add_task(tasks):
    task = input("Enter task name please: ").strip()
    if task == "":
        print("Task field cannot be empty.")
        return
    tasks.append({"title": task, "done": False})
    save_tasks(tasks)
    print("Task added successfully.")

def list_tasks(tasks):
    if len(tasks) == 0:
        print("No added tasks yet.")
        return
    print("\nTask List:")
    for i, task in enumerate(tasks, start=1):
        status = "Done!" if task["done"] else "Not Done Yet"
        print(f"{i}. {task['title']} - {status}")

def mark_done(tasks):
    list_tasks(tasks)
    if len(tasks) == 0:
        return
    try:
        number = int(input("Task number to mark as done: "))
        tasks[number - 1]["done"] = True
        save_tasks(tasks)
        print("Task marked as done.")
    except:
        print("Invalid task number.")

def edit_task(tasks):
    if len(tasks) == 0:
        print("No tasks to edit.")
        return

    # Show tasks
    print("\nTask List:")
    for i, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Not Done"
        print(f"{i}. {task['title']} - {status}")

    # Choose task
    try:
        number = int(input("Enter task number to edit: "))
        if number < 1 or number > len(tasks):
            raise ValueError
    except ValueError:
        print("Invalid task number.")
        return

    task = tasks[number - 1]

    # Edit options
    print("\n1. Rename task")
    print("2. Delete task")
    print("3. Duplicate task")
    choice = input("Choose an option please: ")

    if choice == "1":
        new_title = input("Enter new title please: ").strip()
        if new_title == "":
            print("Title cannot be empty.")
        else:
            task["title"] = new_title
            save_tasks(tasks)
            print("Task renamed successfully.")
    elif choice == "2":
        confirm = input("Are you sure you want to delete this task? (y/n): ")
        if confirm.lower() == "y":
            tasks.pop(number - 1)
            save_tasks(tasks)
            print("Task deleted successfully.")
    elif choice == "3":
        tasks.append({"title": task["title"], "done": task["done"]})
        save_tasks(tasks)
        print("Task duplicated successfully.")
    else:
        print("Invalid choice.")

tasks = load_tasks()

while True:
    print("\n1. Add Task")
    print("2. View Added Tasks")
    print("3. Mark Task as Done")
    print("4. Edit Task")
    print("5. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_task(tasks)
    elif choice == "2":
        list_tasks(tasks)
    elif choice == "3":
        mark_done(tasks)
    elif choice == "4":
        edit_task(tasks)
    elif choice == "5":
        print("See ya!")
        break
    else:
        print("Invalid choice.")