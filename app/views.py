from flask import render_template
from app import app


@app.route('/')
def index():
    """   
     View root page function that returns the index page and its data
    """
    title = 'Home-welcome to the best movie review website online'
    message = "hello kent"
    return render_template('index.html', message=message, title=title)


@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    """
      View root page function that returns the index page and its data
    """
    title = movie_id
    return render_template('movie.html', title=title)
