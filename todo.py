TASKS = []
def show_menu():
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")
def add_task():
    task = input("Enter a new task: ")
    TASKS.append(task)
    print(f"Task '{task}' added.")

def list_tasks():
    if not TASKS:
        print("No tasks available.")
    else:
        print("Your Tasks:")
        for idx, task in enumerate(TASKS, 1):
            print(f"{idx}. {task}")
def delete_task():
    list_tasks()
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(TASKS):
            removed_task = TASKS.pop(task_num - 1)
            print(f"Task '{removed_task}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
if __name__ == "__main__":
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            add_task()
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            print("Exiting the to-do list application.")
            break
        elif choice == '4':
            delete_task()            