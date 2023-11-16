import numpy as np

'''
    Calculates the similarity between two users based on the Euclidean metric

    Parameters:
        dataset (dict): A dictionary containing movie ratings from various users.
        user1 (str): Name of the first user.
        user2 (str): Name of the second user (for compare purpose).
    
    Returns:
        similarity_score (numpy.float64): Pearson correlation coefficient between users (-1 to 1, where 1 means full similarity).
'''


def euclidean_score(dataset, chosen_user, user):
    common_movies = {}

    for movie in dataset[chosen_user]:
        if movie in dataset[user]:
            common_movies[movie] = 1

    if len(common_movies) == 0:
        return 0

    squared_diff = []

    for movie in dataset[chosen_user]:
        if movie in dataset[user]:
            squared_diff.append(np.square(dataset[chosen_user][movie] - dataset[user][movie]))

    return 1 / (1 + np.sqrt(np.sum(squared_diff)))
