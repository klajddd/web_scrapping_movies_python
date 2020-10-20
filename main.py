import random
import requests
from bs4 import BeautifulSoup

# THIS PROGRAM USES BEAUTIFUL SOUP TO SCRAP THE HIGHEST RATED MOVIES ON IMDB AND SUGGESTS MOVIES TO WATCH.

# URL of IBDM's top 250 rated movies
url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'


def get_year(movie_tag):

    moviesplit = movie_tag.text.split()
    year = moviesplit[-1]
    return year


def get_title(movie_tag):
    return movie_tag.text


def get_actor(movie_tag):
    actors = movie_tag['title']
    return actors


def get_rating(movie_tag):
    rating = movie_tag['data-value']
    float_rating = float(rating)
    rounded_rating = round(float_rating, 1)
    return rounded_rating


def suggest_movie(years, titles, actors, ratings, number_of_movies):
    while(True):
        idx = random.randrange(0, number_of_movies)
        print(
            f'TITLE: {titles[idx]}, YEAR: {years[idx]}, RATING: {ratings[idx]}, STARRING: {actors[idx]}')
        user_input_continue = input(
            'Do you want to watch another movie (y/[n])?')
        if user_input_continue.lower() != 'y':
            break


def main():
    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')

    movietags = soup.select('td.titleColumn')
    inner_movietags = soup.select('td.titleColumn a')
    ratingstags = soup.select('td.posterColumn span[name=ir]')

    # list comprehensions
    years = [get_year(tag) for tag in movietags]
    titles = [get_title(tag) for tag in inner_movietags]
    actors = [get_actor(tag) for tag in inner_movietags]
    ratings = [get_rating(tag) for tag in ratingstags]

    number_of_movies = len(titles)

    suggest_movie(years, titles, actors, ratings, number_of_movies)


if __name__ == "__main__":
    main()
