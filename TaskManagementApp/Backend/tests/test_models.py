import unittest
from App.models import Task

class TestTaskModel(unittest.TestCase):
    def test_task_creation(self):
        task = Task('Test Task', 'This is a test', 'pending', '2024-06-20')
        self.assertEqual(task.title, 'Test Task')
        self.assertEqual(task.description, 'This is a test')
        self.assertEqual(task.status, 'pending')
        self.assertEqual(task.due_date, '2024-06-20')

if __name__ == '__main__':
    unittest.main()
