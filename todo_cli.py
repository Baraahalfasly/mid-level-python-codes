import os

class ToDoList:
    def __init__(self, filename):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                self.tasks = [line.strip() for line in file.readlines()]
        else:
            self.tasks = []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            for task in self.tasks:
                file.write(task + '\n')

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()

    def remove_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            removed = self.tasks.pop(task_number - 1)
            self.save_tasks()
            print(f"Task removed: {removed}")
        else:
            print("Invalid task number.")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("Your To-Do List:")
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")

# ---- Main Program ----
todo = ToDoList('tasks.txt')

while True:
    print("\nChoose an option:")
    print("1. Show tasks")
    print("2. Add a task")
    print("3. Remove a task")
    print("4. Exit")

    choice = input("Your choice: ")

    if choice == '1':
        todo.show_tasks()
    elif choice == '2':
        task = input("Enter the task: ")
        todo.add_task(task)
        print("Task added.")
    elif choice == '3':
        todo.show_tasks()
        num = int(input("Enter task number to remove: "))
        todo.remove_task(num)
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
