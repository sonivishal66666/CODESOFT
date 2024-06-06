import os

def banner():

    print("     TO DO LIST    ")
   

def add_task():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner()
    task = input("Enter Your new Task Here: ")
    save = input("Save? (y/n): ")
    if save.lower() == 'y':
        with open("todo.txt", "a") as fout:
            fout.write(f"\nTask: {task}\n")
        more = input("Do you want to Add more tasks? (y/n): ")
        if more.lower() == 'y':
            add_task()
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Tasks added successfully.")

def show_tasks():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner()
    print("Tasks:")
    with open("todo.txt", "r") as fin:
        for line in fin:
            print(line.strip())

def search_task():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner()
    task = input("Enter task to search: ")
    found = False
    with open("todo.txt", "r") as fin:
        for line in fin:
            if task in line:
                print(f"Task found: {line.strip()}")
                found = True
    if not found:
        print("Task not found.")

def delete_task():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner()
    task = input("Enter your task to delete: ")
    found = False
    with open("todo.txt", "r") as fin, open("temp.txt", "w") as temp:
        for line in fin:
            if task in line:
                print(f"Task deleted: {line.strip()}")
                found = True
            else:
                temp.write(line)
    if not found:
        print("Task not found.")
    os.remove("todo.txt")
    os.rename("temp.txt", "todo.txt")

def update_task():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner()
    task = input("Enter Your task to update: ")
    found = False
    with open("todo.txt", "r") as fin, open("temp.txt", "w") as temp:
        for line in fin:
            if task in line:
                new_task = input("Enter new task: ")
                temp.write(f"\nTask: {new_task}\n")
                print("Task got updated.")
                found = True
            else:
                temp.write(line)
    if not found:
        print("Task not found.")
    os.remove("todo.txt")
    os.rename("temp.txt", "todo.txt")

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        banner()
        print("\t1. Add task")
        print("\t2. Show tasks")
        print("\t3. Search task")
        print("\t4. Delete task")
        print("\t5. Update task")
        choice = input("Enter choice: ")
        if choice == '1':
            add_task()
        elif choice == '2':
            show_tasks()
        elif choice == '3':
            search_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            update_task()
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
