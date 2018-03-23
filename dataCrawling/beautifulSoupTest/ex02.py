#네이버 무비에서 영화 랭킹 가져오기

import urllib.request
from bs4 import BeautifulSoup

url = "http://movie.naver.com/movie/sdb/rank/rmovie.nhn"

html = urllib.request.urlopen(url)

soup = BeautifulSoup(html, 'html.parser')
url_header = 'http://movie.naver.com'
tags = soup.findAll('div', attrs={'class':'tit3'})
for tag in tags:
    print(tag.a.text, end = "  -  ")
    print(url_header+tag.a.get('href'))    #tag.g.['href']
    print('-'*80)