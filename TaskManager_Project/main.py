from task_manager import TaskManager


def show_menu():
    print("\n=== TASK MANAGER ===")
    print("1. Add task")
    print("2. List all tasks")
    print("3. List incomplete tasks")
    print("4. Complete task")
    print("5. Delete task")
    print("6. Exit")


def add_task_cli(manager):
    title = input("Enter task title: ").strip()
    if not title:
        print("Task title cannot be empty.")
        return

    priority = input("Enter priority (low/medium/high): ").strip().lower()
    if priority not in ["low", "medium", "high"]:
        priority = "low"

    task = manager.add_task(title, priority)
    print(f"Task added: {task}")


def list_tasks_cli(manager, show_done=True):
    tasks = manager.list_tasks(show_done=show_done)

    if not tasks:
        print("No tasks found.")
        return

    print("\nTasks:")
    for task in tasks:
        print(task)


def complete_task_cli(manager):
    try:
        task_id = int(input("Enter task ID to complete: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if manager.complete_task(task_id):
        print("Task marked as complete.")
    else:
        print("Task not found.")


def delete_task_cli(manager):
    try:
        task_id = int(input("Enter task ID to delete: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if manager.delete_task(task_id):
        print("Task deleted.")
    else:
        print("Task not found.")


def main():
    manager = TaskManager()

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_task_cli(manager)
        elif choice == "2":
            list_tasks_cli(manager, show_done=True)
        elif choice == "3":
            list_tasks_cli(manager, show_done=False)
        elif choice == "4":
            complete_task_cli(manager)
        elif choice == "5":
            delete_task_cli(manager)
        elif choice == "6":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Please select 1 to 6.")


if __name__ == "__main__":
    main()
# Without line 90
# every file that imports your module accidently runs the code
# with it - code only runs when you explicitly runs the module directly.
