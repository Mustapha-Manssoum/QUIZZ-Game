import React, { useState, useRef } from 'react';
import Recorder from 'recorder-js';

const MicButton = () => {
  const [isRecording, setIsRecording] = useState(false);
  const [audioBlob, setAudioBlob] = useState(null);
  const stream = useRef(null);
  const recorder = useRef(null);

  const startRecording = async () => {
    try {
      stream.current = await navigator.mediaDevices.getUserMedia({ audio: true });
      recorder.current = new Recorder(stream.current, {
        numChannels: 1,
        encoding: 'wav',
        sampleRate: 44100,
      });
      recorder.current.record();
      setIsRecording(true);
    } catch (error) {
      console.error('Error accessing user media', error);
    }
  };

  const stopRecording = async () => {
    try {
      recorder.current.stop();
      stream.current.getTracks().forEach(track => track.stop());
      setAudioBlob(await recorder.current.exportWAV());
      setIsRecording(false);
    } catch (error) {
      console.error('Error stopping recording', error);
    }
  };

  const handleUpload = async () => {
    try {
      const formData = new FormData();
      formData.append('audio', audioBlob, 'audio.wav');
      const response = await fetch('https://your-lambda-function-url.com/upload', {
        method: 'POST',
        body: formData,
      });
      const result = await response.json();
      console.log('Upload result:', result);
    } catch (error) {
      console.error('Error uploading audio', error);
    }
  };

  return (
    <div>
      {isRecording ? (
        <button onClick={stopRecording}>Stop Recording</button>
      ) : (
        <button onClick={startRecording}>Start Recording</button>
      )}
      {audioBlob && (
        <button onClick={handleUpload}>Upload</button>
      )}
    </div>
  );
};

export default MicButton;