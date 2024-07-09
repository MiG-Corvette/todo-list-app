import React, { useState, useEffect } from 'react';
import TodoList from '../components/TodoList';
import TodoForm from '../components/TodoForm';
import { getTodos, createTodo, updateTodo, deleteTodo } from '../services/api';

const TodoPage = () => {
  const [todos, setTodos] = useState([]);

  useEffect(() => {
    fetchTodos();
  }, []);

  const fetchTodos = async () => {
    const response = await getTodos();
    setTodos(response.data);
  };

  const handleCreate = async (newTodo) => {
    await createTodo(newTodo);
    fetchTodos();
  };

  const handleToggle = async (id) => {
    const todoToUpdate = todos.find(todo => todo.id === id);
    await updateTodo(id, { ...todoToUpdate, completed: !todoToUpdate.completed });
    fetchTodos();
  };

  const handleDelete = async (id) => {
    await deleteTodo(id);
    fetchTodos();
  };

  return (
    <div>
      <h1>TODO List</h1>
      <TodoForm onCreate={handleCreate} />
      <TodoList todos={todos} onToggle={handleToggle} onDelete={handleDelete} />
    </div>
  );
};

export default TodoPage;