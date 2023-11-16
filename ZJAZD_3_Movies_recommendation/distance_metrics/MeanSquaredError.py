import numpy as np

'''
    Calculate the similarity between two users based on the Mean Squared Error (MSE) metric.

    Parameters:
        dataset (dict): A dictionary containing movie ratings from various users.
        user1 (str): Name of the first user.
        user2 (str): Name of the second user (for compare purpose).
    
    Returns:
        similarity_score (numpy.float64): Pearson correlation coefficient between users (-1 to 1, where 1 means full similarity).
'''


def mean_squared_error_score(dataset, chosen_user, user):
    common_movies = {}

    for movie in dataset[chosen_user]:
        if movie in dataset[user]:
            common_movies[movie] = 1

    if len(common_movies) == 0:
        return 0

    diff = []
    count = 0

    for movie in dataset[chosen_user]:
        if movie in dataset[user]:
            diff.append(np.abs(dataset[chosen_user][movie] - dataset[user][movie]))
            count += 1

    return 1 / (1 + ((1/count) * np.sum(diff)))
