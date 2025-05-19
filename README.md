# INST326 Task Manager

A command-line Task Manager built in Python. It utilizes concepts from Modules 1–13 of INST326.

## Usage

1. **Running the application**
   python task_manager.py

2. **Follow the menu prompts (1–9):**
   1-3. Add, complete, and view tasks (pending/completed/overdue)
   4 Generate analytics (counts & percentages)
   5 Export tasks to CSV
   6 Persist tasks to SQLite database
   7 Fetch a sample task from an API
   8 Scrape tasks from any HTML list
   9 Exit the program

## Demo Scripts

- **Load from database:**
  python load_tasks.py

  Displays all tasks currently stored in tasks.db.

- **HTML scraping demo:**
  1. Serve sample.html locally:

     python -m http.server 8000

  2. In the app, choose option 8 and enter:

     http://localhost:8000/sample.html


## Testing

Run the unit tests to verify core functionality:

python -m unittest test_task_manager.py

## GitHub Repository

View the full commit history and collaborate on GitHub:

`https://github.com/bensimcard/INST326_final`

---

Prepared by: Ben Sim
