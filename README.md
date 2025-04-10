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
