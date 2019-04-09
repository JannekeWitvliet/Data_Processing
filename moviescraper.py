#!/usr/bin/env python
# Name: Janneke Witvliet
# Student number: 10508848
"""
This script scrapes IMDB and outputs a CSV file with highest rated movies.
"""

import csv
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

TARGET_URL = "https://www.imdb.com/search/title?title_type=feature&release_date=2008-01-01,2018-01-01&num_votes=5000,&sort=user_rating,desc"
BACKUP_HTML = 'movies.html'
OUTPUT_CSV = 'movies.csv'


def extract_movies(dom):
    """
    Extract a list of highest rated movies from DOM (of IMDB page).
    Each movie entry should contain the following fields:
    - Title
    - Rating
    - Year of release (only a number!)
    - Actors/actresses (comma separated if more than one)
    - Runtime (only a number!)
    """
    list_moviecontents = []

    # loop through different movie contents to obtain information
    for content in dom.find_all('div', attrs={'class':'lister-item-content'}):
        # obtain title
        Title = content.h3.a.string
        # obtain rating
        Rating = content.strong.string
        # obtain year of release
        year_release = (content.find('span', attrs={'class':'lister-item-year text-muted unbold'}).string)
        Year = int(''.join(list(filter(str.isdigit, year_release))))
        # obtain Actor/actresses
        link_list = content.find_all('a')
        actors_list =[]
        for actors_links in link_list:
            if '_st_' in actors_links['href']:
                actors_list.append(actors_links.string)
        # make actors one string
        Actors = ', '.join(actors_list)

        # obtain runtime
        runtime_movie = (content.find('span', attrs={'class':'runtime'}).string)
        Runtime = int(''.join(list(filter(str.isdigit, runtime_movie))))

        # add all the information to a list in a big list of all movie information
        list_moviecontents.append([Title, Rating, Year, Actors, Runtime])

    return list_moviecontents


def save_csv(outfile, movies):
    """
    Output a CSV file containing highest rated movies.
    """
    writer = csv.writer(outfile)
    writer.writerow(['Title', 'Rating', 'Year', 'Actors', 'Runtime'])
    # iterate over every list that contains movie info and write it in a csv file
    for list in movies:
        writer.writerow(list)

def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None
    except RequestException as e:
        print('The following error occurred during HTTP GET request to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns true if the response seems to be HTML, false otherwise
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


if __name__ == "__main__":

    # get HTML content at target URL
    html = simple_get(TARGET_URL)

    # save a copy to disk in the current directory, this serves as an backup
    # of the original HTML, will be used in grading.
    with open(BACKUP_HTML, 'wb') as f:
        f.write(html)

    # parse the HTML file into a DOM representation
    dom = BeautifulSoup(html, 'html.parser')

    # extract the movies (using the function you implemented)
    movies = extract_movies(dom)

    # write the CSV file to disk (including a header)
    with open(OUTPUT_CSV, 'w', newline='') as output_file:
        save_csv(output_file, movies)
