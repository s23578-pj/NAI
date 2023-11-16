import numpy as np
from distance_metrics.Euclidean import euclidean_score
from distance_metrics.Pearson import pearson_score
from distance_metrics.MeanSquaredError import mean_squared_error_score


'''
    Parameters:
        dataset (dict): Dictionary analyzed videos from varius users.
        chosen_user (str): The username for which the recommendation was made.
        score_type (str): The type of score used for calculations ("euclidean", "pearson", or "mse").
    
    Returns:
        list: as list of recommended movies for the chosen user
    
    +----------------------
    Engine action steps
    +----------------------
    #1 Calculation of Distance: Calculate the distance (rating of user1 - rating of user2) based on the chosen method.
    #2 Calculation of Coefficient: Calculate the coefficient between users, which is then used in subsequent computations.
    #3 Movie Scoring: For each movie rated by other users (excluding movies already rated by the target user),
    multiply the score by the computed coefficient.
    #4 Create a Movie List: Generate a list of movies with scores resulting from coefficients between different users.
    #5 Normalization: Normalize the scores on the list to account for variations in coefficient magnitudes.
       Only the movies over a chosen score level are considered to be recommended or not: 
       - Euclidean less or equal 0.3,
       - Pearson less or equal 0.7,
       - MSE less or equal 0.4.
    #6 Sorting: Sort the list of movies in descending order based on scores, resulting in a finalized list ready for
    recommendations.
'''


def get_recommendations(dataset, chosen_user, score_type):
    if chosen_user not in dataset:
        raise TypeError('Missing ' + chosen_user + ' in the dataset')

    ov = {}

    for user in [x for x in dataset if x != chosen_user]:
        if score_type == "euclidean":
            similarity_score = euclidean_score(dataset, chosen_user, user)
        elif score_type == "pearson":
            similarity_score = pearson_score(dataset, chosen_user, user)
        else:
            similarity_score = mean_squared_error_score(dataset, chosen_user, user)

        if score_type == "mse" and similarity_score <= 0.3:
            continue
        elif score_type == "pearson" and similarity_score <= 0.7:
            continue
        elif score_type == "euclidean" and similarity_score <= 0.1:
            continue

        filtered_list = [movie for movie in dataset[user] if movie not in dataset[chosen_user]
                         or dataset[chosen_user][movie] == 0]

        for movie in filtered_list:
            if movie not in ov:
                ov.update({movie: [dataset[user][movie] * similarity_score, similarity_score]})
            else:
                temp_weight = similarity_score + ov[movie][1]
                weighted_average = (dataset[user][movie] * similarity_score + ov[movie][0]) / temp_weight
                ov.update({movie: [weighted_average, temp_weight]})

    if len(ov) == 0:
        return ['No recommendations possible']

    movie_scores = np.array([[data[0] * data[1], movie] for movie, data in ov.items()])
    movie_scores = movie_scores[np.argsort(movie_scores[:, 0].astype(float))[::-1]]

    movie_recommendations = [movie for _, movie in movie_scores]

    return movie_recommendations
