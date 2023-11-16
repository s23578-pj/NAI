import numpy as np

'''
    Calculates the Pearson correlation coefficient between two users based on movie ratings.

    Parameters:
        dataset (dict): A dictionary containing movie ratings from various users.
        user1 (str): Name of the first user.
        user2 (str): Name of the second user (for compare purpose).
    
    Returns:
        similarity_score (numpy.float64): Pearson correlation coefficient between users (-1 to 1, where 1 means full similarity).
'''


def pearson_score(dataset, user1, user2):
    common_movies = {}

    for item in dataset[user1]:
        if item in dataset[user2]:
            common_movies[item] = 1

    num_ratings = len(common_movies)

    if num_ratings == 0:
        return 0

    user1_sum = np.sum([dataset[user1][item] for item in common_movies])
    user2_sum = np.sum([dataset[user2][item] for item in common_movies])

    user1_squared_sum = np.sum([np.square(dataset[user1][item]) for item in common_movies])
    user2_squared_sum = np.sum([np.square(dataset[user2][item]) for item in common_movies])

    sum_of_products = np.sum([dataset[user1][item] * dataset[user2][item] for item in common_movies])

    xy = sum_of_products - (user1_sum * user2_sum / num_ratings)
    xx = user1_squared_sum - np.square(user1_sum) / num_ratings
    yy = user2_squared_sum - np.square(user2_sum) / num_ratings

    if xx * yy == 0:
        return 0

    return xy / np.sqrt(xx * yy)
