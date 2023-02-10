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
### Front-End
Pour cette partie on a developé sur react. La première page est la page de login. 

Login : représente un formulaire de connexion. Le composant utilise la fonctionnalité de gestion d'état de React avec le hook useState pour gérer les valeurs des entrées email et mot de passe. La fonction handleSubmit est utilisée pour gérer l'événement de soumission du formulaire et afficher l'email dans la console. Les entrées du formulaire sont des composants contrôlés et leurs valeurs sont stockées dans les variables d'état 'email' et 'pass'. Il y a un bouton qui, lorsqu'il est cliqué, appelle la fonction props.onFormSwitch et passe l'argument 'Quiz' en argument. Il y a également un bouton qui, lorsqu'il est cliqué, appelle la fonction props.onFormSwitch et passe l'argument 'register' en argument.

register : gère l'inscription d'un nouvel utilisateur. Il utilise la méthode useState pour gérer les états de trois champs de formulaire : email, mot de passe et nom complet. Lorsque l'utilisateur soumet le formulaire en cliquant sur le bouton "S'inscrire", la méthode handleSubmit est appelée pour prévenir la soumission par défaut et afficher les données entrées par l'utilisateur dans la console. Si l'utilisateur a déjà un compte, il peut cliquer sur le bouton "Déjà inscrit ? Connectez-vous ici" pour basculer vers le formulaire de connexion.

Quiz : permet à un utilisateur de choisir des thèmes pour un quiz. Le composant utilise un tableau de thèmes appelé themes et stocke les thèmes sélectionnés par l'utilisateur dans un état local appelé selectedThemes.
Lorsqu'un utilisateur clique sur une case à cocher, la fonction handleChange est appelée et met à jour selectedThemes en ajoutant ou en supprimant le thème correspondant.
Le composant affiche un formulaire qui affiche tous les thèmes contenus dans le tableau themes sous forme de cases à cocher. Si un thème est sélectionné, sa case à cocher sera cochée.
Enfin, il y a un bouton qui appelle une fonction onFormSwitch passée en tant que propriété au composant pour permettre à l'utilisateur de démarrer le quiz.

Audio : crée un composant React qui permet de faire un enregistrement audio. Il utilise une bibliothèque appelée "AudioRecorder" pour enregistrer la voix de l'utilisateur. Il affiche également une question et une sélection de réponses et calcule le score de l'utilisateur en fonction de sa réponse. Le score est affiché à l'écran.

### Back-End
Cette partie est basé sur NodeJS

app : Ce code crée une application Express et utilise des routes pour les questions et les utilisateurs. Il utilise également le middleware CORS pour permettre les demandes croisées et écoute sur le port 3033 en affichant un message de démarrage du serveur.

Question : Ce code importe express et le modèle Question et Reponse de la base de données.
Il crée un routeur pour les questions, avec deux routes. La première route est pour obtenir toutes les questions ou une catégorie spécifique de questions en fonction des paramètres de requête. La deuxième route est pour créer une nouvelle question avec des réponses associées.

user : Ce code définit un routeur pour les utilisateurs en utilisant le framework Express.js. Le routeur contient deux routes principales: une pour récupérer toutes les réponses enregistrées et une autre pour envoyer de nouvelles réponses. La première route utilise la méthode findAll pour récupérer toutes les entrées dans la table des réponses et les renvoie en utilisant res.send. La deuxième route utilise la méthode post pour accepter des données envoyées par l'utilisateur, les affiche en utilisant console.log et renvoie un message simple "post user". Finalement, le routeur est exporté pour être utilisé dans un autre fichier.


 
## Partie 3: Hébergement Cloud

Pour l'hébergement dans le cloud. 
On utilise l'instance EC2 pour déployer la partie Back et front, le modèle de machine learning entraînée est déployé dans une fonction lambda. Pour la base de données MySQL a été déployer dans un moteur de base de donnée RDS d'Amazon.
Le back récupère les questions de RDS et les transfère sous format json vers le front. 
L'utilsateur répond en audio. Un fichier ".wav" va être transféré vers la fonction lambda pour être traité et convertit en texte. 
La fonction Lambda renvoie par la suite le texte vers le front.









