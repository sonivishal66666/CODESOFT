import os

# Function to display the banner
def display_banner():
    print("======TO DO LIST======")

# Function to add a new task
def add_new_task():
    os.system('cls' if os.name == 'nt' else 'clear')
    display_banner()
    task = input("Enter your new task: ")
    save = input("Save? (y/n): ")
    if save.lower() == 'y':
        with open("todo.txt", "a") as file_out:
            file_out.write(f"Task: {task}\n")
        more = input("Do you want to add more tasks? (y/n): ")
        if more.lower() == 'y':
            add_new_task()
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Tasks added successfully.")

# Function to display all tasks
def show_all_tasks():
    os.system('cls' if os.name == 'nt' else 'clear')
    display_banner()
    print("Tasks:")
    with open("todo.txt", "r") as file_in:
        for line in file_in:
            print(line.strip())

# Function to search for a specific task
def search_for_task():
    os.system('cls' if os.name == 'nt' else 'clear')
    display_banner()
    task = input("Enter task to search: ")
    found = False
    with open("todo.txt", "r") as file_in:
        for line in file_in:
            if task in line:
                print(f"Task found: {line.strip()}")
                found = True
    if not found:
        print("Task not found.")

# Function to delete a task
def remove_task():
    os.system('cls' if os.name == 'nt' else 'clear')
    display_banner()
    task = input("Enter the task to delete: ")
    found = False
    with open("todo.txt", "r") as file_in, open("temp.txt", "w") as temp_file:
        for line in file_in:
            if task in line:
                print(f"Task deleted: {line.strip()}")
                found = True
            else:
                temp_file.write(line)
    if not found:
        print("Task not found.")
    os.remove("todo.txt")
    os.rename("temp.txt", "todo.txt")

# Function to update an existing task
def modify_task():
    os.system('cls' if os.name == 'nt' else 'clear')
    display_banner()
    task = input("Enter the task to update: ")
    found = False
    with open("todo.txt", "r") as file_in, open("temp.txt", "w") as temp_file:
        for line in file_in:
            if task in line:
                new_task = input("Enter the new task: ")
                temp_file.write(f"Task: {new_task}\n")
                print("Task updated successfully.")
                found = True
            else:
                temp_file.write(line)
    if not found:
        print("Task not found.")
    os.remove("todo.txt")
    os.rename("temp.txt", "todo.txt")

# Main function to display the menu and handle user input
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        display_banner()
        print("\t1. Add task")
        print("\t2. Show tasks")
        print("\t3. Search task")
        print("\t4. Delete task")
        print("\t5. Update task")
        choice = input("Enter choice: ")
        if choice == '1':
            add_new_task()
        elif choice == '2':
            show_all_tasks()
        elif choice == '3':
            search_for_task()
        elif choice == '4':
            remove_task()
        elif choice == '5':
            modify_task()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
