import pdfkit
from bs4 import BeautifulSoup
import requests
import re
import os
from collections import Counter
import sys


def search_google(topic):
    base_url = 'https://www.google.com/search?q='
    response = requests.get(base_url + topic)
    if not response.ok:
        raise RuntimeError('error making request to {}'.format(base_url + topic))
    return response.content

def topic_to_pdfs(topic, path):
    urls_seen = []
    html_doc = search_google(topic)
    soup = BeautifulSoup(html_doc, 'html.parser')
    for i, link in enumerate(soup.find_all('a')):
        url = re.findall('/url\?q=(.+)&sa=U', link.get('href'))
        if url and url not in urls_seen:
            urls_seen.append(url[0])
            try:
                pdfkit.from_url(url[0], '{}/{}/{}.pdf'.format(path, topic, get_title(url[0])))
            except OSError:
                print('Unable to retrieve PDF from {}'.format(url[0]))

# I probably could do all of it in one request... but the pdfkit.from_url was the only method I found that
# webpages actually look good, so this will do for now. 
def get_title(url):
    response = requests.get(url)
    if not response.ok:
        return None
    return BeautifulSoup(response.content, 'html.parser').title.string.strip()

def get_topics(file_path):
    with open(file_path) as f:  
        topics = [topic.strip() for topic in f]
    return topics

def main(arguments):
    '''
    First argument should be the path to the list of requirements
    Second arugment should be the path to save the directories in (defaults to current directory)
    '''

    path = '.'
    if len(arguments) not in (2,3):
        raise OSError('Incorrect input to run program. The first argument should be the path to a list of requirments, \
            the second optional argument should the path to save the directories in (default is current directory)')
    topics = get_topics(arguments[1])
    if len(arguments) == 3:
        path = arguments[2]
    for topic in topics:
        try:
            os.mkdir('{}/{}'.format(path, topic))
        except OSError:
            print('Creation of the new directory {}/{} failed'.format(path, topic))
        else:
            print('Successfully created the directory {}/{}'.format(path, topic))
        topic_to_pdfs(topic, path)
    
    print('\nFinished')

main(sys.argv)