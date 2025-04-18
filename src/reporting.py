import sqlite3

def connect_db():
    return sqlite3.connect('collabmanager.db')

def generate_report(user_id):
    conn = connect_db()
    cursor = conn.cursor()

    # Get the user's projects
    cursor.execute("SELECT * FROM projects WHERE created_by = ?", (user_id,))
    projects = cursor.fetchall()

    if not projects:
        print("No projects found for this user.")
        conn.close()
        return

    print("\n=== Report: Projects Created by User ===")
    for project in projects:
        print(f"Project ID: {project[0]}, Name: {project[1]}, Description: {project[2]}")

        # List tasks for each project
        cursor.execute("SELECT * FROM tasks WHERE project_id = ?", (project[0],))
        tasks = cursor.fetchall()

        if tasks:
            print("\nTasks in this project:")
            for task in tasks:
                print(f"  Task ID: {task[0]}, Title: {task[1]}, Status: {task[5]}, Priority: {task[6]}")
        else:
            print("  No tasks for this project.")

    conn.close()
