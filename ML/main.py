import speech_recognition
import librosa
import soundfile as sf
import base64
from flask_cors import CORS
from flask import Flask, request
app = Flask(__name__)
CORS(app)


# Transformer la donnée de la base64 au format mp3 et la stocker dans un fichier output.mp3
def decode_base64_to_mp3(base64_string):
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
    decode_base64_to_mp3(base64_string)
    #  Lire le fichier mp3
    data, sr = librosa.load('output.mp3')
    # Transformer l'audio mp3 au format wav
    sf.write("example.wav", data, sr)

    recognizer = speech_recognition.Recognizer()

    with speech_recognition.AudioFile("example.wav") as wavaudio:
        audio = recognizer.record(wavaudio, duration=5)
        
        # reconnaître la parole à l'aide de Google Speech Recognition
        try:
            text = recognizer.recognize_google(audio, language='fr-FR')
            text = text.lower()
        except speech_recognition.UnknownValueError:
            text = "Je n'ai pas compris votre audio, pouvez-vous le répéter ?"
        except speech_recognition.RequestError as e:
            text = "Impossible de demander les résultats du service de reconnaissance vocale Google; {0}".format(e)
    return {
        'statusCode': 200,
        'body': text  # envoyer le text transcrit
    }




if __name__ == '__main__':
    app.run(debug=True)