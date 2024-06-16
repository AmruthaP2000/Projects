from flask import Flask, request, jsonify
from .database import create_connection
from .controllers import add_task, update_task, delete_task, list_tasks
from .models import Task

app = Flask(__name__)

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.json
    title = data['title']
    description = data['description']
    status = data['status']
    due_date = data['dueDate']

    task = Task(title, description, status, due_date)
    conn = create_connection("tasks.db")
    task_id = add_task(conn, task)
    conn.close()

    return jsonify({"id": task_id, "message": "Task created successfully"}), 201

# Add more routes as needed

if __name__ == '__main__':
    app.run(debug=True)
