import unittest
from App.database import create_connection, create_table
from App.controllers import add_task, update_task, delete_task, list_tasks
from App.models import Task

class TestControllers(unittest.TestCase):
    def setUp(self):
        self.conn = create_connection(":memory:")
        create_table(self.conn)

    def tearDown(self):
        self.conn.close()

    def test_add_task(self):
        task = Task('Test Task', 'This is a test', 'pending', '2024-06-20')
        task_id = add_task(self.conn, task)
        self.assertGreater(task_id, 0)

    def test_update_task(self):
        task = Task('Test Task', 'This is a test', 'pending', '2024-06-20')
        task_id = add_task(self.conn, task)
        updated_task = Task('Updated Task', 'Updated description', 'completed', '2024-06-21', task_id)
        update_task(self.conn, updated_task)
        tasks = list_tasks(self.conn)
        self.assertEqual(tasks[0].title, 'Updated Task')

    def test_delete_task(self):
        task = Task('Test Task', 'This is a test', 'pending', '2024-06-20')
        task_id = add_task(self.conn, task)
        delete_task(self.conn, task_id)
        tasks = list_tasks(self.conn)
        self.assertEqual(len(tasks), 0)

    def test_list_tasks(self):
        task1 = Task('Task 1', 'First task', 'pending', '2024-06-20')
        task2 = Task('Task 2', 'Second task', 'completed', '2024-06-21')
        add_task(self.conn, task1)
        add_task(self.conn, task2)
        tasks = list_tasks(self.conn)
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0].title, 'Task 1')
        self.assertEqual(tasks[1].title, 'Task 2')

if __name__ == '__main__':
    unittest.main()
