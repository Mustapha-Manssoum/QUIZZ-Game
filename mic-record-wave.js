import logo from './logo.svg';
import './App.css';
import { getDefaultNormalizer } from '@testing-library/react';
import React, { useState, useRef } from 'react';



const App = () => {
  const [recording, setRecording] = useState(false);
  const [audioURL, setAudioURL] = useState(null);

  const startRecording = () => {
    navigator.mediaDevices.getUserMedia({ audio: true })
      .then(stream => {
        const mediaRecorder = new MediaRecorder(stream);
        mediaRecorder.start();

        const chunks = [];
        mediaRecorder.addEventListener("dataavailable", event => {
          chunks.push(event.data);
        });

        mediaRecorder.addEventListener("stop", () => {
          const audioBlob = new Blob(chunks, { type: "audio/wav; codecs=opus" });
          setAudioURL(URL.createObjectURL(audioBlob));
        });

        setTimeout(() => {
          mediaRecorder.stop();
        }, 1500);
      });
  };

  return (
    <div style={{ display: "flex", flexDirection: "column", alignItems: "center" }}>
      <button onClick={startRecording} style={{ backgroundColor: "#F45D25", color: "white", padding: "10px 20px", borderRadius: "5px", border: "none", outline: "none", cursor: "pointer", fontWeight: "bold" }}>
        {recording ? "Stop Recording" : "Start Recording"}
      </button>
      {audioURL && (
        <audio src={audioURL} controls style={{ marginTop: "20px", width: "100%" }} />
      )}
    </div>
  );
};

export default App;
