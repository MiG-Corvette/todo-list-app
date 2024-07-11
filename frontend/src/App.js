import React, { useState, useEffect } from 'react';
import axios from 'axios';

const App = () => {
  // Todo リストのデータ状態を管理する useState フック
  const [todos, setTodos] = useState([]);

  // コンポーネントマウント時に実行される useEffect フック
  useEffect(() => {
    // バックエンド API に GET リクエストを送信
    axios.get('http://localhost:8000/todos/')
      // レスポンスが成功した場合
      .then(response => {
        // レスポンスデータ (Todo リスト) を state に設定
        setTodos(response.data);
      })
      // レスポンスが失敗した場合
      .catch(error => {
        // エラー内容をコンソールに出力
        console.error(error);
      });
  }, []);

  // JSX で Todo リストを表示
  return (
    <div>
      {todos.map(todo => (
        <div key={todo.id}>
          <h2>{todo.title}</h2>
          <p>{todo.description}</p>
        </div>
      ))}
    </div>
  );
};

export default App;