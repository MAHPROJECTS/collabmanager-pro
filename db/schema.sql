CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    role TEXT CHECK(role IN ('admin', 'manager', 'member')) NOT NULL
);

CREATE TABLE projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    created_by INTEGER,
    FOREIGN KEY(created_by) REFERENCES users(id)
);

CREATE TABLE project_members (
    user_id INTEGER,
    project_id INTEGER,
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(project_id) REFERENCES projects(id),
    PRIMARY KEY(user_id, project_id)
);

CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    deadline TEXT,
    status TEXT CHECK(status IN ('todo', 'in progress', 'done')) DEFAULT 'todo',
    priority TEXT CHECK(priority IN ('low', 'medium', 'high')),
    assigned_to INTEGER,
    project_id INTEGER,
    FOREIGN KEY(assigned_to) REFERENCES users(id),
    FOREIGN KEY(project_id) REFERENCES projects(id)
);
