import numpy as np
from lightfm.datasets import fetch_movielens
from lightfm import LightFM
# Choose data points with min rating of 4.0 or above 
# fetch_movielens is a csv file that contains 110 movies from 1k users
data = fetch_movielens(min_rating = 4.0)

# Uses content + collaborative system
model = LightFM(loss = 'warp') # WARP(Weighted Approximate-Rank Pairwise) uses SGD
model.fit(data['train'],epochs=30,num_threads = 2)

def sample_recommendation(model, data, user_ids):
    n_users, n_items = data['train'].shape

    for user_id in user_ids:
        known_positives = data['item_labels'][data['train'].tocsr()[user_id].indices]

        scores = model.predict(user_id, np.arange(n_items))
        top_items = data['item_labels'][np.argsort(-scores)]

        print("User %s" % user_id)
        print("     Known positives:")

        for x in known_positives[:3]:
            print("        %s" % x)

        print("     Recommended:")

        for x in top_items[:3]:
            print("        %s" % x)

sample_recommendation(model, data, [3, 25, 450])
