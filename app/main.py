from app.database import Base, engine, SessionLocal
from flask import Flask, render_template, request, redirect, session, url_for, jsonify
from app.models.user import User
import os
import requests

Base.metadata.create_all(engine)

app = Flask(__name__)
app.secret_key = "ton_secret_key"  #

def get_user_session():
    return session.get("user_id")

# Page principale
@app.get("/")
def index():
    if get_user_session():
        return redirect(url_for("recherche"))  # redirige vers la page locale items si connecté
    return render_template("login.html")

# Inscription
@app.route("/register", methods=["GET", "POST"])
def register():
    session_db = SessionLocal()
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if session_db.query(User).filter_by(username=username).first():
            return "Utilisateur déjà existant"
        user = User(username=username)
        user.set_password(password)
        session_db.add(user)
        session_db.commit()
        session_db.close()
        return redirect(url_for("login"))
    session_db.close()
    return render_template("register.html")

# Login
@app.route("/login", methods=["GET", "POST"])
def login():
    session_db = SessionLocal()
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = session_db.query(User).filter_by(username=username).first()
        if user and user.check_password(password):
            session["user_id"] = user.id
            session_db.close()
            return redirect(url_for("recherche"))
        session_db.close()
        return render_template("login.html", error="Identifiants incorrects")
    session_db.close()
    return render_template("login.html")

# Logout
@app.get("/logout")
def logout():
    session.pop("user_id", None)
    return redirect(url_for("index"))

@app.get("/recherche")
def recherche():
    if not get_user_session():
        return redirect(url_for("login"))
    return render_template("recherche.html")

# OMDB API Key
OMDB_KEY = "17d6d8c5"

@app.route("/search")
def search_movie():
    query = request.args.get("q")
    url = f"https://www.omdbapi.com/?apikey={OMDB_KEY}&s={query}"
    response = requests.get(url)
    return jsonify(response.json())

@app.route("/details")
def movie_details():
    imdb_id = request.args.get("id")
    url = f"https://www.omdbapi.com/?apikey={OMDB_KEY}&i={imdb_id}"
    response = requests.get(url)
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(debug=True)
