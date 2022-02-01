# IMDB
An application that scrapes data from IMDB and adjusts IMDB ratings based on some rules.

*Review penalizer*: Compare every movie’s number of reviews to the maximum review number from the top20 and penalize each of them based on the following rule: 
Every 100 000 deviation from the maximum translates to a point deduction of 0.1.

*Oscar calculator*: increases the IMDb score with:
    0.3 points if the film won 1 or 2 Oscars
    0.5 points if the film won 3 to 5 Oscars
    1 point if the film won 6 to 10 Oscars
    1.5 points if the film won more than 10 Oscars.

## Language
Python 3.8

### Libraries
BeautifulSoup, datetime, math, numpy, pandas, re, urllib

## Functions

Scraper, Review_penalizer, Oscar_calculator

### Scraper
Main site: IMDb Top 250 - https://www.imdb.com/chart/top/

Data: top 20 movies /sorted by IMDb rating/
    
    - Title
    
    - IMDb rating
    
    - Number of ratings
    
    - Number of Oscars
    
    - IMDb ranking
    
#### Functions

get_links: get all links from an html webpage (url), which starts with a selected string (tag) - get all the links from the IMDb Top 250 page, which start with the /title tag

unique_list: reshape a list of lists to a one-dimensional list with unique values

create_soup: creating an html soup from a html site, subsite or subsites - create BeautifulSoup object for every movie's site from the Top 250 list and its 'ratings' subsite

title_scraper: get the title of the movie from a BeautifulSoup object of an IMDB site - access the h1 tag from the site with class: TitleHead

aggregate_rating_scraper: get the aggregate rating of the movie from a BeautifulSoup object of an IMDB site - access the span tag from the site with class: AggregateRating

rating_number_scraper: get the number of ratings of the movie from the BeautifulSoup object
of the SUBSITE of an IMDB site, subsite: https://www.imdb.com/title....../ratings - access the div tag from the subsite with class: allText

oscar_number_scraper: get the number of Oscars of the movie from the BeautifulSoup object of the IMDB site - access the div tag from the site with class Awards__List-sc-152rtbv-1 eKsukd and find the next sibling (possible values: Won 1 Oscar, Won N Oscars, Nominated for N Oscars, Won N BAFTA Awards, Awards, Empty)

get_film_attributes: scrape the 4 attributes (title, aggregate Rating, rating Number, Oscar) for the first n (index_range) films from the link_list list - the top n films in the IMDB chart

scraper: download the link list and the top n film attributes - all the functions above in one function - write out to an Excel file

### Review penalizer 

Compare every movie’s number of reviews to the maximum review number from the top20 and penalize each of them based on the following rule: Every 100 000 deviation from the maximum translates to a point deduction of 0.1 - write out to an Excel file.

### Oscar calculator

Increases the IMDb score with:
    0.3 points if the film won 1 or 2 Oscars
    0.5 points if the film won 3 to 5 Oscars
    1 point if the film won 6 to 10 Oscars
    1.5 points if the film won more than 10 Oscars - write out to an Excel file.

### Print rating df

Scrape the top n movie and calculate the review penalizer as well as the oscar calculator, sorts the values according to the original IMDb ranking / or the review_penalized or oscar_calculated ranking/ and writes out the data frame to an Excel file
