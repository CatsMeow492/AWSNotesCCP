import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [questions, setQuestions] = useState([]);
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [selectedOptions, setSelectedOptions] = useState([]);
  const [score, setScore] = useState(0);

  useEffect(() => {
    fetch('/questions')
      .then(response => response.json())
      .then(data => setQuestions(data));
  }, []);

  const handleOptionChange = (index) => {
    setSelectedOptions(prev => {
      if (prev.includes(index)) {
        return prev.filter(i => i !== index);
      } else {
        return [...prev, index];
      }
    });
  };

  const handleSubmit = () => {
    const question = questions[currentQuestion];
    fetch('/check_answer', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        question_id: question.id,
        choices: selectedOptions,
      }),
    })
      .then(response => response.json())
      .then(data => {
        if (data.correct) {
          setScore(score + 1);
        }
        setSelectedOptions([]);
        setCurrentQuestion(currentQuestion + 1);
      });
  };

  if (questions.length === 0) {
    return <div>Loading...</div>;
  }

  if (currentQuestion >= questions.length) {
    return <div>Your final score is: {score}</div>;
  }

  const question = questions[currentQuestion];

  return (
    <div className="App">
      <h1>{question.question}</h1>
      {question.options.map((option, index) => (
        <div key={index}>
          <input
            type="checkbox"
            checked={selectedOptions.includes(index)}
            onChange={() => handleOptionChange(index)}
          />
          {option.text}
        </div>
      ))}
      <button onClick={handleSubmit}>Submit</button>
    </div>
  );
}

export default App;