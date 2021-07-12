from flask import Blueprint, Response, request
from database.models import Movie
from flask_restful import Resource


class MovieApiList(Resource):
    def get(self):
        movies = Movie.objects().to_json()
        return Response(movies, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        movie = Movie(**body).save()
        id = movie.id
        return {"msg": "New Movie added to Database", "created_movie": movie}, 200


class MovieApi(Resource):
    def get(self, movie_id):
        movies = Movie.objects.get(id=movie_id).to_json()
        return Response(movies, mimetype="application/json", status=200)

    def put(self, movie_id):
        body = request.get_json()
        updated_movie = Movie.objects.get(id=movie_id).update(**body)
        return "Updated", 200

    def delete(self, movie_id):
        Movie.objects.get(id=movie_id).delete()
        return "Deleted", 200
