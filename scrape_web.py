# from pprint import pprint
from bs4 import BeautifulSoup
import requests
# import pandas as pd
# import newspaper
from newspaper import fulltext
# from segtok.segmenter import split_single


## REQUIREMENTS:
# pip install newspaper3k
# pip install bs4

# find by tags
def extractByTags(url, tag, class_name=None):
    """
    Args:
        url: Web URL intended to scrape
        tag: HTML tags where the content is. E.g: "h1", "div", "script"
        class_name: the tag class. Default is None
        id_name: the tag id. Default is None

    Returns:
        The content within the specified tag of the given url
    """
    
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    # FIND A SINGLE TAG
    if class_name==None:
        tag = soup.find(tag)
    else:
        tag = soup.find(tag, class_=class_name)

    ## TO FIND ALL TAGS OF THE SAME NAME USE BELOW INSTEAD:
    # tags = soup.find_all(tag, class_=class_name, id=id_name)
    # return tags

    return tag

# extract all text contents
def extractPlainText(url):
    """
    Extract the texts from a given url.
    """
    html = requests.get(url).text
    body = fulltext(html)

    return body


## Implement
URL = "enter url here"
print(extractByTags(URL, tag="h1"))

print(extractPlainText(URL))
