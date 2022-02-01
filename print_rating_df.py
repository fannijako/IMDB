from scraper import scraper
from review_penalizer import review_penalizer
from oscar_calculator import oscar_calculator
import datetime

def print_rating_df(index_range, sort_by = 'rank', ascending = True, return_b = False):
    '''scrape the top n movie
    and calculate the review penalizer
    as well as the oscar calculator'''

    df = scraper(index_range)
    df = review_penalizer(df)
    df = oscar_calculator(df)

    df = df.sort_values(by = sort_by, ascending = ascending)

    today = datetime.date.today()
    now = datetime.datetime.now()
    df.to_excel('final_imdb_top_' + str(index_range) + '_ratings_'
                + str(today.strftime('%b_%d_%Y')) + '_' + str(now.strftime("%H_%M_%S")) + '.xlsx')

    if return_b:
        return df

if __name__ == '__main__':
    df = print_rating_df(20, return_b = True)
    print(df)