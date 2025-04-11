# CollabManager Pro

A CLI-based project collaboration tool using Python and SQLite.

## Features
- Multi-user login with roles (admin, manager, member)
- Create/join projects
- Assign and manage tasks
- Export reports to CSV

## Getting Started
1. Clone the repo
2. Create virtual environment: `python -m venv venv`
3. Activate it:
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`
4. Install dependencies (if any): `pip install -r requirements.txt`
5. Run: `python main.py`

## Tasks
- Person A: `auth.py`, `projects.py`, `db/schema.sql`
- Person B: `tasks.py`, `reporting.py`, CLI improvements

## License
MIT


👥 Team Roles Breakdown (3 People)
🔹 Person A – User Management & Project Control
Focus: Setting up users and managing projects
Files to work on:

auth.py

User registration and login logic

Role validation (admin, manager, member)

projects.py

Create new projects

Join existing projects

Manage project_members table entries

db/schema.sql

Help define tables for users, projects, project_members

🔹 Person B – Task System Developer
Focus: Task creation, updates, and organization
Files to work on:

tasks.py

Create, update, and list tasks

Filtering by project, user, or status

Implement logic for status changes, priorities, and deadlines

main.py (shared task)

Work with Person C to plug in task-related options into the CLI menu

🔹 Person C – Reporting, Utilities & CLI Integration
Focus: File exports, database connectivity, and user interface
Files to work on:

reporting.py

Export task data into CSV files

Allow managers to generate reports

utils.py

Set up the SQLite database connection (connect_db function)

Help with shared helper functions

main.py

Build the CLI menu

Connect all the modules together so that the app runs smoothly
