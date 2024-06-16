// src/App.js

import React from 'react';
import TaskForm from './components/TaskForm';
import './App.css';

function App() {
    const handleAddTask = async (task) => {
        try {
            const response = await fetch('http://localhost:5000/tasks', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(task),
            });
            const data = await response.json();
            console.log(data);
        } catch (error) {
            console.error('Error adding task:', error);
        }
    };

    return (
        <div className="App">
            <h1>Task Management App</h1>
            <TaskForm onAddTask={handleAddTask} />
        </div>
    );
}

export default App;
