from pathlib import Path
try:
    from colorama import Fore, Style
except ImportError:
    # Handle the case where colorama is not installed
    class Dummy: RESET_ALL=""; GREEN=""; RED=""; YELLOW=""; CYAN=""
    Fore = Style = Dummy()
STORE = Path("task_txt")
def load_tasks():
    if not STORE.exists():
        return []
    lines = STORE.read_text(encoding="utf-8").splitlines()
    return [line for line in lines if line.strip()]
def save_tasks(tasks):
    STORE.write_text("\n".join(tasks), encoding="utf-8")
def banner():
    print(f"\n{Fore.CYAN}=== TODO ({len(load_tasks())} tasks) ==={Style.RESET_ALL}")
    print(f"{Fore.CYAN}[1]{Style.RESET_ALL} ADD "
          f"{Fore.CYAN}[2]{Style.RESET_ALL} LIST "
          f"{Fore.CYAN}[3]{Style.RESET_ALL} TOGGLE DONE "
          f"{Fore.CYAN}[4]{Style.RESET_ALL} CLEAR ALL "
          f"{Fore.CYAN}[5]{Style.RESET_ALL} QUIT")
def add_task():
    task = input("Enter a new task: ").strip()
    if task:
        tasks = load_tasks()
        tasks.append(f"[ ] {task}")
        save_tasks(tasks)
        print(f"{Fore.GREEN}Task '{task}' added.{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}Task cannot be empty.{Style.RESET_ALL}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print(f"{Fore.YELLOW}No tasks found.{Style.RESET_ALL}")
        return
    for idx, task in enumerate(tasks, 1):
        print(f"{Fore.CYAN}[{idx}]{Style.RESET_ALL} {task}")
    try:
        n = int(input("Toggle #?: "))
        if 1 <= n <= len(tasks):
            if tasks[n - 1].startswith("[ ]"):
                tasks[n - 1] = tasks[n - 1].replace("[ ]", "[x]", 1)
                print(f"{Fore.GREEN}Task {n} marked as done.{Style.RESET_ALL}")
            elif tasks[n - 1].startswith("[x]"):
                tasks[n - 1] = tasks[n - 1].replace("[x]", "[ ]", 1)
                print(f"{Fore.YELLOW}Task {n} marked as not done.{Style.RESET_ALL}")
            save_tasks(tasks)
        else:
            print(f"{Fore.RED}Invalid task number.{Style.RESET_ALL}")
    except ValueError:
        print(f"{Fore.RED}Please enter a valid number.{Style.RESET_ALL}")
def clear_all():
    confirm = input("Are you sure you want to clear all tasks? (y/n): ").lower()
    if confirm == 'y':
        save_tasks([])
        print(f"{Fore.GREEN}All tasks cleared.{Style.RESET_ALL}")
    else:
        print(f"{Fore.YELLOW}Clear all cancelled.{Style.RESET_ALL}")
if __name__ == "__main__":
    tasks = load_tasks()
    while True:
        banner()
        choice = input("Choose an option: ").strip()
        if choice == '1':
            add_task()
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            list_tasks()
        elif choice == '4':
            clear_all()
        elif choice == '5':
            print(f"{Fore.CYAN}Exiting the to-do list application.{Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.RED}Invalid choice. Please select a valid option.{Style.RESET_ALL}")        