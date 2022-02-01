from beautifulsoup4 import BeautifulSoup
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
    ''' reshaping a list of lists to a 1 dimensional list '''

    my_list = []
    for i in link_list:
        if i not in my_list:
            my_list.append(i)

    return my_list

link_list = unique_list(link_list)

def create_soup(url, sub_1):
    ''' creating a html soup from a html sites subsite'''
    link = url + sub_1
    html_page = urlopen(link)
    soup = BeautifulSoup(html_page, 'lxml')

    return soup

# test with the first film from the top250 list
soup = create_soup('https://www.imdb.com', link_list[0])