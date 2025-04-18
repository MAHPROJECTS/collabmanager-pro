from src import auth, projects, tasks, reporting

def main():
    while True:
        print("\n=== CollabManager Pro ===")
        print("1. Register")
        print("2. Login")
        print("3. Create Project")
        print("4. Join Project")
        print("5. Create Task")
        print("6. Update Task")
        print("7. View Tasks")
        print("8. Export Report")
        print("9. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            print("         ")
            print("Register:")
            auth.register_user()
        elif choice == '2':
            print("         ")
            print("Login:")
            auth.login_user()
        elif choice == '3':
            print("         ")
            print("Create Project:")
            projects.create_project()
        elif choice == '4':
            print("         ")
            print("Join Project:")
            projects.join_project()
        elif choice == '5':
            print("         ")
            print("Create Task:")
            tasks.create_task()
        elif choice == '6':
            print("         ")
            print("Update Task:")
            tasks.update_task()
        elif choice == '7':
            print("         ")
            print("View Tasks:")
            tasks.list_tasks()
        elif choice == '8':
            print("         ")
            ("Export Report:")
            reporting.export_tasks_to_csv()
        elif choice == '9':
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
