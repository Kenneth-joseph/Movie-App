from flask import render_template
from app import app
from .request import get_movies


@app.route('/')
def index():
    """   
     View root page function that returns the index page and its data
    """
    popular_movies = get_movies('popular')
    upcoming_movie= get_movies('upcoming')
    now_showing_movie= get_movies('now_playing')
    # print(popular_movies)

    title = 'Home-welcome to the best movie review website online'
    message = "hello kent"
    return render_template('index.html', message=message, title=title, popular=popular_movies,upcoming=upcoming_movie,now_showing=now_showing_movie)


@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    """
      View root page function that returns the index page and its data
    """
    title = movie_id
    return render_template('movie.html', title=title)
