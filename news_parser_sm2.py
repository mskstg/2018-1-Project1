from bs4 import BeautifulSoup
from urllib.request import urlopen
import nltk


print("# 1-1. print title, author, date, video title, article content using BeautifulSoup")
# TODO - fill in your team's url
url = 'http://money.cnn.com/2018/04/02/technology/mark-zuckerberg-tim-cook-facebook-apple/index.html'

data = urlopen(url).read()
doc = BeautifulSoup(data, 'html.parser')

# TODO - print title
title = doc.find( "h1", class_="article-title speakable").string;
print("Title: ", title)

# TODO - print author
author = doc.find("span", class_ = "byline").string;
print("Author: ", author)

# TODO - print date
date = doc.find("span", class_ = "cnnDateStamp").string;
print("Date: ", date)

# TODO - print video title
video_title = doc.find(class_ = "js-vid-hed-vid0 cnnHeadline").string;
print("Video title: ", video_title)

# TODO - print article content
content = ""
content_raw = doc.find(id="storytext")
content_sliced = content_raw.find_all("h2")
content_sliced.extend(content_raw.find_all("p"))
for s in content_sliced:
    content += s.text
print("Content: ", content)

print('''


''')

print("# 1-2. Tokenize news article content by words")
# TODO - tokenize article content
tokenized_words = nltk.tokenize.word_tokenize(content)
print(tokenized_words)

print('''


''')

print("# 1-3. POS-Tag tokenized words and sort POS by frequency")
# TODO - POS_Tag tokenized words
tagged_list = nltk.pos_tag(tokenized_words)
print(tagged_list)

print('''


''')

# TODO - sort POS by frequency
dictionary = dict()
for tag in tagged_list:
    if(tag[1] in dictionary) : #품사가 사전 안에 있으면 패스
        pass
    else : #품사가 사전 안에 없다면
        POScount = sum(x[1].count(tag[1]) for x in tagged_list)
        dictionary.update({tag[1] : POScount})

#dictionary의 빠른 정렬을 위한 operator 모듈을 import
import operator
sortedArray = sorted(dictionary.items(), key = operator.itemgetter(1), reverse=True)

for d in sortedArray:
    print(d[0])

