from flask import Flask, jsonify, Response, request
from database.db import initialize_db
from database.models import Movie

app = Flask(__name__)

app.config["MONGODB_SETTINGS"] = {"host": "mongodb://localhost/movie-bag"}
initialize_db(app)


@app.route("/movies")
def get_movies():
    movies = Movie.objects().to_json()
    return Response(movies, mimetype="application/json", status=200)


@app.route("/movies", methods=["POST"])
def add_movie():
    body = request.get_json()
    movie = Movie(**body).save()
    id = movie.id
    return {"msg": "New Movie added to Database", "created_movie": movie}, 200


@app.route("/movies/<id>", methods=["GET"])
def get_movie(id):
    movies = Movie.objects.get(id=id).to_json()
    return Response(movies, mimetype="application/json", status=200)


@app.route("/movies/<id>", methods=["PUT"])
def update_movie(id):
    body = request.get_json()
    updated_movie = Movie.objects.get(id=id).update(**body)
    return jsonify("updated_movie", updated_movie), 200


@app.route("/movies/<id>", methods=["DELETE"])
def delete_movie(id):
    Movie.objects.get(id=id).delete()
    return "Deleted", 200


app.run(debug=True)