// src/components/TaskForm.js

import React, { useState } from 'react';
import { Button, TextField, FormControl, InputLabel, Select, MenuItem } from '@mui/material';
import { PlaylistAddOutlined } from '@mui/icons-material';

function TaskForm({ onAddTask }) {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [status, setStatus] = useState('pending');
  const [dueDate, setDueDate] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    const newTask = { title, description, status, dueDate };
    onAddTask(newTask);
    setTitle('');
    setDescription('');
    setStatus('pending');
    setDueDate('');
  };

  return (
    <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', padding: '2rem', maxWidth: '500px', margin: '0 auto' }}>
      <TextField
        fullWidth
        label="Title"
        variant="outlined"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        required
        margin="normal"
        sx={{ marginBottom: '1rem' }}
      />
      <FormControl fullWidth variant="outlined" margin="normal">
        <InputLabel>Status</InputLabel>
        <Select
          value={status}
          onChange={(e) => setStatus(e.target.value)}
          label="Status"
          sx={{ marginBottom: '1rem' }}
        >
          <MenuItem value="pending">Pending</MenuItem>
          <MenuItem value="completed">Completed</MenuItem>
        </Select>
      </FormControl>
      <TextField
        fullWidth
        label="Description"
        variant="outlined"
        multiline
        rows={4}
        value={description}
        onChange={(e) => setDescription(e.target.value)}
        margin="normal"
        sx={{ marginBottom: '1rem' }}
      />
      <TextField
        fullWidth
        label="Due Date"
        type="date"
        variant="outlined"
        value={dueDate}
        onChange={(e) => setDueDate(e.target.value)}
        InputLabelProps={{ shrink: true }}
        margin="normal"
        sx={{ marginBottom: '1rem' }}
      />
      <Button
        type="submit"
        variant="contained"
        color="primary"
        startIcon={<PlaylistAddOutlined />}
        sx={{ marginTop: '1rem', padding: '0.5rem 2rem' }}
      >
        Add Task
      </Button>
    </form>
  );
}

export default TaskForm;