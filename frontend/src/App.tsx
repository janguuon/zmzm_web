import React, { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
  const [data, setData] = useState("");

  useEffect(() => {
    // FastAPI로부터 데이터 가져오기
    axios.get('http://127.0.0.1:8000/api/data')
      .then(response => {
        setData(response.data.message); // FastAPI의 응답 데이터
      })
      .catch(error => {
        console.error("There was an error fetching data:", error);
      });
  }, []);

  return (
    <div className="App">
      <h1>React와 FastAPI 연동</h1>
      <p>{data}</p>
    </div>
  );
}

export default App;
