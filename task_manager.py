import datetime                     # Module 1: python fundamentals
from collections import Counter     # module 6: data container types part 2
import csv                          # Module 10: data analysis
import re                           # Module 8: regex
import sqlite3                      # Module 11: SQL
import requests                     # Module 12: HTTP requests
from bs4 import BeautifulSoup       # Module 13: web scraping

class Task:
    """
    Module 4: basics of OOP
    Defines every basic function within this manager:
    title, due date, priority, category, completion
    """

    # Module 5: container data types (part 1)

    def __init__(self, title, due_date, priority, category):
        self.title = title.strip().casefold()
        self.due_date = datetime.datetime.strptime(due_date.strip(), "%Y-%m-%d")
        self.priority = priority.strip().casefold()
        self.category = category.strip().casefold()
        self.completed = False

    # Module 7: Advanced OOP (method behavior)

    def mark_complete(self):
        self.completed = True

    def is_overdue(self):
        return not self.completed and datetime.datetime.now() > self.due_date

    def __str__(self):
        status = "Done" if self.completed else "Pending"
        return (
            f"{self.title.title()} | Due: {self.due_date.date()} "
            f"| Priority: {self.priority.title()} | Category: {self.category.title()} | Status: {status}"
        )

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, due_date, priority, category):
        # Module 2: python fundamentals pt 2
        try:
            task = Task(title, due_date, priority, category)
            self.tasks.append(task)
            print("Task added successfully.")
        except ValueError:
            print(" Invalid date format. Use YYYY-MM-DD.")

    def complete_task(self, title):
        for task in self.tasks:
            if task.title == title.strip().casefold():
                task.mark_complete()
                print("Task marked as complete.")
                return
        print("Task not found.")

    def show_tasks(self, filter_type="all"):
        print("\n=== Task List ===")
        for task in self.tasks:
            if filter_type == "all":
                print(task)
            elif filter_type == "pending" and not task.completed:
                print(task)
            elif filter_type == "completed" and task.completed:
                print(task)
            elif filter_type == "overdue" and task.is_overdue():
                print(task)
        print()

    def analytics(self):
        total = len(self.tasks)
        completed = len([t for t in self.tasks if t.completed])
        category_count = Counter([t.category for t in self.tasks])
        most_common = category_count.most_common(1)

        print(f"\n=== Task Analytics ===")
        print(f"Total tasks: {total}")
        print(f"Completed: {completed} ({(completed / total) * 100:.2f}%)" if total else "Completed: 0")
        if most_common:
            print(f"Most common category: {most_common[0][0].title()} ({most_common[0][1]} times)")
        print()

    # Module 10: data analysis (CSV)

    def export_to_csv(self, filename="tasks_export.csv"):
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Title", "Due Date", "Priority", "Category", "Completed"])
            for task in self.tasks:
                writer.writerow([
                    task.title.title(),
                    task.due_date.date(),
                    task.priority.title(),
                    task.category.title(),
                    "Yes" if task.completed else "No"
                    ])
        print(f"Tasks exported to {filename}")  


    # Module 11: SQL

    def save_to_db(self, db_name="tasks.db"):
        conn = sqlite3.connect(db_name)
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                title TEXT,
                due_date TEXT,
                priority TEXT,
                category TEXT,
                completed INTEGER,
                UNIQUE(title, due_date)
            )
        ''')
        for task in self.tasks:
            c.execute("""
                INSERT OR REPLACE INTO tasks
                (title, due_date, priority, category, completed)
                VALUES (?, ?, ?, ?, ?)
            """, (
                task.title.title(),
                str(task.due_date.date()),
                task.priority.title(),
                task.category.title(),
                int(task.completed)
            ))
        conn.commit()
        conn.close()
        print(f"Tasks saved to database '{db_name}'.")


    # Module 13: web scraping

    def fetch_tasks_from_web(self, url):
        """ Scrapes all <li> items from the given URL and prints them
        (or optionally adds them as tasks).
        """
        try:
            resp = requests.get(url)
            resp.raise_for_status()
            soup = BeautifulSoup(resp.text, "html.parser")
            items = soup.find_all("li")
            if not items:
                print("No <li> elements found at that URL.")
                return
            print("Scraped tasks:")
            for i, li in enumerate(items, 1):
                text = li.get_text(strip=True)
                print(f"  {i}. {text}")
        except Exception as e:
            print(f"Error scraping tasks: {e}")


# Module 12: data on web

def fetch_sample_task():
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
        if response.status_code == 200:
            data = response.json()
            print(f"Sample Task Suggestion: {data['title'].title()}")
        else:
            print("Could not fetch sample task.")
    except Exception as e:
        print(f"Error fetching task: {e}")


def main():
    manager = TaskManager()

    while True:
        print("=== Task Manager ===")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. Show Tasks (all/pending/completed/overdue)")
        print("4. Show Analytics")
        print("5. Export Tasks to CSV")
        print("6. Save Tasks to SQL Database")
        print("7. Need help? Get Task Suggestion from Web")
        print("8. Scrape Tasks from Web Page")
        print("9. Exit")

        choice = input("Choose an option (1-9): ").strip()

        if choice == "1":
            title = input("Task title: ")
            due = input("Due date (YYYY-MM-DD): ")
            priority = input("Priority (High/Medium/Low): ")
            category = input("Category: ")

            # Module 8: regex

            if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", due.strip()):
                print("Date must be YYYY-MM-DD")
                continue

            if not re.fullmatch(r"[A-Za-z0-9 ]+", category.strip().casefold()):
                print("Category contains invalid characters.")
                continue

            manager.add_task(title, due, priority, category)


        elif choice == "2":
            title = input("Enter title of task to complete: ")
            manager.complete_task(title)

        elif choice == "3":
            filter_type = input("Filter (all/pending/completed/overdue): ").strip().casefold()
            manager.show_tasks(filter_type)

        elif choice == "4":
            manager.analytics()

        elif choice == "5":
            manager.export_to_csv()

        elif choice == "6":
            manager.save_to_db()

        elif choice == "7":
            fetch_sample_task()    
        
        elif choice == "8":
            url = input("Enter URL of page to scrape: ")
            manager.fetch_tasks_from_web(url)

        elif choice == "9":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
