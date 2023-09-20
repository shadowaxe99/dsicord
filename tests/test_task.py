
import unittest
from src.bot.commands import task

class TestTask(unittest.TestCase):

    def setUp(self):
        self.task = task.Task()

    def test_add_task(self):
        self.task.add_task("Test task")
        self.assertIn("Test task", self.task.tasks)

    def test_remove_task(self):
        self.task.add_task("Test task")
        self.task.remove_task("Test task")
        self.assertNotIn("Test task", self.task.tasks)

    def test_clear_tasks(self):
        self.task.add_task("Test task 1")
        self.task.add_task("Test task 2")
        self.task.clear_tasks()
        self.assertEqual(self.task.tasks, [])

if __name__ == '__main__':
    unittest.main()
