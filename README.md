<h1 align="center"> Défiez vos connaissances avec QuiTSE : le Jeu de Quiz en ligne</h1>

# Objectif : 
L'objectif de ce projet est de concevoir une application web qui présente un jeu de Quiz, où les réponses sont données par l'utilisateur.rice à la voix.
<br>

## Ce projet comporte principalement 3 grandes parties:

- La partie **Machine learning** concernant le modèle de reconnaissance vocal
- Le développement de l'interface web et la communication avec la base de données (**Front-End** + **Back-End**)
- Le déploiement de l’application dans le **cloud AWS** avec stockage de toutes les données.

## Partie 1: Machine Learning: Modèle de reconnaissance vocale:
Au cours de notre travail sur cette partie, nous avons commencé par apprendre un modèle à partir de zéro en utilisant les données que nous avons collectées, représentant des fichiers audio des mots suivants : **"un"**, **"deux"**, **"trois"** et **"quatre"**. Les données sont stockées selon leur classe dans le fichier **"new_data"** dans le dossier **"Model1"**. <br>
Chaque classe contient 20 fichiers audio correspondant au mot approprié.<br>
Le modèle d'apprentissage automatique que nous avons conçu consiste à parcourir les données classe par classe et à extraire les caractéristiques MFCC (Mel-frequency cepstrum) ainsi que le label de chaque fichier audio. Il crée ensuite un vecteur représentatif de cet audio en utilisant la moyenne et l'écart-type de ses caractéristiques MFCC. Toutes les caractéristiques sont stockées avec leur label dans une liste appelée "mfcc_features". Les données sont ensuite divisées en deux parties : un jeu de données d'entraînement et un jeu de données de validation. <br>
Nous avons choisi l'algorithme SVM en tant que classificateur pour entraîner le modèle.<br>
**Résultat:** <br>
- Précision sur le jeu de données d'entraînement : **58.73%**<br>
- Précision sur le jeu de données de validation : **56.25%**<br>
Nous constatons que le modèle fonctionne assez bien, surtout avec un jeu de données aussi restreint. Pour améliorer sa précision, nous devons collecter plus de données. Étant donné que notre application doit être efficace et précise, nous avons choisi d'utiliser un modèle pré-entraîné de la bibliothèque **"speech_recognition"**, que nous vous présentons ci-dessous.<br>
Le code de ce modèle se trouve dans le fichier **"Quizz model.ipynb"** dans le dossier "Model1".<br><br>

Afin de mettre en œuvre notre modèle final qui peut prendre en entrée un fichier audio au format WAV, nous avons utilisé une API Flask développée en Python pour héberger ce modèle. Ce modèle utilise la bibliothèque "speech_recognition" pour transcrire le mot prononcé par l'utilisateur en un texte compréhensible.<br>
Ce code se concentre sur la préparation de l'audio reçu du front-end en format base64. Il le décode en un fichier MP3, puis le convertit en un fichier WAV avant de l'envoyer à la fonction de transcription. Une fois la transcription terminée, le texte est envoyé au front-end pour être affiché en tant que réponse de l'utilisateur.<br>
Les détails de code se trouvent dans le dossier **ML** *(main.py)*
 

## Partie 2: Développement de l'interface utilisateur: Back-End + Front-End
- ### Front-End
Nous avons utilisé ReactJS pour développer la partie frontend du projet. Elle comprend l'affichage de la page d'inscription ou de connexion de l'utilisateur, ainsi que l'affichage du jeu Quiz qui permet à l'utilisateur de répondre en utilisant son microphone. Il est important de noter que le frontend est api rest qui communique avec le backend pour obtenir les questions à afficher et envoyer les informations du formulaire saisi par l'utilisateur (cette partie n'est pas encore finalisée !), ainsi qu'avec le modèle ML pour obtenir la transcription du texte qui sera affiché en tant que réponse de l'utilisateur.<br>
Les détails de code se trouvent dans le dossier **front-end_web**<br>
- ### Back-End

Pour le développement du backend, nous utilisons Node.js avec le framework Express. Il définit la structure de la base de données et assure la communication avec celle-ci. Le backend envoie des requêtes POST sous forme de fichiers JSON pour alimenter la base de données avec les questions du quiz, et des requêtes GET pour récupérer les questions désirées. En plus de cela, le backend communique également avec le frontend pour envoyer les questions ou les informations de l'utilisateur nécessaires (cette partie est à compléter aussi !).<br>
En ce qui concerne la base de données, nous avons choisi MySQL qui sera hébergée dans le cloud grâce à la solution RDS (Amazon Relational Databases) d'AWS. Cela permet d'attribuer une adresse IP à cette base de données pour que le backend puisse communiquer avec elle.<br>
Les détails de code se trouvent dans le dossier **back-end**<br>
## Partie 3: Hébergement Cloud

- La base de données des questions est stockée dans la solution de déployement de base de données relationnelles **RDS** proposée par AWS.
<img src="https://user-images.githubusercontent.com/63628060/218280449-53dbd3de-d495-466c-a2cc-3ed268c1fd8b.png" alt="c" width="400" height="200"/>
<br>
- Tous les autres serveurs backend, frontend et l'API du modèle ML sont déployés sur une instance EC2 utilisant une image Ubuntu qui a été configurée pour prendre en charge tous les modules nécessaires et modifier les groupes de sécurité afin de permettre au ports utilisés par les serveurs d'être atteints, pour assurer une communication adéquate entre les serveurs.<br>
<img src="https://user-images.githubusercontent.com/63628060/218280741-8189e150-d9dc-4844-8a3b-0cc3fad72b68.png" alt="c" width="400" height="200"/>

<br> 

### NOTE : <br>
Nous avons commencé en utilisant la solution AWS Lambda pour déployer notre modèle ML, mais cela n'a pas été possible en raison du grand volume du fichier zip contenant les dépendances du code du modèle. Nous aurions pu stocker ces dépendances dans un bucket S3 et y accéder à partir de la fonction Lambda, mais le compte AWS étudiant ne nous permettait pas de configurer les autorisations nécessaires pour cela.







