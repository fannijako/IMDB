def print_rating_df(index_range, sort_by = 'rank', ascending = True, return_b=False):
    '''scrape the top n movie
    and calculate the review penalizer
    as well as the oscar calculator'''

    df = scraper(index_range)
    df = review_penalizer(df)
    df = oscar_calculator(df)

    df = df.sort_values(by = sort_by, ascending = ascending)
    df.to_excel('final_imdb_top_' + str(index_range) + '_ratings.xlsx')

    if return_b:
        return df