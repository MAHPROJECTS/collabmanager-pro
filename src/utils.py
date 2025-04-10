def connect_db():
    import sqlite3
    return sqlite3.connect("collabmanager.db")
