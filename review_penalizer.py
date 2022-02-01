import numpy as np
import math

def review_penalizer(df, save = False):
    '''Compare every movie’s number of reviews to the
    maximum review number from the top20
    and penalize each of them based on the following rule:
    Every 100k deviation from the maximum translates to a
    point deduction of 0.1. '''

    df = df.sort_values(by = 'rank', ascending = True)
    top_20 = df.iloc[0:20]
    max_rating = max(top_20.ratingNumber)

    df['pen_rating'] = df.apply(lambda row:
                                row.aggregateRating - 0.1 * math.floor((max_rating - row.ratingNumber) / 100000)
                                if row.ratingNumber < max_rating
                                else row.aggregateRating,
                                axis = 1)

    df = df.sort_values(by = 'pen_rating', ascending = False)

    if save:
        df.to_excel('imdb_top_' + str(len(df.pen_rating)) + 'review_penalized.xlsx')

    return df