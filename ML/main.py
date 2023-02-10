import speech_recognition
import librosa
import soundfile as sf
import base64
from flask_cors import CORS
from flask import Flask, request
app = Flask(__name__)
CORS(app)

def decode_base64_to_wav(base64_string):
    # remove the header information from the base64 string
    wav_bytes = base64.b64decode(base64_string)
    
    # write the bytes to a file
    with open("output.mp3", "wb") as f:
        f.write(wav_bytes)


@app.route('/audio', methods=['POST'])
def handle_request():
    # Récupérer les données du corps de la requête
    data = request.get_json()
    print(data)
    text = ''
    base64_string = data['audioData']
    decode_base64_to_wav(base64_string)
    data, sr = librosa.load('output.mp3')
    sf.write("example.wav", data, sr)

    recognizer = speech_recognition.Recognizer()

    with speech_recognition.AudioFile("example.wav") as wavaudio:
        audio = recognizer.record(wavaudio, duration=5)
        
        # recognize speech using Google Speech Recognition
        try:
            text = recognizer.recognize_google(audio, language='fr-FR')
            text = text.lower()
        except speech_recognition.UnknownValueError:
            text = "Je n'ai pas compris votre audio, pouvez-vous le répéter"
        except speech_recognition.RequestError as e:
            text = "Could not request results from Google Speech Recognition service; {0}".format(e)
    return {
        'statusCode': 200,
        'body': text
    }




if __name__ == '__main__':
    app.run(debug=True)