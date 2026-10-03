class Task():
    def __init__(self, name, description, priority):
        self.name = name
        self.description = description
        self.priority = priority


class ToDoList():
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def show_tasks(self):
        if not self.tasks:
            print('No Tasks Found')
            return

        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task.name}")
            print(f"   Description: {task.description}")
            print(f"   Priority: {task.priority}")
            print("-" * 30)

    def delete_task(self, index):
        if 1 <= index <= len(self.tasks):
            removed_task = self.tasks.pop(index - 1)
            print(f"Task '{removed_task.name}' deleted.")
        else:
            print("Invalid task number.")

todo = ToDoList()



while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. Show Tasks")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter task name: ")
        description = input("Enter description: ")
        priority = input("Enter priority (High/Medium/Low): ")

        task = Task(name, description, priority)
        todo.add_task(task)

        print("Task added successfully.")

    elif choice == "2":
        todo.show_tasks()

        if todo.tasks:
            number = int(input("Enter task number to delete: "))
            todo.delete_task(number)

    elif choice == "3":
        todo.show_tasks()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")