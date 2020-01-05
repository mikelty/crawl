'''

local
craws aaronsw.com
aaron is a great person and pretty wise in general.

'''
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

url = "http://www.aaronsw.com/weblog/fullarchive"
resp = urlopen(url)
soup = BeautifulSoup(resp,features="html.parser")
all_href = [a['href'] for a in soup.find_all('a',href=True)]
base = "http://www.aaronsw.com/weblog/"
all_posts = [base + url for url in all_href]
for post in all_posts:
    try:
        resp = urlopen(post)
        soup = BeautifulSoup(resp,features="html.parser")
        name = soup.div.h1.getText()
        content = '\n\n'.join(p.getText() for p in soup.find_all('p'))
        with open(name+'.txt', 'w') as f:
            f.write(name)
            f.write('\n\n')
            f.write(content)
        print('crawled %s\n'%post)
    except:
        print('failed to crawl %s\n'%post)
        pass
