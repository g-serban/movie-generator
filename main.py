from random import randrange

from requests import request

from header import credentials_for_movie_db, credentials_for_imdb


# ----- imdb api ---- get by category


def get_genre(get_genre_from_content):

    url = "https://imdb8.p.rapidapi.com/title/get-popular-movies-by-genre"

    querystring = {"genre": "/chart/popular/genre/"f"{get_genre_from_content}"}

    headers = {
        'x-rapidapi-key': f"{credentials_for_imdb['key']}",
        'x-rapidapi-host': f"{credentials_for_imdb['host']}"
        }

    response = request("GET", url, headers=headers, params=querystring)

    movie_list = response.json()

    random_movie = randrange(0, 99)

    movie = movie_list[random_movie][7:-1]  # movie_list returns /title/tt000000/, for id we just need tt00000

    return movie


# ----- imdb api ---- get by year

def get_movie_by_year(year):

    url = "https://imdb8.p.rapidapi.com/title/find"

    querystring = {"q": f"{year}"}

    headers = {
        'x-rapidapi-key': f"{credentials_for_imdb['key']}",
        'x-rapidapi-host': f"{credentials_for_imdb['host']}"
        }

    response = request("GET", url, headers=headers, params=querystring)

    movie_list = response.json()

    random_movie = randrange(0, 18)

    return movie_list['results'][random_movie]['id'][7:-1]


# ----- movie database api ---- get by id info about movie

def get_movie_details(movie_id):

    url = "https://movie-database-imdb-alternative.p.rapidapi.com/"

    querystring = {"i": f"{movie_id}", "r": "json"}

    headers = {
        'x-rapidapi-key': f"{credentials_for_movie_db['key']}",
        'x-rapidapi-host': f"{credentials_for_movie_db['host']}"
        }

    response = request("GET", url, headers=headers, params=querystring)

    try:
        movie_details = response.json()
    except:
        get_movie_details(movie_id)

    return movie_details


def recursion(year):
    movie = get_movie_details(get_movie_by_year(year))

    while movie is not None:

        try:
            if movie['Type'] == 'movie' and movie['Year'] == year:
                is_movie = []

                for key in movie:
                    is_movie.append(movie[key])

                return is_movie if not None else recursion(year)

            else:
                recursion(year) if not None else recursion(year)
                break

        except:
            recursion(year) if not None else recursion(year)
            break


# TODO find out why recursion doesn't work on flask app but works on test2.py
# TODO display dictionary values separately
# TODO 3. add year option
# TODO 4. send from frontend info to backend, backend sends info to frontend with selected specifications
# TODO 5. display all information about the movie on frontend
# TODO 6. add a 'show another movie' option
# TODO 7. maybe add a search functionality
# TODO 8. deploy on heroku or aws
# TODO 9. add requirements.txt


