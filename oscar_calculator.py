import pandas as pd
import numpy as np
import datetime

def oscar_calculator(df, save = False):
    '''increases the IMDb score with:
    0.3 points if the film won 1 or 2 Oscars
    0.5 points if the film won 3 to 5 Oscars
    1 point if the film won 6 to 10 Oscars
    1.5 points if the film won more than 10 Oscars'''

    df['oscar_rating'] = df.apply(lambda row:
                                  row.aggregateRating + 1.5 if row.Oscar > 10
                                  else row.aggregateRating + 1 if row.Oscar > 5
                                  else row.aggregateRating + 0.5 if row.Oscar > 2
                                  else row.aggregateRating + 0.3 if row.Oscar > 0
                                  else row.aggregateRating,
                                  axis = 1)

    df = df.sort_values(by = 'oscar_rating', ascending = False)
    if save:
        today = datetime.date.today()
        now = datetime.datetime.now()
        df.to_excel('imdb_top_' + str(len(df.oscar_rating)) + 'oscar_adjusted' +
                    str(today.strftime('%b_%d_%Y')) + '_' + str(now.strftime("%H_%M_%S")) + '.xlsx')

    return df