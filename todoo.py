"""
TO-DO LIST MANAGER (Text-Based)

PURPOSE (Plain English):
- Help a person keep track of tasks they need to do.
- Let the person add new tasks, mark tasks as complete, view all tasks, or quit.

HOW YOU USE IT:
- Run the program. A simple menu appears with four choices.
- Type 1 to add a task (for example: "Pay bills").
- Type 2 to mark a task complete (you’ll pick the task by its number).
- Type 3 to view your task list (it shows which are Pending or Done).
- Type 4 to quit the program.

WHAT IT SHOWS:
- A numbered list of tasks.
- Each task shows a status: "❌ Pending" (not done yet) or "✅ Done" (completed).

DESIGN CHOICES (Simple & Safe):
- Tasks are kept in a list. Each item has a title (the text you typed) and a
  “done” flag (True/False) for whether the task is finished.
- The program checks for common mistakes (e.g., typing letters when numbers
  are expected) and does not crash. It shows a friendly message instead.
- Empty task names are not allowed, so you don’t end up with a “blank” task.

HOW TO RUN:
- You can run this in VSCode:
  1) Open the file (e.g., todo.py).
  2) Make sure the Python extension is installed and a Python 3 interpreter is selected.
  3) Press Ctrl/Cmd+F5 (Run Without Debugging) to start.
"""

# -----------------------------
# SECTION 1: Helper Functions
# -----------------------------

def show_menu():
    """
    PURPOSE:
    - Display the main choices the user can make.
    - This appears on every loop until the user chooses to quit.

    WHAT IT DOES:
    - Prints a labeled menu with four options.
    """
    print("\n===== TO-DO LIST MANAGER =====")
    print("1. Add a task")
    print("2. Mark task as complete")
    print("3. View tasks")
    print("4. Quit")
    print("==============================")


def view_tasks(tasks):
    """
    PURPOSE:
    - Show the user their current list of tasks and whether each one is done.

    INPUT:
    - tasks: a list where each item looks like {"title": <text>, "done": <True/False>}

    OUTPUT ON SCREEN:
    - If there are no tasks, says “No tasks yet!”.
    - Otherwise, prints a numbered list like:
        1. Pay bills [❌ Pending]
        2. Do homework [✅ Done]
    """
    if not tasks:
        print("\nNo tasks yet!")
        return

    print("\nYour Tasks:")
    for i, item in enumerate(tasks, start=1):
        status = "✅ Done" if item["done"] else "❌ Pending"
        print(f"{i}. {item['title']} [{status}]")


def add_task(tasks):
    """
    PURPOSE:
    - Ask the user for the text of a new task and add it to the list as “Pending”.

    INPUT:
    - tasks: the list of task dictionaries (modified in place).

    SAFETY CHECKS:
    - If the user types only spaces or nothing, the program refuses and explains why.

    RESULT:
    - A new task like {"title": "Pay bills", "done": False} is appended to the list.
    """
    task_text = input("Enter the task: ").strip()  # .strip() removes leading/trailing spaces
    if not task_text:
        print("Task cannot be empty.")
        return

    tasks.append({"title": task_text, "done": False})
    print(f"Task '{task_text}' added.")


def complete_task(tasks):
    """
    PURPOSE:
    - Let the user mark one task as complete by choosing a number from the list.

    INPUT:
    - tasks: the list of task dictionaries (modified in place).

    WHAT HAPPENS:
    - First, we display the tasks so the user can see the numbers.
    - If there are no tasks, we simply return.
    - Then we ask for the task number.
    - We convert the input to an integer and validate it.
    - If the input is invalid (letters, zero, too large, etc.), we show
      a friendly message and do nothing.

    RESULT:
    - If the choice is valid, we flip that task’s “done” status to True,
      and print a confirmation.
    """
    view_tasks(tasks)  # Show tasks first so the user knows what number to pick.
    if not tasks:
        return

    try:
        choice_text = input("Enter task number to mark complete: ").strip()
        choice = int(choice_text)  # This will fail if the user typed letters.
        # Convert human-friendly number (1-based) to computer index (0-based).
        index = choice - 1

        # This line will raise IndexError if the number is out of range.
        tasks[index]["done"] = True
        print(f"Task '{tasks[index]['title']}' marked as complete!")

    except ValueError:
        # This happens if the user typed something that isn’t a whole number (e.g., "abc").
        print("Invalid choice. Please enter a number that matches a task.")
    except IndexError:
        # This happens if the number is too small (0 or negative) or too large.
        print("Invalid choice. That task number does not exist.")


# -----------------------------
# SECTION 2: Main Program Loop
# -----------------------------

def main():
    """
    PURPOSE:
    - This is the “engine” that keeps the program running.
    - It creates the empty task list and then shows the menu over and over,
      reacting to the user’s choices.

    PROCESS:
    - Create an empty list named tasks.
    - Repeatedly:
        1) Show the menu.
        2) Ask the user for a choice (1, 2, 3, or 4).
        3) Perform the action:
           - 1: add a task
           - 2: mark a task complete
           - 3: view tasks
           - 4: quit (stop the loop)
        4) If the user types anything else, show a helpful message and continue.
    """
    tasks = []  # Start with no tasks. Each task is {"title": <text>, "done": <True/False>}

    while True:  # “Forever” loop—ends only when the user chooses 4 (Quit).
        show_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            complete_task(tasks)
        elif choice == "3":
            view_tasks(tasks)
        elif choice == "4":
            print("Goodbye! Stay organized ✨")
            break  # Exit the loop and end the program.
        else:
            print("Invalid option. Please type 1, 2, 3, or 4.")


# -----------------------------
# SECTION 3: Program Entry Point
# -----------------------------

if __name__ == "__main__":
    """
    PURPOSE:
    - This line means “only run main() if we launched this file directly”.
    - If someone imports this file into another Python file, main() won’t auto-run.
      That makes it easier to reuse or test parts of the code later.
    """
    main()
