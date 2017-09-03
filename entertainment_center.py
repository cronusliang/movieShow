import fresh_tomatoes
from get_movie_data import get_movies

movies = get_movies()
fresh_tomatoes.open_movies_page(movies)