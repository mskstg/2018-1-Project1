from bs4 import BeautifulSoup
from urllib.request import urlopen
import nltk


# 1-1. print title, author, date, video title, article content using BeautifulSoup
# TODO - fill in your team's url
url = 'http://money.cnn.com/2018/04/02/technology/mark-zuckerberg-tim-cook-facebook-apple/index.html'

data = urlopen(url).read()
doc = BeautifulSoup(data, 'html.parser')
# print(doc)
# TODO - print title
title = doc.find("meta", attrs={"name":"title"}).get("content")
print("Title: ", title)

# TODO - print author
author = doc.find("meta", attrs={"name":"author"}).get("content")
print("Author: ", author)

# TODO - print date
date = doc.find("meta", attrs={"name":"date"}).get("content")
print("Date: ", date)

# TODO - print video title
video_title = doc.find("div", attrs={"class":"cnnVidFooter"}).get_text()
print("Video title: ", video_title)

# TODO - print article content
container = doc.find("div", id="storytext")
content_list = [p.string for p in container.findAll("p") if p.string]
content = "\n".join(content_list)

print("Content: ", content)


# 1-2. Tokenize news article content by words
# TODO - tokenize article content
tokenized_words = nltk.word_tokenize(content)

print(tokenized_words)


# 1-3. POS-Tag tokenized words and sort POS by frequency
# TODO - POS_Tag tokenized words
tagged_list = nltk.pos_tag(tokenized_words)
print(tagged_list)

# TODO - sort POS by frequency
from collections import Counter
counter = Counter([el[1] for el in tagged_list])
print(counter)
# for tag in tagged_list:
#     pass
