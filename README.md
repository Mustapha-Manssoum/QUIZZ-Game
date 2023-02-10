# Développement d’une application web de quiz qu’on a nommé QuiTSE.

## Ce projet comporte principalement 3 grandes parties:
	### - L’entrainement d’un modèle machine learning à fin qu’il reconnaisse des audios 
	### - Le développement d’une interface utilisateur (Front-End + Back-End)
	### - Déploiement de l’application dans un cloud AWS avec stockage des données, modèles et réponses dans le cloud aussi.

## Partie 1: ML: Modèle de reconnaissance vocale:

### speech_recognition.ipynb

On a utilisé pour la reconnaissance vocale le model « speech_recognition », une bibliothèque Python qui utilise l’API de Google Speech Recognition.

1 -Le modèle prend comme entrée un audio qui sera enregistrer en utilisant le microphone 🎙.

-La méthode listen de l'objet recognizer est utilisée pour écouter l'audio provenant du microphone. L'objet audio est ensuite transmis à la méthode recognize_google, qui effectue la reconnaissance de la parole en utilisant Google Speech Recognition et en spécifiant que la reconnaissance doit être effectuée en français (fr-FR).
-La variable text stocke la réponse prononcé par l'utilisateur, qui va être comparée par la suite avec les réponses que nous avons définie pour notre quizz dans une base de données.

2 -Le modèle prend comme entrée un fichier audio .
  - La bibliothèque librosa fournit par Python, est utilisée pour charger et traiter des fichiers audio.
  -  La fonction librosa.load est ensuite utilisée pour charger les données audio et la fréquence d'échantillonnage à partir du fichier audio dont il faut préciser le chemain d'accès .
 Par la suite on a utilisé la même bibliothèque cité dans la méthode1:  « speech_recognition » pour convertir l’audio en texte.



### Quizz model.ipynb

On a utilisé un script python qui va effectuer le traitement de fichiers audio. Il définit deux listes, labels et mfcc_features, pour stocker les étiquettes et les caractéristiques MFCC respectivement.

On a utilisé, par la suite, la fonction os.listdir pour parcourir tous les sous-dossiers dans le dossier "new_data". Pour chaque sous-dossier, il parcourt également tous les fichiers audio à l'aide de os.listdir. Pour chaque fichier audio, il utilise la bibliothèque librosa pour charger le fichier audio et extraire les caractéristiques MFCC.

On a répartis notre data à train_set et test_set, on a utilisé comme modèle pour entraîner la data; SVC (Support Vector Classification) du module sklearn.svm. L'objet entraîné est stocké dans la variable H. Le modèle peut maintenant être utilisé pour prédire des labels pour des données de test en utilisant la méthode predict.

La fonction accuracy_score est utilisée pour évaluer la précision du modèle en comparant les labels réelles y_train avec les labels prédites y_pred. Le score de précision est stocké dans la variable train_accuracy. On fait de même pour data test. 

## Partie 2: Développement de l'interface utilisateur: Back-End + Front-End


## Partie 3: Hébergement Cloud









