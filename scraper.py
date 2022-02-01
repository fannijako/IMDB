import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random
import pandas as pd
import datetime

def get_links(url, tag):
    '''get all links from an html webpage (url)
    which starts with a selected string (tag)'''

    html_page = urlopen(url)
    soup = BeautifulSoup(html_page, features = 'lxml')

    links = []

    for link in soup.findAll('a', attrs={'href': re.compile(tag)}):
        links.append(link.get('href'))

    return links

def unique_list(link_list):
    '''reshaping a list of lists to a one-dimensional list with unique values '''

    my_list = []
    for i in link_list:
        if i not in my_list:
            my_list.append(i)

    return my_list

def create_soup(url, sub_1, sub_2 = ''):
    '''creating an html soup from an html sites, subsite or subsites'''

    link = url + sub_1 + sub_2
    html_page = urlopen(link)
    soup = BeautifulSoup(html_page, features = 'lxml')

    return soup

def title_scraper(soup):
    '''get the title of the movie from a BeautifulSoup object of an IMDb site'''

    s_title = soup.findAll('h1', attrs={'class': re.compile('TitleHead')})

    if s_title == []:
        return 0

    return s_title[0].string

def aggregate_rating_scraper(soup):
    '''get the aggregate rating of the movie from a BeautifulSoup object of an IMDb site'''

    s_rating = soup.findAll('span', attrs={'class': re.compile('AggregateRating')})

    if s_rating == []:
        return 0

    return float(s_rating[0].string)

def rating_number_scraper(soup):
    '''get the number of ratings of the movie from the BeautifulSoup object
    of the SUBSITE of an IMDB site
    subsite: https://www.imdb.com/title....../ratings'''

    s_number = soup.findAll('div', attrs={'class': re.compile('allText')})

    if s_number == []:
        return 0

    s_number = s_number[1].get_text()
    s_number = s_number.splitlines()[1].strip()
    s_number = s_number.replace(',', '')

    return int(s_number)

def oscar_number_scraper(soup):
    '''get the number of Oscars of the movie from the BeautifulSoup object
    of the IMDb site'''

    s_Oscar = soup.findAll('div', attrs={'class': re.compile("Awards__List-sc-152rtbv-1 eKsukd")})

    if s_Oscar == []:
        return 0

    Oscar = s_Oscar[0].next_sibling.findAll('a')[0].string

    if Oscar is None:
        return 0

    Oscar = Oscar.split()
    if Oscar[0] == 'Won' and (Oscar[2] == 'Oscar' or Oscar[2] == 'Oscars'):
        return int(Oscar[1])
    else:
        return 0

def get_film_attributes(index_range, link_list):
    '''scrape the 4 attributes (title, aggregate Rating, rating Number, Oscar)
    for the first n (index_range) films from the link_list list - the top n
    films in the IMDb chart'''

    title_list = []
    aggregateRating_list = []
    ratingNumber_list = []
    Oscar_list = []

    for index in range(index_range):

        main_soup = create_soup('https://imdb.com', link_list[index])
        sub_soup = create_soup('https://imdb.com', link_list[index], 'ratings')

        title_list.append(title_scraper(main_soup))
        aggregateRating_list.append(aggregate_rating_scraper(main_soup))
        ratingNumber_list.append(rating_number_scraper(sub_soup))
        Oscar_list.append(oscar_number_scraper(main_soup))

    df = {'title': title_list,
          'aggregateRating': aggregateRating_list,
          'ratingNumber': ratingNumber_list,
          'Oscar': Oscar_list,
          'rank': range(1, index_range + 1)}
    df = pd.DataFrame(df)

    return df

def scraper(index_range, save = False):
    '''download the link list and the top n film attributes'''

    link_list = get_links('https://www.imdb.com/chart/top/', '^/title')
    link_list = unique_list(link_list)

    df = get_film_attributes(index_range, link_list)

    if save:
        today = datetime.date.today()
        now = datetime.datetime.now()
        df.to_excel('imdb_top_' + str(index_range) +
                    str(today.strftime('%b_%d_%Y')) + '_' + str(now.strftime("%H_%M_%S")) + '.xlsx')

    return df