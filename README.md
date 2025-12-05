# TP_API_CRUD – API Flask + Authentification + SQLite

Ce projet est une application web simple écrite en **Python (Flask)** permettant :
- l’inscription d’utilisateurs
- la connexion
- l’affichage de pages HTML (login, register, recherche)
- l’utilisation d’une base SQLite
- la page recherche fait l'appel a un API pour trouver des films et series
- une fois le film ou la serie trouver un bouton plus de détail fais un autre appel a l'api pour avoir le détails sur celle ci


Il sert de TP pour apprendre les bases d’un backend Flask + base de données + templates.

---

## Structure du projet

app/
- main.py → point d’entrée Flask
- database.py → gestion de la base SQLite
- data.db → base SQLite
- models/
  - user.py → modèle utilisateur
- templates/
  - login.html
  - register.html
  - recherche.html

---

## Installation sur votre machine

### 1. Prérequis
- Python 3.9+


Vérifier Python :
python --version

### 2. Cloner le projet
git clone https://github.com/RPintre/TP_API_CRUD.git
cd TP_API_CRUD/app

### 3. Créer un environnement virtuel (recommandé)
python -m venv venv

Activer l’environnement :
- Windows : venv\Scripts\activate
- Linux/macOS : source venv/bin/activate

### 4. Installer les dépendances
pip install flask
pip install alchemysql
pip install requests


---

## Lancer l’application

Depuis le dossier app :
python app.main

L’application démarre sur :
http://localhost:5000

---

## Fonctionnement général

### Base de données
- type : SQLite
- fichier : data.db
- gestion : database.py

### Templates HTML
- /login → page de connexion
- /register → inscription
- /recherche → interface de recherche

### Modèle utilisateur
Défini dans models/user.py  
Contient les champs essentiels (email, mot de passe, etc.)

---

## Endpoints principaux

### Inscription
- URL : /register
- Méthodes : GET (form), POST (validation)

### Connexion
- URL : /login
- Méthodes : GET (form), POST (auth)

### Recherche
- URL : /recherche
- Méthode : GET

---

## Tests

L’application peut être testée avec :
- un navigateur web
- Postman
- curl

---

## Technologies utilisées
- Python
- Flask
- SQLite

---

## Auteur
Projet développé par **Romain Pintre** dans le cadre d’un TP API/CRUD.
