import os
from flask import Flask
from flask import render_template
import imdb
import random

app = Flask(__name__)
ia = imdb.IMDb()

app.debug=True

def selectRandomMovie():
    movies = ia.search_movie('% age%', results=500)
    movie = movies[random.randint(0, len(movies))]
    return movie

@app.route('/')
def hello():
    movie = selectRandomMovie()
    while not 'Age' in movie['title']:
      movie = selectRandomMovie()
    title = movie['title'].replace('Age','Cage')
    return render_template('age.html',title=title,id=movie.getID())

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
