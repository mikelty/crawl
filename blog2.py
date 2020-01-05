'''

local
craws http://www.paulgraham.com/
paul wrote 'hackers and painters' and is a famous programmer, and a decent human being in general.

'''
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

base_url = "http://www.paulgraham.com/"
resp = urlopen(base_url+"articles.html")
soup = BeautifulSoup(resp,features="html.parser")
#posts' link selector parts
sel_1='body > table > tr > td:nth-child(3) > table:nth-child(5) > tr:nth-child('
sel_2=') > td > font > a'
urls = []
for i in range(2,368+2,2):
    a=soup.select(sel_1+str(i)+sel_2)[0]
    urls.append(a['href'])
all_posts = [base_url+url for url in urls]
#article selector
content_sel='body > table > tr > td:nth-child(3) > table:nth-child(4) > tr > td > font'
#statistics
succ, fail = 0,0
for post in all_posts:
    try:
        resp = urlopen(post)
        soup = BeautifulSoup(resp,features="html.parser")
        name = soup.head.title.getText()
        content = soup.select(content_sel)[0].getText()
        with open(name+'.txt', 'w') as f:
            f.write(name)
            f.write('\n\n')
            f.write(content)
        succ += 1
        print('crawled %s\n'%post)
    except:
        fail += 1
        print('failed to crawl %s\n'%post)
        pass
