import unittest
from App.database import create_connection, create_table

class TestDatabase(unittest.TestCase):
    def test_create_connection(self):
        conn = create_connection(":memory:")
        self.assertIsNotNone(conn)

    def test_create_table(self):
        conn = create_connection(":memory:")
        create_table(conn)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='tasks'")
        table = cursor.fetchone()
        self.assertIsNotNone(table)

if __name__ == '__main__':
    unittest.main()
