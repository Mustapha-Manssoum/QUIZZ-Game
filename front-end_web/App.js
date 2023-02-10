import React, { useState } from "react";
import { BrowserRouter, Link } from 'react-router-dom';

import logo from './logo.svg';
import './App.css';
import Quiz from './Quiz.jsx';

import Audio from './Audio.jsx';
import Question from './Question.jsx'
import { Login } from "./Login";
import { Register } from "./Register";


function App() {
  const [currentForm, setCurrentForm] = useState('login');

  const toggleForm = (formName) => {
    setCurrentForm(formName);
  }

  return (
    <div className="App">
      {
        currentForm === "login" ? <Login onFormSwitch={toggleForm} /> : 
        currentForm === "register" ? <Register onFormSwitch={toggleForm} /> : 
        currentForm === "Quiz" ? <Quiz onFormSwitch={toggleForm} /> :
 
        <Audio />

      }
      
    </div>

  );
}

export default App;
