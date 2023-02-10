import React, { useState, useRef } from "react";

const RecordButton = () => {
  const [recording, setRecording] = useState(false);
  const mediaRecorderRef = useRef(null);
  const chunksRef = useRef([]);

  const [question, setQuestion] = useState('Quelle est la capitale de la France?');
  const [answer, setAnswer] = useState('');
  const [score, setScore] = useState(0);

  const startRecording = () => {
    navigator.mediaDevices.getUserMedia({ audio: true })
      .then(stream => {
        mediaRecorderRef.current = new MediaRecorder(stream);
        mediaRecorderRef.current.start();
        setRecording(true);

        mediaRecorderRef.current.ondataavailable = (event) => {
          chunksRef.current.push(event.data);
        };

        mediaRecorderRef.current.onstop = (event) => {
          const audioBlob = new Blob(chunksRef.current, { type: 'audio/ogg; codecs=opus' });
          const audioUrl = URL.createObjectURL(audioBlob);

          console.log("Audio URL: ", audioUrl);
        };
      })
      .catch(error => {
        console.error("Error getting user media: ", error);
      });
  };

  const stopRecording = () => {
    mediaRecorderRef.current.stop();
    setRecording(false);
  };

  function handleSubmit(event) {
    event.preventDefault();
    if (answer.toLowerCase() === 'paris') {
      setScore(score + 1);
    }
  }

  return (
    <div>
    <h1>Question</h1>
    <p>{question}</p>
    <form onSubmit={handleSubmit}>
      {recording ? (
        <button onClick={stopRecording}>Stop</button>
      ) : (
        <button onClick={startRecording}>Start</button>
      )}
    </form>
    <p>Score: {score}</p>


    </div>
  );
};

export default RecordButton;