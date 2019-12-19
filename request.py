from app import app
from instance.config import MOVIE_API_KEY

# getting API key

api_key = app.config[MOVIE_API_KEY]
