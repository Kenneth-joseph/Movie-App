from app import app
from instance.config import MOVIE_API_KEY
from models import movie
import urllib.request,json

Movie=movie.Movie

# getting API key

api_key = app.config['MOVIE_API_KEY']

# Getting the movie base url
base_url = app.config["MOVIE_API_BASE_URL"]
