import sqlite3

def connect_db():
    return sqlite3.connect('collabmanager.db')

def register_user():
    username = input("Enter username: ")
    password = input("Enter password: ")
    role = input("Enter role (admin/manager/member): ")

    conn = connect_db()
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", (username, password, role))
        conn.commit()
        print("User registered successfully!")
    except sqlite3.IntegrityError:
        print("Username already exists.")
    finally:
        conn.close()

def login_user():
    username = input("Enter username: ")
    password = input("Enter password: ")

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()

    if user:
        print("Login successful!")
        return user  # Return the user details to keep track of their session
    else:
        print("Invalid credentials.")
        return None
