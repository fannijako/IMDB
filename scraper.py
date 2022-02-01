from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

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

# test with the first film from the top250 list
soup = create_soup('https://www.imdb.com', link_list[0])

def title_scraper(soup):
    '''get the title of the movie from a BeautifulSoup object of an IMDB site'''

    s_title = soup.findAll('h1', attrs={'class': re.compile('TitleHead')})

    return s_title[0].string

# test the first film from the top250 list
title = title_scraper(soup)

def aggregate_rating_scraper(soup):
    '''get the aggregate rating of the movie from a BeautifulSoup object of an IMDB site'''

    s_rating = soup.findAll('span', attrs={'class': re.compile('AggregateRating')})

    return float(s_rating[0].string)

# test the first film from the top250 list
aggregateRating = aggregate_rating_scraper(soup)

def rating_number_scraper(soup):
    '''get the number of ratings of the movie from the BeautifulSoup object
    of the SUBSITE of an IMDB site
    subsite: https://www.imdb.com/title....../ratings'''

    s_number = soup.findAll('div', attrs={'class': re.compile('allText')})

    s_number = s_number[1].get_text()
    s_number = s_number.splitlines()[1].strip()
    s_number = s_number.replace(',', '')

    return int(s_number)

# test with the first film from the top250 list
sub_soup = create_soup('https://www.imdb.com', link_list[0], 'ratings')
ratingNumber = rating_number_scraper(sub_soup)
print(ratingNumber)