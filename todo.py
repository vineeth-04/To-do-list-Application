import json

class Task:
    def __init__(self, title, description, category):
        self.title = title
        self.description = description
        self.category = category
        self.completed = False

    def mark_completed(self):
        self.completed = True

def save_tasks(tasks):
    with open('tasks.json', 'w') as f:
        json.dump([task.__dict__ for task in tasks], f)

def load_tasks():
    try:
        with open('tasks.json', 'r') as f:
            return [Task(**data) for data in json.load(f)]
    except FileNotFoundError:
        return []

def display_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    for idx, task in enumerate(tasks, start=1):
        status = "✅ Completed" if task.completed else "❌ Not Completed"
        print(f"{idx}. {task.title} ({task.category}) - {status}")
        print(f"   Description: {task.description}")

def main():
    tasks = load_tasks()
    while True:
        print("\n===== Personal To-Do List =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter description: ")
            category = input("Enter category (Work/Personal/Urgent): ")
            tasks.append(Task(title, description, category))

        elif choice == '2':
            display_tasks(tasks)

        elif choice == '3':
            display_tasks(tasks)
            try:
                index = int(input("Enter task number to mark as completed: ")) - 1
                if 0 <= index < len(tasks):
                    tasks[index].mark_completed()
            except:
                print("Invalid input.")

        elif choice == '4':
            display_tasks(tasks)
            try:
                index = int(input("Enter task number to delete: ")) - 1
                if 0 <= index < len(tasks):
                    tasks.pop(index)
            except:
                print("Invalid input.")

        elif choice == '5':
            save_tasks(tasks)
            print("Tasks saved. Exiting...")
            break

if __name__ == "__main__":
    main()
