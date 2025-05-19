import sqlite3
from task_manager import Task

conn = sqlite3.connect("tasks.db")
c = conn.cursor()
c.execute("SELECT * FROM tasks")
for row in c.fetchall():
    print(row)
conn.close()
