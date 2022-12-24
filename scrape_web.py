# from pprint import pprint
from bs4 import BeautifulSoup
import requests, re
# import pandas as pd
# import newspaper
from newspaper import fulltext
# from segtok.segmenter import split_single

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
    tags = soup.find_all(tag, class_=class_name, id=id_name)
    return tags

    return tag

# extract all text contents
def extractPlainText(url):
    """
    Extract the texts from a given url.
    """
    html = requests.get(url).text
    body = fulltext(html, language="es")

    return body


## Implement
# URL = "https://www.blanes.cat/docweb/agenda-2022-10-01-vela"
#URL = "https://www.blanes.cat/docweb/agenda-2022-09-stageentrenadorsfutbolsala"
URL = "https://www.blanes.cat/docweb/agenda-2022-09-19-policialocal"
# print(extractByTags(URL, tag="h1"))

# print(extractPlainText(URL))

### IMAGE
html = requests.get(URL).text
soup = BeautifulSoup(html, 'html.parser')
print("\n")

image = soup.find_all("img")[-1]
# for image in images:
#     if "oiapdocs" in image["src"]:
#         img.append(image)
if "https://www.blanes.cat" in image["src"]:

    print(image["src"])
else:
    image_src = "https://www.blanes.cat"+image["src"]
    print(image_src)

### TITLE
# html = requests.get(URL).text
# soup = BeautifulSoup(html, 'html.parser')
# title = soup.find_all("h1")[-1]

# print(title.get_text())

### DATE
# html = requests.get(URL).text
# soup = BeautifulSoup(html, 'html.parser')
# print("\n")

tables = soup.find_all("table")
for table in tables:
    dt = table.get_text()
    split_dt = dt.split("\n")
    str_list = list(filter(None, split_dt))
    # print(str_list)
    for item in str_list:
        splt = item.split()
        # print(splt)
        first_word = splt[0]
        first_word_ = re.findall('[A-Z][^A-Z]*', first_word)
        splt.pop(0) # remove the first list item
        if type(first_word_)=="str":
            print(first_word_+": ")
        else:
            splt = first_word_[1:] + splt
            print(first_word_[0]+": "+" ".join([str(item) for item in splt]))
        print("\n")



# class Scrape:
#     def __init__(self, url):
#         html = requests.get(url).text
#         self.soup = BeautifulSoup(html, 'html.parser')

#     def image(self, tag="img"):

#         image = self.soup.find_all(tag)[-1]
#         if "https://www.blanes.cat" in image["src"]:

#             image_ = image["src"]
#         else:
#             image_ = "https://www.blanes.cat"+image["src"]

#             return image_

#     def title(self, tag="h1"):
#         title = self.soup.find_all(tag)[-1]
#         title_ = title.get_text()
#         return title_

#     def date(self, tag="table"):
#         tables = self.soup.find_all(tag)
#         for table in tables:
#             dt = table.get_text()
#             split_dt = dt.split("\n")
#             str_list = list(filter(None, split_dt))
#             print(str_list)
#             for item in str_list:
#                 splt = item.split()
#                 # print(splt)
#                 first_word = splt[0]
#                 first_word_ = re.findall('[A-Z][^A-Z]*', first_word)
#                 splt.pop(0)  # remove the first list item
#                 if type(first_word_) == "str":
#                     data = first_word_+": "
#                     return data
#                 else:
#                     splt = first_word_[1:] + splt
#                     data = first_word_[0]+": "+" ".join([str(item) for item in splt])
#                     return data



# print(Scrape.title(URL))
# for line in dt:
#     print(line)
#     print("\n")
    # dt_ = re.findall('[A-Z][^A-Z]*', dt)
    # print(dt_)

    # x = "".join([(":"+i if i.isupper() else i)
    #     for i in dt]).strip().split()
    # print(x)

