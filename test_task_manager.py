import unittest
import datetime
from task_manager import Task, TaskManager

class TestTask(unittest.TestCase):
    def test_initialization(self):
        t = Task("Test Title", "2025-01-01", "Low", "Work")
        self.assertEqual(t.title, "test title")
        self.assertEqual(t.priority, "low")
        self.assertEqual(t.category, "work")
        self.assertFalse(t.completed)
        self.assertIsInstance(t.due_date, datetime.datetime)

    def test_mark_complete(self):
        t = Task("Another Task", "2025-01-01", "High", "Personal")
        t.mark_complete()
        self.assertTrue(t.completed)

    def test_is_overdue_future(self):
        future = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
        t = Task("Future Task", future, "Medium", "Chores")
        self.assertFalse(t.is_overdue())

    def test_is_overdue_past(self):
        t = Task("Past Task", "2000-01-01", "Medium", "Chores")
        self.assertTrue(t.is_overdue())

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()

    def test_add_task(self):
        self.manager.add_task("Sample", "2025-12-31", "Low", "Test")
        self.assertEqual(len(self.manager.tasks), 1)
        task = self.manager.tasks[0]
        self.assertEqual(task.title, "sample")

    def test_complete_task(self):
        self.manager.add_task("Finish", "2025-12-31", "High", "Work")
        self.manager.complete_task("Finish")
        self.assertTrue(self.manager.tasks[0].completed)

if __name__ == '__main__':
    unittest.main()
