from flask import Flask, jsonify, Response, request
from database.db import initialize_db
from resources.routes import initialize_routes
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

app.config["MONGODB_SETTINGS"] = {"host": "mongodb://localhost/movie-bag"}
initialize_db(app)

initialize_routes(api)
app.run(debug=True)