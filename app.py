from flask import Flask, render_template, request

from main import get_genre, get_movie_details, get_movie_by_year, recursion

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        if 'content' in request.form:
            content = request.form['content']
            movie = get_movie_details(get_genre(content))
            is_movie = []

            for key in movie:
                is_movie.append(movie[key])

            return render_template('index.html', is_movie=is_movie)

        else:
            year = request.form['year']
            is_movie = recursion(year)

            return render_template('index.html', is_movie=is_movie)

    else:
        is_movie = ''

        return render_template('index.html', is_movie=is_movie)


if __name__ == '__main__':
    app.run()
