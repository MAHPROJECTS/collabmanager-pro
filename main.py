from src import auth, projects, tasks, reporting

def main():
    current_user = None
    current_project = None

    while True:
        print("\n=== CollabManager Pro ===")
        print("1. Register")
        print("2. Login")
        print("3. Create Project")
        print("4. Join Project")
        print("5. Create Task")
        print("6. View Tasks")
        print("7. Update Task")
        print("8. Generate Report")
        print("9. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            print("         ")
            print("Register:")
            auth.register_user()
        elif choice == '2':
=======
            current_user = auth.login_user()
            if current_user:
                print(f"Welcome, {current_user[1]}!")
            else:
                print("Login failed. Try again.")
        elif choice == '3':
            if current_user:
                project_name = input("Enter project name: ")
                current_project = projects.create_project(current_user[0], project_name)
                if current_project:
                    print(f"Project '{current_project['name']}' created successfully!")
                else:
                    print("Failed to create project.")
            else:
                print("Please log in first.")
        elif choice == '4':
            if current_user:
                project_name = input("Enter the project name to join: ")
                current_project = projects.join_project(current_user[0], project_name)
                if current_project:
                    print(f"Joined project '{current_project['name']}' successfully!")
                else:
                    print("Project not found or failed to join.")
            else:
                print("Please log in first.")
        elif choice == '5':
            if current_user:
                if current_project is None:
                    print("You need to join or create a project first.")
                else:
                    task_name = input("Enter task name: ")
                    task_description = input("Enter task description: ")
                    task = tasks.create_task(current_user[0], current_project['id'], task_name, task_description)
                    if task:
                        print(f"Task '{task['name']}' created successfully!")
                    else:
                        print("Failed to create task.")
            else:
                print("Please log in first.")
        elif choice == '6':
            if current_user:
                if current_project is None:
                    print("You need to join or create a project first.")
                else:
                    tasks.list_tasks(current_project['id'])
            else:
                print("Please log in first.")
        elif choice == '7':
            if current_user:
                task_id = int(input("Enter task ID to update: "))
                task_name = input("Enter new task name: ")
                task_description = input("Enter new task description: ")
                task = tasks.update_task(current_user[0], task_id, task_name, task_description)
                if task:
                    print(f"Task '{task['name']}' updated successfully!")
                else:
                    print("Failed to update task.")
            else:
                print("Please log in first.")
        elif choice == '8':
            if current_user:
                reporting.generate_report(current_user[0])
            else:
                print("Please log in first.")
>>>>>>> 7c99c53 (Updated main.py)
        elif choice == '9':
            print("Exiting program...")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
