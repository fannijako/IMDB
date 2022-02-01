import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random
import pandas as pd

def get_links(url, tag):
    '''get all links from a html webpage (url)
    wich start with a selected string (tag)'''

    html_page = urlopen(url)
    soup = BeautifulSoup(html_page)

    links = []

    for link in soup.findAll('a', attrs={'href': re.compile(tag)}):
        links.append(link.get('href'))

    return links

# downloading all the links from the IMDB top250 list which start with /title
link_list = get_links('https://www.imdb.com' + "/chart/top/", '^/title')

def unique_list(link_list):
    '''reshaping a list of lists to a 1 dimensional list '''

    my_list = []
    for i in link_list:
        if i not in my_list:
            my_list.append(i)

    return my_list

link_list = unique_list(link_list)

def create_soup(url, sub_1, sub_2 = ''):
    '''creating a html soup from a html sites subsite or subsites'''

    link = url + sub_1 + sub_2
    html_page = urlopen(link)
    soup = BeautifulSoup(html_page)

    return soup

# test with one of the films from the top250 list
random_integer = random.randrange(0, 250)
soup = create_soup('https://www.imdb.com', link_list[random_integer])

def title_scraper(soup):
    '''get the title of the movie from a BeautifulSoup object of an IMDB site'''

    s_title = soup.findAll('h1', attrs={'class': re.compile('TitleHead')})

    if s_title == []:
        return 0

    return s_title[0].string

# test with one of the films from the top250 list
title = title_scraper(soup)
print('title')
print(title)

def aggregate_rating_scraper(soup):
    '''get the aggregate rating of the movie from a BeautifulSoup object of an IMDB site'''

    s_rating = soup.findAll('span', attrs={'class': re.compile('AggregateRating')})

    if s_rating == []:
        return 0

    return float(s_rating[0].string)

# test with one of the films from the top250 list
aggregateRating = aggregate_rating_scraper(soup)
print('IMDB rating')
print(aggregateRating)

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

# test with one of the films from the top250 list
sub_soup = create_soup('https://www.imdb.com', link_list[random_integer], 'ratings')
ratingNumber = rating_number_scraper(sub_soup)
print('Number of ratings')
print(ratingNumber)

def oscar_number_scraper(soup):
    '''get the number of Oscars of the movie from the BeautifulSoup object
    of the IMDB site'''

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

# test with one of the films from the top250 list
Oscar = oscar_number_scraper(soup)
print('Number of Oscars')
print(Oscar)

def get_film_attributes(index_range, link_list):
    '''scrape the 4 attributes (title, aggregate Rating, rating Number, Oscar)
    for the first n (index_range) films from the link_list list - the top n
    films in the IMDB chart'''

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
        df.to_excel('imdb_top_' + str(index_range) + '.xlsx')

    return df

# scrape the first 20 film in one function
df = scraper(20)
print(df)