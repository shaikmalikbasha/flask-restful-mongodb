from .movie_resource import MovieApi, MovieApiList


def initialize_routes(api):
    api.add_resource(MovieApiList, "/api/movies")
    api.add_resource(MovieApi, "/api/movies/<movie_id>")
