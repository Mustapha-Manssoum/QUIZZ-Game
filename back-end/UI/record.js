// Create a new audio context
const audioContext = new (window.AudioContext || window.webkitAudioContext)();

// Request access to the user's microphone
navigator.mediaDevices.getUserMedia({ audio: true })
  .then(stream => {
    // Create a MediaStreamAudioSourceNode from the user's microphone
    const source = audioContext.createMediaStreamSource(stream);

    // Create an AnalyserNode to analyse the audio data
    const analyser = audioContext.createAnalyser();
    source.connect(analyser);

    // Create a Uint8Array to receive the audio data
    const dataArray = new Uint8Array(analyser.frequencyBinCount);

    // Function to update the audio data
    function update() {
      requestAnimationFrame(update);

      // Get the audio data from the AnalyserNode
      analyser.getByteFrequencyData(dataArray);

      // Use the audio data here
      console.log(dataArray);
      download(dataArray);
      source.disconnect();
      audioContext.close();
    }

    // Start updating the audio data
    update();
  })
  .catch(error => {
    console.error(error);
  });

// Function to download the dataArray as a text file
function download(dataArray) {
  const data = dataArray.join('\n');
  const blob = new Blob([data], { type: 'text/plain' });
  const link = document.createElement('a');
  link.href = URL.createObjectURL(blob);
  link.download = 'dataArray.txt';
  link.click();
}
