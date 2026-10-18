
#Name: Nwobi Golibe
#This is a program that will create a 'to-do' list

def add_task(tasks):
    """Adds a new task to the list if it's not a duplicate."""
    task = input("What task do you want to add?: ").strip()
    if task and task not in tasks:
        tasks.append(task)
        print(f'{task} has been added to the list')
    elif task:
        print("Task already exists in the list.")
    else:
        print("Enter a valid task to add.")

def remove_item(tasks):
    """Removes an existing task from the list if found."""
    if not tasks:
        print("There are no items to remove.")
        return
    item = input("What item do you want to remove?: ").strip()
    if item in tasks:
        tasks.remove(item)
        print(f'{item} has been removed from the list')
    else:
        print("Item not found in the list.")

def display_tasks(tasks):
    """Displays all tasks in the list."""
    print("\nYour Very Own To-Do List:")
    if tasks:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("No tasks available in your list.")

def show_menu():
    """Displays the menu options to the user."""
    print("\nWhat do you want to do?:")
    print("A - Add Task")
    print("D - Delete Item")
    print("V - View List")
    print("X - Exit")

def main():
    """Main function to run the to-do list program in a loop until the user exits."""
    tasks = []
    while True:
        show_menu()
        choice = input("Choose (A/D/V/X): ").strip().upper()
        if choice == "A":
            add_task(tasks)
        elif choice == "D":
            remove_item(tasks)
        elif choice == "V":
            display_tasks(tasks)
        elif choice == "X":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
