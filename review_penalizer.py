import numpy as np
import math
import datetime

def review_penalizer(df, save = False):
    '''Compare every movie’s number of reviews to the
    maximum review number from the top20
    and penalize each of them based on the following rule:
    Every 100 000 deviation from the maximum translates to a
    point deduction of 0.1. '''

    df = df.sort_values(by = 'rank', ascending = True)

    if df.shape[0] > 20:
        top_20 = df.iloc[0:20]
    else:
        top_20 = df
    max_rating = max(top_20.ratingNumber)

    df['pen_rating'] = df.apply(lambda row:
                                row.aggregateRating - 0.1 * math.floor((max_rating - row.ratingNumber) / 100000)
                                if row.ratingNumber < max_rating
                                else row.aggregateRating,
                                axis = 1)

    df = df.sort_values(by = 'pen_rating', ascending = False)

    if save:
        today = datetime.date.today()
        now = datetime.datetime.now()
        df.to_excel('imdb_top_' + str(len(df.pen_rating)) + 'review_penalized' +
                    str(today.strftime('%b_%d_%Y')) + '_' + str(now.strftime("%H_%M_%S")) + '.xlsx')

    return df