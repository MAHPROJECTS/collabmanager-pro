import sqlite3

def connect_db():
    return sqlite3.connect('collabmanager.db')

def create_project(user_id):
    name = input("Enter project name: ")
    description = input("Enter project description: ")

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO projects (name, description, created_by) VALUES (?, ?, ?)", (name, description, user_id))
    conn.commit()

    project_id = cursor.lastrowid  # Get the ID of the newly created project
    print(f"Project '{name}' created successfully with ID {project_id}.")
    conn.close()

def join_project(user_id):
    project_id = int(input("Enter project ID to join: "))

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM projects WHERE id = ?", (project_id,))
    project = cursor.fetchone()

    if project:
        cursor.execute("INSERT INTO project_members (user_id, project_id) VALUES (?, ?)", (user_id, project_id))
        conn.commit()
        print(f"Joined project '{project[1]}' successfully.")
    else:
        print("Project not found.")
    conn.close()
