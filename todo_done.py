from pathlib import Path
STORE = Path("task_txt")
def load_tasks():
    if not STORE.exists():
        return []
    lines = STORE.read_text(encoding="utf-8").splitlines()
    return [line for line in lines if line.strip()]
def save_tasks(tasks):
    STORE.write_text("\n".join(tasks), encoding="utf-8")
def show_menu():
   print("\n[1] Add [2] List [3] Toggle Done [4] Clear All [5] Quit")

def add_task():
    task = input("Enter a new task: ").strip()
    if task:
        tasks = load_tasks()
        tasks.append(f"[ ] {task}")
        save_tasks(tasks)
        print(f"Task '{task}' added.")
    else:
        print("Task cannot be empty.")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No Tasks Available.")
        return
    for i, t in enumerate(tasks, start=1):
        print(f"{i}. {t}")

def toggle_done():
    list_tasks()
    try:
        task_num = int(input("Enter the task number to toggle done: "))
        if 1 <= task_num <= len(tasks):
            if tasks[task_num - 1].startswith("[ ]"):
                tasks[task_num - 1] = tasks[task_num - 1].replace("[ ]", "[x]", 1)
                print(f"Task {task_num} marked as done.")
            elif tasks[task_num - 1].startswith("[x]"):
                tasks[task_num - 1] = tasks[task_num - 1].replace("[x]", "[ ]", 1)
                print(f"Task {task_num} marked as not done.")
            save_tasks(tasks)
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
def clear_all():
    confirm = input("Are you sure you want to clear all tasks? (y/n): ").lower()
    if confirm == 'y':
        save_tasks([])
        print("All tasks cleared.")
    else:
        print("Clear all cancelled.")
if __name__ == "__main__":
    while True:
        tasks = load_tasks()
        show_menu()
        choice = input("Choose an option: ").strip()
        if choice == '1':
            add_task()
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            toggle_done()
        elif choice == '4':
            clear_all()
        elif choice == '5':
            print("Exiting the to-do list application.")
            break
        else:
            print("Invalid choice. Please select a valid option.")                                               