"""
==================================================
Movies and series recommendation engine
==================================================

Authors:
Alicja Szczypior
Krzysztof Szczypior

To run the program, install the following Python packages (if required):
pip3 install NumPy
pip3 install argparse

This program uses a movie or series recommendation engine based on collaborative filtering. It uses K-means concept for
machine learning application.
It provides personalized recommendations for users by analyzing their movie preferences and comparing them with other
users in the dataset.

Please ensure that your movie data is stored in a JSON file ('movieData.json') with the following format:
{
    "user1": {"movie1": rating1, "movie2": rating2, ...},
    "user2": {"movie1": rating1, "movie2": rating2, ...},
    ...
}

To run the program use the command line to provide user and score type:

python3 main.py --user --score-type <score_type>

--user: Input user, as a String.
--score-type: Choose between Euclidean, Pearson, or MSE distance metrics, as a String.

"""

import json

from recommentation_engine.RecommendationEngine import get_recommendations
from parser_tool.ArgsParser import create_arg_parser

'''
     Displays movie recommendations for a given user.
     
     Parameters:
        user (string): user for which the recommendation will be printed
        movies (list): list of recommended movies in desc score order
        scoreType (string): The type of score used for recommendations (e.g. "Euclidean", "Pearson", "MSE").
 '''


def print_recommendations(user, movies, scoreType):
    print("\nMovie recommendations for: " + user + ".")
    print("\nDistance metric: " + scoreType)

    print("\nThe most recommended for " + user + ":")
    for i, movie in enumerate(movies[:5]):
        print(f"{i + 1}. {movie}")

    print("\nDefinitely not recommended for " + user + ":")
    for i, movie in enumerate(reversed(movies[-5:])):
        print(f"{i + 1}. {movie}")


if __name__ == '__main__':
    args = create_arg_parser().parse_args()
    user = args.user
    score_type = args.score_type

    ratings_file = 'resources/movieData.json'
    with open(ratings_file, 'r') as file:
        data = json.loads(file.read())

    if score_type == 'Euclidean':
        movies = get_recommendations(data, user, "euclidean")
        print_recommendations(user, movies, score_type)
    elif score_type == 'Pearson':
        movies = get_recommendations(data, user, "pearson")
        print_recommendations(user, movies, score_type)
    elif score_type == 'MSE':
        movies = get_recommendations(data, user, "mse")
        print_recommendations(user, movies, score_type)
    else:
        TypeError('Wrong score type: ' + score_type + '.')
