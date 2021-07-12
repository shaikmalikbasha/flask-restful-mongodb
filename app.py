from flask import Flask, jsonify, Response, request
from database.db import initialize_db
from database.models import Movie
from resources.movie_resource import movies

app = Flask(__name__)

app.config["MONGODB_SETTINGS"] = {"host": "mongodb://localhost/movie-bag"}
initialize_db(app)

app.register_blueprint(movies, url_prefix="/api")
app.run(debug=True)