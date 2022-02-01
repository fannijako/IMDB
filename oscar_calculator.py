import pandas as pd
import numpy as np


def oscar_calculator(df, save = False):
    '''increases the imdb score with:
    0.3 point if the film won 1 or 2 oscars
    0.5 point if the film won 3 to 5 oscars
    1 point if the film won 6 to 10 oscars
    1.5 point if the film won more than 10 oscars'''

    df['oscar_rating'] = df.apply(lambda row:
                                  row.aggregateRating + 1.5 if row.Oscar > 10
                                  else row.aggregateRating + 1 if row.Oscar > 5
                                  else row.aggregateRating + 0.5 if row.Oscar > 2
                                  else row.aggregateRating + 0.3 if row.Oscar > 0
                                  else row.aggregateRating,
                                  axis = 1)

    df = df.sort_values(by = 'oscar_rating', ascending = False)
    if save:
        df.to_excel('imdb_top_' + str(len(df.oscar_rating)) + 'oscar_adjusted.xlsx')

    return df