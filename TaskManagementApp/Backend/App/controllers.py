from .models import Task

def add_task(conn, task: Task):
    sql = ''' INSERT INTO tasks(title, description, status, due_date)
              VALUES(?,?,?,?) '''
    cursor = conn.cursor()
    cursor.execute(sql, task.to_tuple())
    conn.commit()
    return cursor.lastrowid

def update_task(conn, task: Task):
    sql = ''' UPDATE tasks
              SET title = ?,
                  description = ?,
                  status = ?,
                  due_date = ?
              WHERE id = ? '''
    cursor = conn.cursor()
    cursor.execute(sql, task.to_tuple() + (task.id,))
    conn.commit()

def delete_task(conn, task_id):
    sql = 'DELETE FROM tasks WHERE id=?'
    cursor = conn.cursor()
    cursor.execute(sql, (task_id,))
    conn.commit()

def list_tasks(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()
    tasks = []
    for row in rows:
        tasks.append(Task(row[1], row[2], row[3], row[4], row[0]))
    return tasks
