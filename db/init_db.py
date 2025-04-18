import sqlite3

def initialize_database():
    # Open the schema.sql file to create the tables
    with open('schema.sql', 'r') as f:
        sql_script = f.read()

    # Connect to the SQLite database (will create a new database file if it doesn't exist)
    conn = sqlite3.connect('collabmanager.db')
    cursor = conn.cursor()

    # Execute the SQL script to initialize the database
    cursor.executescript(sql_script)
    
    # Commit and close the connection
    conn.commit()
    conn.close()

    print("✅ Database initialized!")

# Call the function to initialize the database
initialize_database()
